"""create users table

Revision ID: ba6614ca4f13
Revises:
Create Date: 2021-06-14 15:39:16.855579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba6614ca4f13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(60), nullable=False),
        sa.Column('password', sa.String(30), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade():
    op.drop_table('users')
