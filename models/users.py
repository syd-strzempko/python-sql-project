# import datetime
# from typing import List, Optional
# from sqlalchemy import DateTime
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy.sql import func

# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]
#     addresses: Mapped[List["Address"]] = relationship(back_populates="user")
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
