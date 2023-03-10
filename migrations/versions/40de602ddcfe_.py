"""empty message

Revision ID: 40de602ddcfe
Revises: 651050517c9c
Create Date: 2023-02-28 16:34:19.157533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40de602ddcfe'
down_revision = '651050517c9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Organization', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=256), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Organization', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
