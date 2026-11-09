from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESSFULLY = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESSFULLY = "file_upload_successfully"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    PROCESSING_SUCCESSFULLY = "processing_success"
    PROCESSING_FAILED = "processing_failed"
    NO_FILE_TO_PROCESS = "no_file_to_process"
    PROJECT_NOT_FOUND_ERROR = "project_not_found"
    INSERT_INTO_VECTORDB_ERROR = "insert_into_vectordb_error"
    INSERT_INTO_VECTORDB_SUCCESS = "insert_into_vectordb_success"
    VECTORDB_COLLECTION_RETRIEVED = "vectordb_collection_retrieved"
    VECTORDB_SEARCH_ERROR = "vectordb_search_error"
    VECTORDB_SEARCH_SUCCESS = "vectordb_search_success"
    RAG_ANSWER_ERROR = "rag_answer_error"
    RAG_ANSWER_SUCCESS = "rag_answer_success"
