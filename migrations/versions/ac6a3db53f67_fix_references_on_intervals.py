"""Fix references on intervals

Revision ID: ac6a3db53f67
Revises: 8dfac21ded04
Create Date: 2019-07-06 17:05:27.574809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac6a3db53f67'
down_revision = '8dfac21ded04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('interval', sa.Column('id_location', sa.Integer(), nullable=False))
    op.drop_constraint('interval_id_venue_fkey', 'interval', type_='foreignkey')
    op.create_foreign_key(None, 'interval', 'venue', ['id_location'], ['id'])
    op.drop_column('interval', 'id_venue')
    op.drop_column('location', 'opening_hours')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('opening_hours', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('interval', sa.Column('id_venue', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'interval', type_='foreignkey')
    op.create_foreign_key('interval_id_venue_fkey', 'interval', 'venue', ['id_venue'], ['id'])
    op.drop_column('interval', 'id_location')
    # ### end Alembic commands ###