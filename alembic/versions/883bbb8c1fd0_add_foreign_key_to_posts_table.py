"""add foreign-key to posts table

Revision ID: 883bbb8c1fd0
Revises: e5ea97cdb08e
Create Date: 2021-11-29 01:52:28.742984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '883bbb8c1fd0'
down_revision = 'e5ea97cdb08e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
