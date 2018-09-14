from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

from app import Base

class Stuntman(Base):
    __tablename__ = 'stuntment'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Boolean)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref=backref("stuntman", userlist=False))

    def __init__(self, name, active, actor):
        self.name = name
        self.active = active
        self.actor = actor