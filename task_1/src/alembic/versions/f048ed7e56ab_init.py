"""Init

Revision ID: f048ed7e56ab
Revises: 
Create Date: 2023-05-19 02:59:00.892016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f048ed7e56ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_questions_id'), 'questions', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_questions_id'), table_name='questions')
    op.drop_table('questions')
    # ### end Alembic commands ###
