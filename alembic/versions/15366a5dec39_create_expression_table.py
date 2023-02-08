"""create expression table

Revision ID: 15366a5dec39
Revises: 
Create Date: 2023-02-08 01:50:05.441741

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "15366a5dec39"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "expression",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("expression", sa.String(256), nullable=False),
        sa.Column("result", sa.Boolean, nullable=False),
    )


def downgrade() -> None:
    pass
