"""add last few columns to posts table

Revision ID: 839c3858c0a6
Revises: 883bbb8c1fd0
Create Date: 2021-11-29 01:56:16.522465

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '839c3858c0a6'
down_revision = '883bbb8c1fd0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean, nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('polsts', 'published')
    op.drop_column('posts', 'created_at')
    pass
