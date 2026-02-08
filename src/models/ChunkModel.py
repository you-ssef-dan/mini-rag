from .BaseDataModel import BaseDataModel
from .db_schemes import DataChunk
from .enums.DataBaseEnum import DataBaseEnum
from bson import ObjectId
from pymongo import InsertOne

class ChunkModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_CHUNKS_NAME.value]

    async def create_chunk(self, chunk: DataChunk):
        result = await self.collection.insert_one(chunk.dict(by_alias=True, exclude_unset=True))#we use the by_alias to get the _id instead of id and we use the exclude_unset to exclude the fields that are not set (in this case the _id)
        chunk._id = result.inserted_id
        return chunk
    
    async def get_chunk(self, chunk_id: str):
        chunk_data = await self.collection.find_one({
            "_id": ObjectId(chunk_id)
        })
        
        if chunk_data is None:
            return None
        
        return DataChunk(**chunk_data) #the chunk_data is a dict and we used the ** to unpack it and pass it as keyword arguments to the DataChunk constructor
    
    async def insert_many_chunks(self, chunks: list, batch_size: int = 100):
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            operations = [ 
                InsertOne(chunk.dict(by_alias=True, exclude_unset=True)) #we use the by_alias to get the _id instead of id and we use the exclude_unset to exclude the fields that are not set (in this case the _id)
                for chunk in batch
            ]
            await self.collection.bulk_write(operations)
        return len(chunks)
    
    async def delete_chunks_by_project_id(self, project_id: ObjectId):
        result = await self.collection.delete_many({
            "chunk_project_id": project_id
        })
        return result.deleted_count
    