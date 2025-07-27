import uuid
from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.infrastructure.database import Base


class Product(Base):
    __tablename__ = "products"

    id: orm.Mapped[uuid.UUID] = orm.mapped_column(
        sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    image_url: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String(255), nullable=False)
    url: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    query_id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer, sa.ForeignKey("queries.id", ondelete="CASCADE"), nullable=False
    )
    price: orm.Mapped[float] = orm.mapped_column(
        sa.Numeric(precision=10, scale=2), nullable=False
    )
    address: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=True)

    created_at: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, server_default=sa.func.now(), nullable=False
    )

    query = orm.relationship("Query", backref="products")
