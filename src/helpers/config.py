# Change the import to come from pydantic_settings
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    MONGODB_URL: str
    MONGODB_DATABASE: str
    
    # In Pydantic V2, we use model_config instead of class Config
    model_config = SettingsConfigDict(env_file=".env")

def get_settings():
    return Settings()