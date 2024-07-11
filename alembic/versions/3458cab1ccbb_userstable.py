"""UsersTable

Revision ID: 3458cab1ccbb
Revises: 
Create Date: 2024-07-07 19:11:27.284567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3458cab1ccbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", 
                    sa.Column("user_id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
                    sa.Column("name", sa.String(), nullable=False, index=True),
                    sa.Column("email", sa.String(), nullable=False, unique=True, index=True),
                    sa.Column("password", sa.String(),nullable=False),
                    sa.Column("dob", sa.String()),
                    sa.Column("phone_no", sa.String(), index=True)
                    )


def downgrade() -> None:
    op.drop_table("users")
