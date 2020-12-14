"""product table

Revision ID: 64c071e0061c
Revises: 
Create Date: 2020-12-13 20:57:36.008130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64c071e0061c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False, default=0)
    )


def downgrade():
    op.drop_table("product")
