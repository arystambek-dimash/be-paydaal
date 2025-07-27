from datetime import datetime
from enum import Enum

import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.infrastructure.database import Base


class DealStatus(str, Enum):
    IN_QUEUE = "IN_QUEUE"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"


class DealProduct(Base):
    __tablename__ = "deal_products"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    product_id: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)

    started_price: orm.Mapped[float] = orm.mapped_column(
        sa.Numeric(precision=10, scale=2), nullable=False
    )
    expected_price: orm.Mapped[float] = orm.mapped_column(
        sa.Numeric(precision=10, scale=2), nullable=False
    )
    ended_price: orm.Mapped[float] = orm.mapped_column(
        sa.Numeric(precision=10, scale=2), nullable=True
    )

    start_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, server_default=sa.func.now(), nullable=False
    )
    end_date: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, nullable=True)

    status: orm.Mapped[DealStatus] = orm.mapped_column(
        sa.Enum(DealStatus, name="deal_status"), nullable=False
    )
