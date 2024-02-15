import json

class Settings:
    
    def __init__(self, name, value):
        self.name = name
        self.value = value

## Settings methods ##        
def initialise(settings_file:str):

    settings_collection = []

    with open(settings_file, 'r') as f:
        data = json.load(f)
        for array in data.items():
            for values in array:
                
                print(values)
                # settings_collection.append(Settings(key, value))

    return settings_collection

def get_item_value(settings_collection: list, item_name: str):
    for item in settings_collection:
        if item.name == item_name:
            return item.value

    return None