#trabalho oficial - redivo
nomes = []
especies = []
idades = []
vacinados = []

def cadastrar_pets():
    while True:
        nome = input("Nome do pet (somente letras): ").strip()
        if nome.isalpha():
            break
        else:
            print("Nome inválido. Digite apenas letras, sem espaços ou números.")

    while True:
        especie = input("Espécie do pet (somente letras): ").strip()
        if especie.isalpha():
            break
        else:
            print("Espécie inválida. Digite apenas letras, sem espaços ou números.")

    try:
        idade = int(input("Idade do pet (0 a 20): ").strip())
        if 0 <= idade <= 20:
            pass
        else:
            print("Idade inválida. Digite um número entre 0 e 20.")
            return
    except ValueError:
        print("Idade inválida. Digite um número inteiro.")
        return

    nomes.append(nome)
    especies.append(especie)
    idades.append(idade)
    vacinados.append(False)
    print("Pet cadastrado com sucesso!")

def listar_pets():
    if not nomes:
        print("Nenhum pet cadastrado.")
        return
    print("\nLista de pets:")
    for i in range(len(nomes)):
        status_vacina = "Vacinado" if vacinados[i] else "Não vacinado"
        print(f"{i+1}. Nome: {nomes[i]}, Espécie: {especies[i]}, Idade: {idades[i]} anos, {status_vacina}")

def vacinar_pet():
    listar_pets()
    try:
        i = int(input("Número do pet para vacinar: ")) - 1
        if 0 <= i < len(nomes):
            if vacinados[i]:
                print(f"{nomes[i]} já está vacinado.")
            else:
                vacinados[i] = True
                print(f"{nomes[i]} foi vacinado com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def editar_pets():
    listar_pets()
    try:
        i = int(input("Número do pet para editar: ")) - 1
        if 0 <= i < len(nomes):
            while True:
                print(f"\nEditando '{nomes[i]}':")
                print("1. Editar nome")
                print("2. Editar espécie")
                print("3. Editar idade")
                print("4. Voltar ao menu principal")
                opcao = input("Escolha uma opção: ").strip()

                match opcao:
                    case '1':
                        novo_nome = input("Novo nome (somente letras): ").strip()
                        if novo_nome.isalpha():
                            nomes[i] = novo_nome
                            print("Nome atualizado com sucesso!")
                        else:
                            print("Nome inválido. Digite apenas letras, sem espaços ou números.")

                    case '2':
                        nova_especie = input("Nova espécie (somente letras): ").strip()
                        if nova_especie.isalpha():
                            especies[i] = nova_especie
                            print("Espécie atualizada com sucesso!")
                        else:
                            print("Espécie inválida. Digite apenas letras, sem espaços ou números.")

                    case '3':
                        try:
                            nova_idade = int(input("Nova idade (0 a 20): ").strip())
                            if 0 <= nova_idade <= 20:
                                idades[i] = nova_idade
                                print("Idade atualizada com sucesso!")
                            else:
                                print("Idade inválida. Digite um número entre 0 e 20.")
                        except ValueError:
                            print("Por favor, digite um número inteiro válido.")

                    case '4':
                        print("Voltando ao menu principal...")
                        break

                    case _:
                        print("Opção inválida. Tente novamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def menu():
    while True:
        print("\nMenu do sistema:")
        print("1. Cadastrar pet")
        print("2. Listar pets")
        print("3. Vacinar pet")
        print("4. Editar informações")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()
        print("")

        match opcao:
            case '1':
                cadastrar_pets()
            case '2':
                listar_pets()
            case '3':
                vacinar_pet()
            case '4':
                editar_pets()
            case '5':
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

# Iniciar o sistema
menu()


