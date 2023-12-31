"""Initial migration.

Revision ID: fe150375ffab
Revises: 
Create Date: 2023-06-29 11:04:27.316632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe150375ffab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('nis', sa.String(length=7), nullable=False),
    sa.Column('kelas', sa.String(length=15), nullable=False),
    sa.Column('cardUid', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nis')
    )
    op.create_table('ro_absen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currentMode', sa.String(length=255), nullable=False),
    sa.Column('availableModes', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('absen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nis', sa.String(length=7), nullable=False),
    sa.Column('tanggal', sa.DateTime(), nullable=False),
    sa.Column('cardUid', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['nis'], ['member.nis'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('absen')
    op.drop_table('ro_absen')
    op.drop_table('member')
    op.drop_table('admin_member')
    # ### end Alembic commands ###
