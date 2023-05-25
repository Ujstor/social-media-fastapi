"""add content column to post table

Revision ID: ef2418aa2b26
Revises: e90949b95aa9
Create Date: 2023-05-25 22:01:33.130178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef2418aa2b26'
down_revision = 'e90949b95aa9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
