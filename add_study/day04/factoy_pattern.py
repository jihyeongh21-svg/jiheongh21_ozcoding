from abc import ABC, abstractmethod
class uploadserviecenter(ABC):
    @abstractmethod
    def upload(self):
        pass
    @abstractmethod
    def create_thumnail(self):
        pass
    @abstractmethod
    def metadata(self):
        pass
    @abstractmethod
    def create_url(self):
        pass

class AwsS3(uploadserviecenter):
    def upload(self):
        print("AWS S3에 파일을 업로드합니다.")

    def create_thumnail(self):
        print("AWS Lambda를 사용하여 썸네일을 생성합니다.")

    def metadata(self):
        print("AWS S3 객체 메타데이터를 설정합니다.")

    def create_url(self):
        print("CloudFront URL을 생성합니다.")

class Startup(uploadserviecenter):
    def upload(self):
       

    def create_thumnail(self):
       

    def metadata(self):

    def create_url(self):
       

class Privacy(uploadserviecenter):
    def upload(self):
        

    def create_thumnail(self):

    def metadata(self):
      

    def create_url(self):
      


class UploadFactory(ABC):
    @abstractmethod
    def create_service(self) -> uploadserviecenter:
        pass

    def process_upload(self):
        service = self.create_service()
        service.upload()
        service.create_thumnail()
        service.metadata()
        service.create_url()
        return service



