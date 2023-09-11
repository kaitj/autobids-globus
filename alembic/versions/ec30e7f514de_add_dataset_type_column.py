"""Add dataset type column

Revision ID: ec30e7f514de
Revises: 87575c790c2d
Create Date: 2023-09-07 16:19:04.000382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ec30e7f514de"
down_revision = "87575c790c2d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    dataset_type = sa.Enum(
        "SOURCE_DATA", "RAW_DATA", "DERIVED_DATA", name="datasettype"
    )
    dataset_type.create(op.get_bind())
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "guest_collection",
        sa.Column(
            "dataset_type",
            dataset_type,
            nullable=False,
            server_default="RAW_DATA",
        ),
    )
    op.drop_constraint(
        "guest_collection_study_id_key", "guest_collection", type_="unique"
    )
    op.create_unique_constraint(
        "uq_guest_collection_study_id_dataset_type",
        "guest_collection",
        ["study_id", "dataset_type"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "uq_guest_collection_study_id_dataset_type", "guest_collection", type_="unique"
    )
    op.create_unique_constraint(
        "guest_collection_study_id_key", "guest_collection", ["study_id"]
    )
    op.drop_column("guest_collection", "dataset_type")
    # ### end Alembic commands ###
    dataset_type = sa.Enum(
        "SOURCE_DATA", "RAW_DATA", "DERIVED_DATA", name="datasettype"
    )
    dataset_type.drop(op.get_bind())
