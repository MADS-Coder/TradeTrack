from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select, delete, update
from src.infra.providers import hash_provider


class RepositorioVendedor():

    def __init__(self, db: Session):
        self.db = db

    def criar_vendedor(self, vendedor: schemas.Vendedor):
        # Verifica se já existe um para a matrícula.
        vendedor_existente = self.obter_matricula_vendedor(vendedor.matricula)
        if vendedor_existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe um vendedor para esta matrícula."
            )

        # Realiza o hash da senha antes de salvar
        vendedor.senha = hash_provider.gerar_hash(vendedor.senha)

        db_vendedor = models.Vendedor(usuario_do_vendedor=vendedor.usuario_do_vendedor,
                                      matricula=vendedor.matricula, senha=vendedor.senha)
        self.db.add(db_vendedor)
        self.db.commit()
        self.db.refresh(db_vendedor)
        return db_vendedor

    def listar_vendedor(self):
        listar_vendedores = select(models.Vendedor)
        vendedores = self.db.execute(listar_vendedores).scalars().all()
        return vendedores

    def obter_matricula_vendedor(self, matricula_vendedor):
        # Buscar vendedor pela matrícula usando filter
        vendedor = self.db.query(models.Vendedor).filter(
            models.Vendedor.matricula == matricula_vendedor).first()

        if not vendedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Vendedor de matrícula {matricula_vendedor} não encontrado!'
            )

        return vendedor

    def atualizar_vendedor(self, matricula: str, vendedor: schemas.VendedorUpdate):
        # Busca o vendedor no banco
        vendedor_existente = self.db.query(models.Vendedor).filter(
            models.Vendedor.matricula == matricula).first()

        if not vendedor_existente:
            raise HTTPException(
                status_code=404, detail="Vendedor não encontrado")

        # Atualiza os dados
        vendedor_existente.usuario_do_vendedor = vendedor.usuario_do_vendedor
        vendedor_existente.senha = hash_provider.gerar_hash(vendedor.senha)

        # Salva as alterações
        self.db.commit()
        self.db.refresh(vendedor_existente)

        return vendedor_existente  # Agora retorna o vendedor atualizado

    def remover_vendedor(self, matricula_vendedor):
        # Cria uma consulta no banco de dados para a tabela 'Vendedor'
        vendedor = self.db.query(models.Vendedor).filter(
            models.Vendedor.matricula == matricula_vendedor).first()

        if not vendedor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'{matricula_vendedor} não encontrado!'
            )

        # Se o vendedor existir, remove ele do banco de dados
        self.db.delete(vendedor)
        # Confirma a operação de exclusão no banco de dados
        self.db.commit()

        # Retorna uma mensagem indicando sucesso na exclusão
        return {'Mensagem': f'O vendedor com matrícula {vendedor.matricula} foi removido com sucesso!'}
