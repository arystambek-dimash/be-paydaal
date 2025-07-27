from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.infrastructure.database import Base


class Query(Base):
    __tablename__ = "queries"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    query: orm.Mapped[str] = orm.mapped_column(sa.Text, nullable=False)
    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, server_default=sa.func.now(), nullable=False
    )
    user_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)

    user = orm.relationship("User", backref="queries")
