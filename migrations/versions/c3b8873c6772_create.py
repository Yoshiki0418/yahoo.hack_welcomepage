"""create

Revision ID: c3b8873c6772
Revises: 
Create Date: 2024-02-23 14:30:59.856179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3b8873c6772'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('style',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('style_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('style_name')
    )
    op.create_table('user',
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('iconImage', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('email')
    )
    op.create_table('closet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('style_id', sa.Integer(), nullable=True),
    sa.Column('size', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('purchase_date', sa.DateTime(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['style_id'], ['style.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coordinate',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('continue_name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('follower',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('follower_uid', sa.String(length=50), nullable=False),
    sa.Column('followed_uid', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['followed_uid'], ['user.uid'], ),
    sa.ForeignKeyConstraint(['follower_uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_style_link',
    sa.Column('user_id', sa.String(length=50), nullable=False),
    sa.Column('style_id', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['style_id'], ['style.id'], name='fk_user_style_style_id'),
    sa.ForeignKeyConstraint(['user_id'], ['user.uid'], name='fk_user_style_user_id'),
    sa.PrimaryKeyConstraint('user_id', 'style_id')
    )
    op.create_table('coordinate_items',
    sa.Column('coordinate_id', sa.Integer(), nullable=False),
    sa.Column('closet_item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['closet_item_id'], ['closet.id'], ),
    sa.ForeignKeyConstraint(['coordinate_id'], ['coordinate.id'], ),
    sa.PrimaryKeyConstraint('coordinate_id', 'closet_item_id')
    )
    op.create_table('post_closet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=True),
    sa.Column('style_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('brand', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['style_id'], ['style.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_closet')
    op.drop_table('coordinate_items')
    op.drop_table('user_style_link')
    op.drop_table('post')
    op.drop_table('follower')
    op.drop_table('coordinate')
    op.drop_table('closet')
    op.drop_table('user')
    op.drop_table('style')
    # ### end Alembic commands ###