from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

import logging

# 로깅 설정 초기화: 모든 INFO 레벨 로그를 터미널에 출력
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# 데이터베이스 연결
engine = create_engine('sqlite:///users.db',echo=True)
# 데이터베이스 연결 통로 : 세션
sessionlocal = sessionmaker(bind=engine)
# Base 클래스 정의
Base = declarative_base()
# User 모델 정의
class User(Base):
    __tablename__ = 'users'

    id=Column(Integer, primary_key=True, index=True)
    name = Column(String,nullable=False)
    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"


# 테이블 생섳
Base.metadata.create_all(bind=engine)

#################################
#  연습
def run_single():
    db = sessionlocal()
    # CRUD
    # Create
    new_user=User(name ="test1")
    db.add(new_user)
    db.commit()
    print("사용자 추가",new_user.__repr__())

    # Read
    user=db.query(User).first()
    print("사용자 조회",user.__repr__())


    # Update
    if user:
        user.name="test2"
        db.commit()
        print("사용자 수정",user.__repr__())
    
    # Delete
    if user:
        db.delete(user)
        db.commit()
        print("사용자 삭제",user.__repr__())

    
    # final check
    check = db.query(User).all()
    print("사용자 확인",check.__repr__())
    db.close()

def run_many():
    db = sessionlocal()
    # Create
    new_users = [
        User(name="test1"),
        User(name="test2"),
        User(name="test3"),
    ]
    db.add_all(new_users)
    db.commit()
    print("복수사용자 추가",new_users.__repr__())

    # Read filter
    user_filter = db.query(User).filter(User.name=="test3").first()
    print("필터사용자 조회",user_filter.__repr__())

    ## pattern Read
    user_pattern = db.query(User).filter(User.name.like("test%")).all()
    print("패턴사용자 조회",user_pattern.__repr__())

    # Update
    if user_pattern:
        for p in user_pattern:
            p.name += "수정"
        db.commit()
        print("사용자 수정",user_filter.__repr__())

    # Delete
    db.query(User).delete()
    db.commit()
    print("사용자 삭제")
    
    db.close()

if __name__ == "__main__":
    run_many()