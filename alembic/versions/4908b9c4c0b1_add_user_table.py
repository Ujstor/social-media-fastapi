"""add user table

Revision ID: 4908b9c4c0b1
Revises: ef2418aa2b26
Create Date: 2023-05-25 22:11:10.717241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4908b9c4c0b1'
down_revision = 'ef2418aa2b26'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
