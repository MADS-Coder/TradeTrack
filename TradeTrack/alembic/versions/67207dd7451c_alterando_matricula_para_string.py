"""Alterando matricula para string

Revision ID: 67207dd7451c
Revises: fc2a962672c8
Create Date: 2025-04-01 16:55:58.370164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67207dd7451c'
down_revision: Union[str, None] = 'fc2a962672c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
