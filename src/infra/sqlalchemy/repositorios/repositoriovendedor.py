from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select


class RepositorioVendedor():

    def __init__(self, db: Session):
        self.db = db

    def criar_vendedor(self, vendedor: schemas.Vendedor):
        db_vendedor = models.Vendedor(usuario_do_vendedor=vendedor.usuario_do_vendedor,
                                      senha=vendedor.senha)
        self.db.add(db_vendedor)
        self.db.commit()
        self.db.refresh(db_vendedor)
        return db_vendedor

    def listar_vendedor(self):
        listar_vendedores = select(models.Vendedor)
        vendedores = self.db.execute(listar_vendedores).scalars().all()
        return vendedores

    def remover_vendedor(self, usuario_do_vendedor):
        # Cria uma consulta no banco de dados para a tabela 'Vendedor'
        vendedor = self.db.query(models.Vendedor).filter(
            models.Vendedor.usuario_do_vendedor == usuario_do_vendedor).first()

        # Verifica se um vendedor foi encontrado
        if vendedor:
            # Se o vendedor existir, remove ele do banco de dados
            self.db.delete(vendedor)
            # Confirma a operação de exclusão no banco de dados
            self.db.commit()

            # Acessa o nome do vendedor deletado
            return {'Mensagem': f'O vendedor {vendedor.usuario_do_vendedor} foi removido com sucesso!'}

        return {'Mensagem': f'Vendedor {usuario_do_vendedor} não encontrado!.'}
