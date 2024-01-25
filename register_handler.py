from file_handler import FileHandler
from datetime import datetime

class RegisterHandler:
    file_content = {}

    def __init__(self):
        file_handler = FileHandler()
        self.file_content = file_handler.get_file()

    def __generate_id(self):
        content = self.file_content
        
        if len(content) == 0: return 1
        
        last_item = content[-1]
        last_id = last_item["id"]
        
        return last_id + 1

    def create_register(self, register):
        file_handler = FileHandler()

        register["id"] = self.__generate_id()
        self.file_content.append(register)

        file_handler.write_file(self.file_content)

    def create_register_range(self, registers):
        file_handler = FileHandler()

        for register in registers:
            register["id"] = self.__generate_id()
            self.file_content.append(register)

        file_handler.write_file(self.file_content)
        
    def update_register(self, register):
        file_handler = FileHandler()
        registers = self.file_content
        for item in registers:
            if (item["id"] == register["id"]):

                item["type"] = register["type"]
                item["value"] = register["value"]

                if(register["type"] == "despesa"):
                    item["value"] = -abs(item["value"])

                print("Informações atualizadas com sucesso!")
                break

        file_handler.write_file(registers)

    def delete_register(self, register_id: str) -> float:
        file_handler = FileHandler()
        content = self.file_content

        filteredList = [register for register in content if str(register["id"]) != register_id]

        file_handler.write_file(filteredList)

    def get_register_groupby_type(self, type: str) -> float:
        registers = self.file_content

        acc =  sum([register["value"] for register in registers if register["type"] == type])

        return acc
    
    def get_register_groupby_years(self, *years) -> float:
        registers = self.file_content

        acc = sum(register["value"] for register in registers if datetime.strptime(register["created_date"], "%Y-%m-%d").year in years)

        return acc
    
    def register_exists(self, register_id: str) -> bool:
        registers = self.file_content

        if(len(registers) == 0):
            return False
        try:
            return any(str(register["id"]) == register_id for register in registers) 
        except:
            return False
        
    def clear_data(self):
        file_handler = FileHandler()
        total_lines = len(self.file_content)
        file_handler.write_file([])

        return total_lines
    
    def get_by_id(self, register_id):
        registers = self.file_content

        for register in registers:
            if(str(register["id"]) == register_id):
                return register

        return None




    