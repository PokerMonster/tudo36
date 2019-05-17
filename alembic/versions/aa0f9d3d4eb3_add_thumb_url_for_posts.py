"""add thumb url for posts

Revision ID: aa0f9d3d4eb3
Revises: 532f8a02bb75
Create Date: 2019-05-17 21:15:25.407813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa0f9d3d4eb3'
down_revision = '532f8a02bb75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('thumb_url', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'thumb_url')
    # ### end Alembic commands ###