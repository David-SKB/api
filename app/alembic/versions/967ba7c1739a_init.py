"""init

Revision ID: 967ba7c1739a
Revises: 
Create Date: 2022-11-25 13:49:12.216311

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '967ba7c1739a'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'event',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('event_title', sa.String, nullable=False),
        sa.Column('event_description', sa.String, nullable=True),
        sa.Column('start_date', sa.Date, nullable=False),
        sa.Column('end_date', sa.Date, nullable=True),
        sa.Column('start_time', sa.Time, nullable=True),
        sa.Column('end_time', sa.Time, nullable=True),
        sa.Column('is_full_day_event', sa.Boolean, nullable=False),
        sa.Column('is_reccuring', sa.Boolean, nullable=False),
        sa.Column('created_by', sa.String, nullable=False),
        sa.Column('created_date', sa.DateTime, nullable=False),
        sa.Column('parent_event_id', sa.Integer, sa.ForeignKey("event.id"), nullable=True),
        sa.Column('event_label', sa.String, nullable=True)
    )


def downgrade():
    op.drop_table('event')
