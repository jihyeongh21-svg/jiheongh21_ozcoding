from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

#########
# DB 설정
#########
BASE_DIR = os.path.dirname(__file__)
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

DATABASE_URL = f"sqlite:///{os.path.join(INSTANCE_DIR, "todos.db")}"
engine = create_engine(DATABASE_URL, echo=True)
# "sqlite:///instance/todos.db"

SessionLocal = sessionmaker(bind=engine)

##########
# 모델 정의
##########
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)

    def __repr__(self):
        return f"<Todo id={self.id}, task='{self.task}'>"

Base.metadata.create_all(bind=engine)