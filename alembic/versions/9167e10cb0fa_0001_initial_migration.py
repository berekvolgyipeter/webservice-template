"""0001 initial migration

Revision ID: 9167e10cb0fa
Revises: 
Create Date: 2025-03-04 14:40:54.452302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9167e10cb0fa'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drivers',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('team', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name', 'team', name='unique_name_team')
    )
    op.create_table('results',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('grand_prix', sa.String(), nullable=False),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('driver_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.CheckConstraint('position > 0', name='positive_value_check'),
    sa.ForeignKeyConstraint(['driver_name'], ['drivers.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('grand_prix', 'driver_name', name='unique_grand_prix_driver_name'),
    sa.UniqueConstraint('grand_prix', 'position', name='unique_grand_prix_position')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('drivers')
    # ### end Alembic commands ###
