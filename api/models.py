from sqlalchemy import (
    TIMESTAMP,
    VARCHAR,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    text,
)
from sqlalchemy.orm import relationship

from database import Base


class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    # owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False) # datatype should match the column of the other table
    # owner = relationship("User")
