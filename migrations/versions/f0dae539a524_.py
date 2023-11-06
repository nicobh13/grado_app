"""empty message

Revision ID: f0dae539a524
Revises: 012fc38aadb2
Create Date: 2023-11-05 21:58:53.600482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0dae539a524'
down_revision = '012fc38aadb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('estado', sa.String(length=20), nullable=False))
        batch_op.create_foreign_key(None, 'grupos', ['grupo_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('estado')

    # ### end Alembic commands ###
