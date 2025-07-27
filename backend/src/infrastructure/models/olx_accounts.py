import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.infrastructure.database import Base


class OlxAccount(Base):
    __tablename__ = "olax_accounts"

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)

    user_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )
    email: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)
    password: orm.Mapped[str] = orm.mapped_column(sa.String, nullable=False)

    user = orm.relationship("User", uselist=False, backref="account")
