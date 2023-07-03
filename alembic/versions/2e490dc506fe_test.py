"""test

Revision ID: 2e490dc506fe
Revises: 737269befe73
Create Date: 2023-06-22 16:04:56.984780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e490dc506fe'
down_revision = '737269befe73'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('description2', sa.String(), server_default='Not provided', nullable=False))
    op.alter_column('items', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('items', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('items', 'is_done',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    op.alter_column('items', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_items_description2'), 'items', ['description2'], unique=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'phone',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('users', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('users', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('users', 'is_verified',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.alter_column('users', 'is_verified',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('users', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('users', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('users', 'phone',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('users', 'password',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.drop_index(op.f('ix_items_description2'), table_name='items')
    op.alter_column('items', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('items', 'is_done',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.alter_column('items', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('items', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('items', 'description2')
    # ### end Alembic commands ###
