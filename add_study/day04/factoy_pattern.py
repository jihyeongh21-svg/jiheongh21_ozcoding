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
        

    def create_thumnail(self):
       

    def metadata(self):
     

    def create_url(self):
      

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



