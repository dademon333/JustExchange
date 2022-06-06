"""Add profile photos

Revision ID: f68716778878
Revises: 673426e50378
Create Date: 2022-05-28 23:39:17.098834

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'f68716778878'
down_revision = '673426e50378'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'profile_photos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('media_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(('media_id',), ['media.id'], name=op.f('fk_profile_photos_media_id_media'), onupdate='CASCADE', ondelete='CASCADE'),
        sa.ForeignKeyConstraint(('owner_id',), ['users.id'], name=op.f('fk_profile_photos_owner_id_users'), onupdate='CASCADE', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_profile_photos'))
    )
    op.create_index(op.f('ix_profile_photos_owner_id'), 'profile_photos', ['owner_id'], unique=False)
    op.create_index(op.f('ix_profile_photos_media_id'), 'profile_photos', ['media_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_profile_photos_media_id'), table_name='profile_photos')
    op.drop_index(op.f('ix_profile_photos_owner_id'), table_name='profile_photos')
    op.drop_table('profile_photos')
    # ### end Alembic commands ###
