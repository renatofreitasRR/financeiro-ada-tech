from register_handler import RegisterHandler
from file_handler import FileHandler
from generate_data import GenerateData
from register_inputs_handler import RegisterInputHandler
from generate_data import GenerateData
import csv

register_handler = RegisterHandler()
file_handler = FileHandler()
generate_data = GenerateData()
register_input_handler = RegisterInputHandler()
generate_data = GenerateData()



while True:
    try:
        print("\nOpções:")
        print("1. Adicionar")
        print("2. Importar Base CSV")
        print("3. Atualizar")
        print("4. Deletar")
        print("5. Exportar Relatório Final")
        print("6. Atualizar rendimento")
        print("7. Agrupar por ano")
        print("8. Agrupar por tipo")
        print("9. Limpar Base")
        print("10. Gerar base aleatória")
        print("0. Sair do programa")

        opt = int(input("Digite a opção desejada: "))

        if opt == 0:
            print("Saindo do programa.")
            break
        elif opt == 1:
            register = register_input_handler.create_inputs()
            register_handler.create_register(register)
        elif opt == 2:
            print("Você escolheu a opção 2: Importar Base CSV")
            file = open('base.csv', 'r')
            data = csv.reader(file, delimiter=",")
            registers = []

            header = next(data)

            for type, value, created_at, modified_at in data:
                value = float(value)
                if(type.lower() == "despesa"):
                    value = -abs(value)

                register = {
                    "type": type,
                    "value": value,
                    "created_at": created_at,
                    "modified_at": modified_at
                }

                registers.append(register)

            file.close()

            register_handler.create_register_range(registers)
            print("Base importada com sucesso!")

        elif opt == 3:
            updated_register = register_input_handler.update_inputs()
            register_handler.update_register(updated_register)
        elif opt == 4:
            delete_register = register_input_handler.delete_inputs()
        elif opt == 5:
            print("Você escolheu a opção 5: Exportar Relatório Final")
            
        elif opt == 6:
            print("Você escolheu a opção 6: Atualizar Rendimentos")
        elif opt == 7:
            print("Você escolheu a opção 9: Agrupar por ano")

            is_valid = False
            go_back = ""

            while is_valid == False and go_back != "voltar":
                try:
                    years = input("Insira os anos separado por ',' : ")
                    string_years_splited = years.split(",")

                    print("SPLITED", string_years_splited)

                    years = [int(year) for year in string_years_splited]

                    result = register_handler.get_register_groupby_years(*years)

                    print(f"O total dos registros agrupados pelos anos {years} é igual a: {abs(result)}")

                    is_valid = True   
                except:
                    go_back = input("Registro não encontrado, digite voltar para voltar ao menu anterior ou pressione enter para continuar: ").lower()
        elif opt == 8:
            type = register_input_handler.get_type()
            result = register_handler.get_register_groupby_type(type)
            print(f"O total dos registros agrupados por {type} é igual a: {abs(result)}")
        elif opt == 9:
            total_lines = register_handler.clear_data()
            print(f"Os registros foram apagados, {total_lines} linhas afetadas")
        elif opt == 10:
            total = input("Insira a quantidade de valores para inserir: ")

            try:
                total = int(total)
                data = generate_data.generate_list_dict_data(total)
                register_handler.create_register_range(data)
            except:
                print("Valor inválido, 5 dados aleatórios foram gerados")
                data = generate_data.generate_list_dict_data()
                register_handler.create_register_range(data)
           
            print("Dados adicionados com sucesso!")
        else:
            print("Opção inválida. Por favor, escolha novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número.")



