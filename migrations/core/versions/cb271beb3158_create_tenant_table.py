"""create tenant table

Revision ID: cb271beb3158
Revises: 
Create Date: 2021-06-14 11:49:40.977377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb271beb3158'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tenants',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('code', sa.String(20), nullable=False),
        sa.Column('domain', sa.String(150), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade():
    op.drop_table('tenants')
