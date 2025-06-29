"""add Department

Revision ID: 174d1a0371e8
Revises: ef6c63f1ddc5
Create Date: 2025-05-26 10:49:56.448185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '174d1a0371e8'
down_revision = 'ef6c63f1ddc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deparment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deparment')
    # ### end Alembic commands ###
