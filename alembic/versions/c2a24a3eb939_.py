"""empty message

Revision ID: c2a24a3eb939
Revises: 4993f4e8fe21
Create Date: 2023-06-22 15:36:28.672794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c2a24a3eb939"
down_revision = "4993f4e8fe21"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "items",
        sa.Column(
            "description2", sa.Text(), nullable=False, server_default="Not provided"
        ),
    )


def downgrade() -> None:
    pass
