"""first_migration

Revision ID: 5bf9c0657ebc
Revises: 452e60d0850b
Create Date: 2024-03-03 13:06:07.643359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bf9c0657ebc'
down_revision: Union[str, None] = '452e60d0850b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
