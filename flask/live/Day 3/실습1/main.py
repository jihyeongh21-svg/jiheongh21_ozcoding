from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# 1. Base 클래스 정의
Base = declarative_base()

# 2. User 모델 정의: 사용자 이름을 저장하는 테이블
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"

# 3. 데이터베이스 연결
engine = create_engine("sqlite:///users.db", echo=True)

# 4. 테이블 생성
Base.metadata.create_all(bind=engine)

# 5. 데이터베이스 연결 통로: 세션
SessionLocal = sessionmaker(bind=engine)

############
# 연습
############
def run_single():
    db = SessionLocal()

    # CREATE
    new_user = User(name="OZ_BE")
    db.add(new_user)
    db.commit()
    print("단일 사용자 추가:", new_user)
    
    # READ
    user = db.query(User).first()
    print("단일 사용자 찾음:", user)

    # UPDATE
    if user:
        user.name = "OZ_BE_Updated"
        db.commit()
        print("수정된 단일 사용자:", user)

    # DELETE
    if user:
        db.delete(user)
        db.commit()
        print("단일 사용자 삭제!")

    db.close()


def run_bulk():
    db = SessionLocal()

    # CREATE
    new_users = [User(name="OZ_BE17"), User(name="BE_18"), User(name="BE_19")]
    # for new_user in new_users:
    #     db.add(new_user)
    db.add_all(new_users)
    db.commit()
    print("복수 사용자 추가:", new_users)

    # READ
    ## 조건 조회
    user = db.query(User).filter(User.name == "OZ_BE17").first()
    print("조건조회: ", user)

    ## 패턴 검색
    patterns = db.query(User).filter(User.name.like("BE_%")).all()
    print("패턴 검색: ", patterns)

    # UPDATE
    if patterns:
        for p in patterns:
            p.name = p.name + "_Updated"
        db.commit()
        print("복수 사용자 일괄 수정:", patterns)

    # DELETE
    db.query(User).delete()
    db.commit()
    print("모든 사용자 삭제!!")

    db.close()



if __name__ == "__main__":
    # run_single()
    run_bulk()