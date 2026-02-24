from abc import ABC, abstractmethod

# 1. Product Interface (서비스 센터 인터페이스)

class UploadServiceCenter(ABC): 
    @abstractmethod
    def upload(self): pass
    
    @abstractmethod
    def create_thumbnail(self): pass 
    
    @abstractmethod
    def metadata(self): pass
    
    @abstractmethod
    def create_url(self): pass


# 2. Concrete Products (구체적인 서비스 구현)

class AwsS3(UploadServiceCenter):
    def upload(self): print("☁️ AWS S3: 파일 업로드 완료")
    def create_thumbnail(self): print("🖼️ AWS Lambda: 썸네일 생성 완료")
    def metadata(self): print("📊 MediaConvert: 메타데이터 추출 완료")
    def create_url(self): print("🔗 CloudFront: Signed URL 생성 완료")

class Startup(UploadServiceCenter):
    def upload(self): print("📁 Local Storage: 파일 저장 완료")
    def create_thumbnail(self): print("🖼️ Pillow: 썸네일 생성 완료")
    def metadata(self): print("📊 FFmpeg: 메타데이터 추출 완료")
    def create_url(self): print("🔗 Static Builder: 일반 URL 생성 완료")

class Privacy(UploadServiceCenter):
    def upload(self): print("🔒 Private Storage: 보안 저장 완료")
    def create_thumbnail(self): print("🖼️ Internal Server: 내부 썸네일 생성 완료")
    def metadata(self): print("📊 Private Analyzer: 보안 메타데이터 추출")
    def create_url(self): print("🔗 Token Builder: 1회용 토큰 URL 생성")


# 3. Creator (공장 추상 클래스)

class UploadFactory(ABC):
    @abstractmethod
    def create_service(self) -> UploadServiceCenter:
        """이것이 바로 '팩토리 메서드'입니다."""
        pass

    def process_upload(self):
        """템플릿 메서드: 서비스 객체를 만들어 일련의 과정을 실행합니다."""
        service = self.create_service()
        print(f"\n--- {service.__class__.__name__} 처리 시작 ---")
        service.upload()
        service.create_thumbnail()
        service.metadata()
        service.create_url()
        return service

# 4. Concrete Creators (구체적인 공장)

class AwsS3Factory(UploadFactory):
    def create_service(self): return AwsS3()

class StartupFactory(UploadFactory):
    def create_service(self): return Startup()

class PrivacyFactory(UploadFactory):
    def create_service(self): return Privacy()


# 실행 결과

if __name__ == "__main__":
    # 1. AWS 공장 가동
    aws_factory = AwsS3Factory()
    aws_factory.process_upload()

    # 2. 보안(Privacy) 공장 가동
    privacy_factory = PrivacyFactory()
    privacy_factory.process_upload()