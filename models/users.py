import datetime
from typing import List, Optional
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from extensions import db
from utilities import safe_convert

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    entries: Mapped[List["Entry"]] = relationship(back_populates="user")
    def __repr__(self) -> str:
        return f"<User(id={self.id!r}, name={self.name!r}, no_entries={len(self.entries)})>"
    def to_dict(self, incl_relationship=False):
        if (incl_relationship):
            entries_dict = { 'entries': [e.to_dict() for e in self.entries] }
            return {**entries_dict, **safe_convert(self)}
        return safe_convert(self)