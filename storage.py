import json
import os.path
import aiofiles


class DataStorage:

    def __init__(self, filepath=None):
        self.filepath = filepath or "./storage.json"
        self._create_storage()

    def _create_storage(self) -> None:
        if not os.path.exists(self.filepath):
            with open(self.filepath, mode="w") as file:
                file.write(json.dumps({}))

    def write(self, key: str, value) -> None:
        with open(self.filepath, mode="r") as file:
            data = json.loads(file.read())
            data[key] = value
        with open(self.filepath, mode="w") as file:
            file.write(json.dumps(data))

    def read(self, key: str, default:str=None) -> None:
        with open(self.filepath, mode="r") as file:
            return json.loads(file.read()).get(key, default)


app_storage = DataStorage()
