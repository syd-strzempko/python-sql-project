import datetime
from typing import List, Optional
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from extensions import db
from utilities import safe_convert

class Entry(db.Model):
    __tablename__ = "entries"
    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    title: Mapped[str]
    lat: Mapped[int] = mapped_column(default=0, nullable=False)
    long: Mapped[int] = mapped_column(default=0, nullable=False)
    verified: Mapped[bool] = mapped_column(default=False, nullable=False)
    # TODO - backref/foreignkey relationship
    user_id = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="entries")
    def __repr__(self) -> str:
        return f"<Entry(id={self.id!r}, title={self.title!r}, lat={self.lat!r}, long={self.long!r}), user={self.user!r}, verified={self.verified!r})>"
    def to_dict(self, incl_relationship=False):
        if (incl_relationship):
            user_dict = { 'user': self.user.to_dict() }
            return {**user_dict, **safe_convert(self)}
        else:
            return safe_convert(self)