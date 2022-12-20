import os 
import yaml
import json



# ------------ Manager (Model objects handler) ------------ #
class BaseManager:

    def __init__(self, model_class):
        self.model_class = model_class

    def select(self, *field_names):

        pass

    def bulk_insert(self, rows: list):
        pass

    def update(self, new_data: dict):
        pass

    def delete(self):
        pass

# ----------------------- Model ----------------------- #
class MetaModel(type):
    manager_class = BaseManager

    def _get_manager(cls):
        return cls.manager_class(model_class=cls)

    @property
    def objects(cls):
        return cls._get_manager()


class BaseModel(metaclass=MetaModel):
    directory_path = ""


        

class YamlDB:
    def __init__(self, path):
        self.data = {}
        self.path = path
        self.config = load_yaml(self.path+"config.yaml")
        self.load_data()

    def load_data(self):
        for filename in os.listdir(self.path):
            f = os.path.join(self.path, filename)
            if os.path.isdir(f):
                items = []
                for filenamen in os.listdir(f):
                    nf = os.path.join(f, filenamen)
                    if os.path.isfile(nf):
                        # load file 
                        items.append(load_yaml(nf))
                self.data[filename] = items

    def get(self,table,query_data = {}):
        searchType = "multi"
        if isinstance(query_data, str):
            searchType = "single"

        found = []
        for item in self.data[table]:
            match = True
            if searchType == "single":
                if query_data == item["name"]:
                    found.append(item)
            else:
                for key, value in item.items():
                    if key in query_data and item[key] != query_data[key]:
                        match = False
                if match: 
                    found.append(item)

        if searchType == "single":
            result =  found[0]
        else:
            result =  found
        return result

    # dump data
    def dump(self):
        return self.data


def load_yaml(file):
    with open(file, "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return data