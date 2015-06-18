"""alter db

Revision ID: 64457af6068
Revises: 26acac2c77cd
Create Date: 2015-06-13 15:21:27.589222

"""

# revision identifiers, used by Alembic.
revision = '64457af6068'
down_revision = '26acac2c77cd'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('apscheduler_jobs')
    op.add_column('income', sa.Column('account_item_id', sa.Integer(), nullable=False))
    op.create_foreign_key('fk_account_item_id_cashflow', 'income', 'account_item', ['account_item_id'], ['id'])
    op.alter_column('subaccount', 'account_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('subaccount', 'account_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('fk_account_item_id_cashflow', 'income', type_='foreignkey')
    op.drop_column('income', 'account_item_id')
    op.create_table('apscheduler_jobs',
    sa.Column('id', sa.VARCHAR(length=191), autoincrement=False, nullable=False),
    sa.Column('next_run_time', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('job_state', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'apscheduler_jobs_pkey')
    )
    ### end Alembic commands ###