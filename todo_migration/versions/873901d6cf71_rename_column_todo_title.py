"""rename column todo -> title

Revision ID: 873901d6cf71
Revises: c9c7446eb04d
Create Date: 2019-02-26 23:09:10.333633

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '873901d6cf71'
down_revision = 'c9c7446eb04d'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('title', sa.String(length=255), nullable=True))
    op.drop_column('todos', 'todo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('todo', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('todos', 'title')
    # ### end Alembic commands ###
