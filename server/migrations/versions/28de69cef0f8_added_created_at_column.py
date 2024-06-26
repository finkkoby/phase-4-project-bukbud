"""added created at column

Revision ID: 28de69cef0f8
Revises: 3729cf6f85b9
Create Date: 2024-04-26 11:21:57.158142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28de69cef0f8'
down_revision = '3729cf6f85b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
