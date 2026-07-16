"""create root directory

Revision ID: 2f34a6d1
Revises: 1c8d91ab
Create Date: 2026-07-11

"""

from uuid import UUID as PyUUID

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

# revision identifiers, used by Alembic.
revision = "2f34a6d1"
down_revision = "1c8d91ab"
branch_labels = None
depends_on = None

ROOT_ID = PyUUID("00000000-0000-0000-0000-000000000001")

directories = sa.table(
    "directories",
    sa.column("id", UUID(as_uuid=True)),
    sa.column("name", sa.String),
    sa.column("parent_id", UUID(as_uuid=True)),
)


def upgrade():
    op.bulk_insert(
        directories,
        [
            {
                "id": ROOT_ID,
                "name": "/",
                "parent_id": None,
            }
        ],
    )


def downgrade():
    op.execute(
        sa.text("DELETE FROM directories WHERE id = :id"),
        {"id": ROOT_ID},
    )