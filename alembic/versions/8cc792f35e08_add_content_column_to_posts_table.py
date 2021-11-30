"""add content column to posts table

Revision ID: 8cc792f35e08
Revises: 403a67278de7
Create Date: 2021-11-29 01:38:53.090834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cc792f35e08'
down_revision = '403a67278de7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
