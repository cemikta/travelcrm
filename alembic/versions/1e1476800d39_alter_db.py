"""alter db

Revision ID: 1e1476800d39
Revises: 3b4755fe841
Create Date: 2014-02-08 16:19:41.490223

"""

# revision identifiers, used by Alembic.
revision = '1e1476800d39'
down_revision = '3b4755fe841'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(
        "fk_resource_id_appointment_header", "appointment_header",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_appointment_header_id_appointment_row", "appointment_row",
        "appointment_header", ["appointment_header_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_employee_id_appointment_row", "appointment_row",
        "employee", ["employee_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_position_id_appointment_row", "appointment_row",
        "position", ["position_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resources_id_attachment", "attachment",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_id_currency", "currency",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_id_employee", "employee",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_attachment_id_employee", "employee",
        "attachment", ["attachment_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_id_position_navigation", "navigation",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_navigation_position_id", "navigation",
        "position", ["position_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_parent_id_navigation", "navigation",
        "navigation", ["parent_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_type_id_permission", "permision",
        "resource_type", ["resource_type_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_position_id_permision", "permision",
        "position", ["position_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_permision_structure_id", "permision",
        "structure", ["structure_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_id_position", "position",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_position_structure_id", "position",
        "structure", ["structure_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_id_resource_log", "resource_log",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_user_id_resource_log", "resource_log",
        "user", ["user_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_id_resource_type", "resource_type",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_type_id_resource", "resource",
        "resource_type", ["resource_type_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_structure_id_resource", "resource",
        "structure", ["structure_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_id_structure", "structure",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_structure_parent_id", "structure",
        "structure", ["parent_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_resource_id_user", "user",
        "resource", ["resource_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(
        "fk_employee_id_user", "user",
        "employee", ["employee_id"], ["id"],
        onupdate='CASCADE', ondelete='CASCADE')