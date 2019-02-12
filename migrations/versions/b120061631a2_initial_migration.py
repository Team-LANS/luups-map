"""Initial migration

Revision ID: b120061631a2
Revises: 
Create Date: 2019-02-11 23:53:09.970873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b120061631a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('homepage', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('opening_hours', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_venue', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=256), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id_venue'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voucher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_venue', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['id_venue'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voucher_tag',
    sa.Column('id_voucher', sa.Integer(), nullable=False),
    sa.Column('tag', sa.Enum('BREAKFAST', 'MAIN_COURSE', 'SNACK', 'PASTRIES', 'ICE_CREAM', 'COFFEE', 'ALCOHOL', 'EVENT', 'TICKET', 'GUIDED_TOUR', 'WORKSHOP', 'SHOPPING', 'FREE_GIFT', 'COMBINATION', 'SEASONAL', name='tag'), nullable=False),
    sa.ForeignKeyConstraint(['id_voucher'], ['voucher.id'], ),
    sa.PrimaryKeyConstraint('id_voucher', 'tag')
    )
    op.create_table('voucher_type',
    sa.Column('id_voucher', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('FOOD', 'DRINK', 'TICKET', name='type'), nullable=False),
    sa.ForeignKeyConstraint(['id_voucher'], ['voucher.id'], ),
    sa.PrimaryKeyConstraint('id_voucher', 'type')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voucher_type')
    op.drop_table('voucher_tag')
    op.drop_table('voucher')
    op.drop_table('location')
    op.drop_table('venue')
    # ### end Alembic commands ###