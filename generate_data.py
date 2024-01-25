from faker import Faker

class GenerateData:

    def generate_list_dict_data(self, count = 5):
        fake = Faker()

        registers = []
        
        for _ in range(count):
            type = fake.random_element(["Receita", "Despesa", "Investimento"])
            value = fake.random_number(digits=3)
            date = fake.date()

            if(type.lower() == "despesa"):
                value = -abs(value)

            register = {
                "created_date": date,
                "modified_date": date,
                "type": type,
                "value": value,
            }

            registers.append(register)

        return registers

        
            