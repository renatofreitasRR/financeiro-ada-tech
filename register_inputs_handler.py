from faker import Faker
from register_handler import RegisterHandler

class RegisterInputHandler:

    def create_inputs(self):
        fake = Faker()

        type = self.get_type()
        value = self.__get_value()
        date = fake.date()

        if(type.lower() == "despesa"):
            value = -abs(value)

        return {
            "type": type,
            "value": value,
            "created_date": date,
            "modified_date": date
        }

    def update_inputs(self):
        is_valid, register = self.get_by_id_input()

        if(is_valid == True):
            old_value = register["value"]
            old_type = register["type"]
            created_date = register["created_date"]

            print(f"Alterando registro do tipo: {old_type}, valor: {old_value} criado em: {created_date}")

            new_value = self.__get_value()
            print(f"Alterando valor de {old_value} para {new_value}")

            new_type = self.get_type()
            print(f"Alterando tipo de {old_type} para {new_type}")

            register["type"] = new_type
            register["value"] = new_value

            return register
        
        return None


    def get_by_id_input(self):
        register_handler = RegisterHandler()
        is_valid = False
        go_back = ""
        register = None

        while is_valid == False and go_back != "voltar":
            register_id = input("Insira o id do registro: ")

            register = register_handler.get_by_id(register_id)

            if(register is not None):
                is_valid = True
            else:
               go_back = input("Registro não encontrado, digite voltar para voltar ao menu anterior ou pressione enter para continuar: ").lower()

        return (is_valid, register)
    
    def delete_inputs(self):
        register_handler = RegisterHandler()
        is_valid = False
        go_back = ""
        register_id = ""
        while is_valid == False and go_back != "voltar":
            register_id = input("Insira o id do registro: ")

            register_exists = register_handler.register_exists(register_id)

            if(register_exists == True):
                is_valid = True
                register_handler.delete_register(register_id)
                print("Registro deletado com sucesso!")
            else:
               go_back = input("Id não encontrado, digite voltar para voltar ao menu anterior ou pressione enter para continuar: ").lower()

    def get_type(self):
        type = ""
        while type.lower() not in ["investimento", "despesa", "receita"]:
            type = input("Insira o tipo de registro: Investimento | Despesa | Receita: ")
        return type

    def __get_value(self):
        is_valid = False
        while is_valid == False:
            value = input("Insira um valor maior que 0 ex: 50.32: ")

            try:
                value = float(value)
                is_valid = True
            except:
                print("Por favor, insira um valor válido")
        
        return value