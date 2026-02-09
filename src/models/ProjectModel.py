from .BaseDataModel import BaseDataModel
from .db_schemes.project import Project
from .enums.DataBaseEnum import DataBaseEnum

class ProjectModel(BaseDataModel):
    def __init__(self, db_client: object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECTS_NAME.value]

    @classmethod
    async def create_instance(cls, db_client: object):
        instance = cls(db_client=db_client)
        await instance.init_collection()
        return instance

    async def init_collection(self):
        all_collections = await self.db_client.list_collection_names()
        if DataBaseEnum.COLLECTION_PROJECTS_NAME.value not in all_collections:
            await self.db_client.create_collection(DataBaseEnum.COLLECTION_PROJECTS_NAME.value)
            #create indexes
            indexes = Project.get_indexes()
            for index in indexes:
                await self.collection.create_index(
                    index["key"],
                    name=index["name"],
                    unique=index["unique"]
                )

    async def create_project(self, project: Project):
        project_dict = project.dict(by_alias=True, exclude_unset=True) #we use the by_alias to get the _id instead of id and we use the exclude_unset to exclude the fields that are not set (in this case the _id)
        result = await self.collection.insert_one(project_dict)
        project._id = result.inserted_id
        return project
    
    async def get_project_or_create_one(self, project_id: str):

        record = await self.collection.find_one({"project_id": project_id}) #the record is a dictionary
        if record is None:
            #create new project
            project = Project(project_id=project_id)
            project = await self.create_project(project)
            return project
        
        return Project(**record) #the record is a dict and we want to return a Project instance, so we use the ** operator to unpack the dictionary and pass it as keyword arguments to the Project constructor.
    
    async def get_all_projects(self, page: int = 1, page_size: int = 10):

        #count total number of documents in the collection
        total_documents = await self.collection.count_documents({})

        #calculate total number of pages
        total_pages = total_documents // page_size
        if total_documents % page_size > 0:
            total_pages += 1

        cursor = self.collection.find().skip((page - 1) * page_size).limit(page_size)
        projects = []
        async for record in cursor:
            projects.append(
                Project(**record)
                )
        return projects, total_pages