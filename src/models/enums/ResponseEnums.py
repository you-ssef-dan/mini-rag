from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESSFULLY = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESSFULLY = "file_upload_successfully"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    PROCESSING_SUCCESSFULLY = "processing_success"
    PROCESSING_FAILED = "processing_failed"
