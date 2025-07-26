import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.infrastructure.database import Base


class User(Base):
    __tablename__ = "users"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    email: orm.Mapped[str] = orm.mapped_column(sa.String, unique=True, nullable=False)
    password: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    is_google_authenticated: bool = orm.mapped_column(
        sa.Boolean,
        nullable=True,
        default=False
    )
    is_apple_id_authenticated: bool = orm.mapped_column(
        sa.Boolean,
        nullable=True,
        default=False
    )
