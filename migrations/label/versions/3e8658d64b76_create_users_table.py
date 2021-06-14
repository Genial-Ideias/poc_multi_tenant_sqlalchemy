"""create users table

Revision ID: 3e8658d64b76
Revises:
Create Date: 2021-06-14 17:07:12.935751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e8658d64b76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(60), nullable=False),
        sa.Column('password', sa.String(30), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade(engine_name):
    op.drop_table('users')
