"""empty message

Revision ID: b8455fd35efa
Revises: 
Create Date: 2019-08-03 13:21:48.046784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8455fd35efa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('video_url', sa.String(length=128), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('duration', sa.String(length=128), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('thumbnail', sa.String(length=128), nullable=True),
    sa.Column('image', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('videos')
    # ### end Alembic commands ###