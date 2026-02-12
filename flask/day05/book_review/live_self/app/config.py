import os

# 1. 현재 파일(config.py)의 절대 경로를 구합니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. 프로젝트 루트의 instance 폴더 경로를 계산합니다. (app 폴더의 상위 폴더)
# os.path.abspath를 써서 경로를 깔끔하게 정리합니다.
INSTANCE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "instance"))

# 3. 폴더가 없으면 미리 생성합니다. (에러 방지 핵심!)
if not os.path.exists(INSTANCE_DIR):
    os.makedirs(INSTANCE_DIR)

# 4. DB 파일의 전체 경로를 만듭니다.
DB_PATH = os.path.join(INSTANCE_DIR, "reviews.db")

class Config:
    """환경 설정"""
    # 5. 위에서 만든 절대 경로(DB_PATH)를 넣어줍니다.
    # f-string을 사용하여 변수를 문자열 안에 넣습니다.
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False