from yorm import BaseManager, BaseModel

class Function(BaseModel):
    manager_class = BaseManager
    directory_path = "/storage/data/functions/"

    