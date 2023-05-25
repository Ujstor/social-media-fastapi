"""create post table

Revision ID: e90949b95aa9
Revises: 
Create Date: 2023-05-25 21:50:28.914894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e90949b95aa9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
