"""empty message

Revision ID: f9d20e8819bf
Revises: 
Create Date: 2022-09-17 13:47:34.673819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9d20e8819bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('banner_url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ads',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('years_playing', sa.Integer(), nullable=False),
    sa.Column('discord', sa.String(length=50), nullable=False),
    sa.Column('week_days', sa.String(length=50), nullable=False),
    sa.Column('hour_start', sa.Integer(), nullable=False),
    sa.Column('hour_end', sa.Integer(), nullable=False),
    sa.Column('use_voice_channel', sa.Boolean(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ads')
    op.drop_table('games')
    # ### end Alembic commands ###
