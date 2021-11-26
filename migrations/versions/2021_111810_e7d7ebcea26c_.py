"""empty message

Revision ID: e7d7ebcea26c
Revises: b8fd175c084a
Create Date: 2021-11-18 10:35:05.122715

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7d7ebcea26c'
down_revision = 'b8fd175c084a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('disable_import', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'disable_import')
    # ### end Alembic commands ###