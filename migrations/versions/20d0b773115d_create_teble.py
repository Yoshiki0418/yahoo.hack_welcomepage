"""create Teble

Revision ID: 20d0b773115d
Revises: 
Create Date: 2024-02-18 18:47:57.645799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20d0b773115d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('email')
    )
    op.create_table('closet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_uid', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('size', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('purchase_date', sa.DateTime(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('follower',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('follower_uid', sa.Integer(), nullable=False),
    sa.Column('followed_uid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_uid'], ['user.uid'], ),
    sa.ForeignKeyConstraint(['follower_uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('style',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_uid', sa.Integer(), nullable=True),
    sa.Column('closet_id', sa.Integer(), nullable=True),
    sa.Column('style', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['closet_id'], ['closet.id'], ),
    sa.ForeignKeyConstraint(['user_uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('style')
    op.drop_table('follower')
    op.drop_table('closet')
    op.drop_table('user')
    # ### end Alembic commands ###