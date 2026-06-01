from database import Base
from sqlalchemy import Column,Integer, BIGINT, String, Boolean, ForeignKey

class Project(Base):
   __tablename__ = 'project'

   id = Column(Integer, primary_key=True, index=True)
   title = Column(String(280))
   location = Column(String(200))
   start_date = Column(Integer)
   budget = Column(BIGINT)