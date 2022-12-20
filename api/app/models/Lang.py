from yorm import BaseManager, BaseModel
from models.Function import Function
class Lang(BaseModel):
    manager_class = BaseManager
    directory_path = "/storage/data/langs/"

    def functions(self):
        return Function.objects.get(lang=self.name)

    
