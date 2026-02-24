from abc import ABC, abstractmethod


####################################
# 추상 제품 정의 (재품 공통)
####################################


class Storage(ABC):
    @abstractmethod
    def save(self, file):
        pass


class ThumbnailProcessor(ABC):
    @abstractmethod
    def create_thumbnail(self, file):
        pass


class MetadataExtractor(ABC):
    @abstractmethod
    def extract(self, file):
        pass


class URLBuilder(ABC):
    @abstractmethod
    def build(self, file):
        pass

####################################
# 고객사별  제품 정의
####################################

# Enterprise (AWS 기반)


class S3Storage(Storage):
    def save(self, file):
        print("Saving file to S3")


class LambdaThumbnailProcessor(ThumbnailProcessor):
    def create_thumbnail(self, file):
        print("Generating thumbnail via AWS Lambda")


class MediaConvertMetadataExtractor(MetadataExtractor):
    def extract(self, file):
        print("Extracting metadata via AWS MediaConvert")


class CloudFrontURLBuilder(URLBuilder):
    def build(self, file):
        print("Building CloudFront signed URL")



# Startup (로컬 기반)

class LocalStorage(Storage):
    def save(self, file):
        print("Saving file to local storage")


class PillowThumbnailProcessor(ThumbnailProcessor):
    def create_thumbnail(self, file):
        print("Generating thumbnail via Pillow")


class FFmpegMetadataExtractor(MetadataExtractor):
    def extract(self, file):
        print("Extracting metadata via FFmpeg")


class StaticURLBuilder(URLBuilder):
    def build(self, file):
        print("Building static URL")

# Privacy

class PrivacyObjectStorage(Storage):
    def save(self, file):
        print("Saving file to private storage")

class InternalSever(ThumbnailProcessor):
    def create_thumbnail(self, file):
        print("Generating thumbnail via internal server")

class InternalAnalys(MetadataExtractor):
    def extract(self, file):
        print("Extracting metadata via internal analyzer")

class TokenBuilder(URLBuilder):
    def build(self, file):
        print("Building token URL")




# Stream pro

class CloudStorage(Storage):
    def save(self, file):
        print("Saving file to Cloud Storage")

class Nanobana(ThumbnailProcessor):
    def create_thumbnail(self, file):
        print("Generating thumbnail via Nanobana")

class Googlevids(MetadataExtractor):
    def extract(self, file):
        print("Extracting metadata via Googlevids")

class AutoURLBuilder(URLBuilder):
    def build(self, file):
        print("Building Auto URL")



####################################
# 추상 팩토리 정의(설계))
####################################


class MediaInfrastructureFactory(ABC):

    @abstractmethod
    def create_storage(self) -> Storage:
        pass

    @abstractmethod
    def create_thumbnail_processor(self) -> ThumbnailProcessor:
        pass

    @abstractmethod
    def create_metadata_extractor(self) -> MetadataExtractor:
        pass

    @abstractmethod
    def create_url_builder(self) -> URLBuilder:
        pass


####################################
#  구체적인 팩토리 정의
####################################

class EnterpriseMediaFactory(MediaInfrastructureFactory):

    def create_storage(self):
        return S3Storage()

    def create_thumbnail_processor(self):
        return LambdaThumbnailProcessor()

    def create_metadata_extractor(self):
        return MediaConvertMetadataExtractor()

    def create_url_builder(self):
        return CloudFrontURLBuilder()


class StartupMediaFactory(MediaInfrastructureFactory):

    def create_storage(self):
        return LocalStorage()

    def create_thumbnail_processor(self):
        return PillowThumbnailProcessor()

    def create_metadata_extractor(self):
        return FFmpegMetadataExtractor()

    def create_url_builder(self):
        return StaticURLBuilder()
    
class PrivacyMediaFactory(MediaInfrastructureFactory):
    def create_storage(self):
        return PrivacyObjectStorage()
    def create_thumbnail_processor(self):
        return InternalSever()
    def create_metadata_extractor(self):
        return InternalAnalys()
    def create_url_builder(self):
        return TokenBuilder()

class StreamingProMediaFactory(MediaInfrastructureFactory):
    def create_storage(self):
        return CloudStorage()
    def create_thumbnail_processor(self):
        return Nanobana()
    def create_metadata_extractor(self):
        return Googlevids()
    def create_url_builder(self):
        return AutoURLBuilder()


####################################
# 클라이언트 (비지니스 로직)
####################################

class UploadService:

    def __init__(self, factory: MediaInfrastructureFactory):
        self.storage = factory.create_storage()
        self.thumbnail = factory.create_thumbnail_processor()
        self.metadata = factory.create_metadata_extractor()
        self.url_builder = factory.create_url_builder()

    def upload(self, file):
        print("\n=== Upload Start ===")
        self.storage.save(file)
        self.thumbnail.create_thumbnail(file)
        self.metadata.extract(file)
        self.url_builder.build(file)
        print("=== Upload Complete ===\n")


# ======================================================
# 실행 예시
# ======================================================

if __name__ == "__main__":

    enterprise_factory = EnterpriseMediaFactory()
    enterprise_service = UploadService(enterprise_factory)
    enterprise_service.upload("enterprise_video.mp4")

    startup_factory = StartupMediaFactory()
    startup_service = UploadService(startup_factory)
    startup_service.upload("startup_image.png")

    privacy_factory = PrivacyMediaFactory()
    privacy_service = UploadService(privacy_factory)
    privacy_service.upload("privacy_video.mp4")

    streaming_pro_factory = StreamingProMediaFactory()
    streaming_pro_service = UploadService(streaming_pro_factory)
    streaming_pro_service.upload("streaming_pro_video.mp4")

