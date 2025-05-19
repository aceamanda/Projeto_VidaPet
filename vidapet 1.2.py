import os
import datetime

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para pausar a execução
def pausar():
    input("Pressione enter para continuar.")

# Função para exibir o menu
def exibir_menu():
    limpar_tela() 
    print("-----Sistema Vida Pet-----")
    print("1- Cadastrar pets")
    print("2- Listar Pets")
    print("3- Remover pets")
    print("4- Editar pets")
    print("5- Cadastrar eventos")
    print("6- Listar eventos")
    print("7- Definir metas")
    print("8- Listar metas ")
    print("9- Sugerir cuidados")
    print("10- Estatísticas dos pets") 
    print("0- Sair")
    opção=int(input("Digite a opção que deseja realizar no menu: "))
exibir_menu()   

# Função para ler os dados do arquivo
# Função para ler os dados do arquivo
def ler_dados(nome_arquivo):
    dados = []
    try:
        # Abrindo o arquivo em modo 'a+' (leitura e escrita, cria se não existir)
        with open(nome_arquivo, "a+", encoding="utf-8") as arquivo:
            arquivo.seek(0)  # Posiciona o ponteiro no início do arquivo
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    dados.append(linha.split(","))
    except FileNotFoundError:
        pass
    return dados

# Função para escrever os dados no arquivo
def escreve_dados(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for linha in dados:
                arquivo.write(",".join(linha) +"\n")
    except Exception as e:
        print(f"Erro ao escrever o arquivo {nome_arquivo}: {e}")

# Função para calcular a idade de um pet
def calcular_idade(data_nascimento):
    if data_nascimento:
        hoje = datetime.date.today()
        idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        return idade
    return 0 

# Função para criar um pet
def cria_pet():
    try:
        limpar_tela()
        print("-----Cadastrar Pets-----")
        nome = input("Digite o nome do seu animal: ").capitalize()
        especie = input("Digite a especie do seu animal: ").capitalize()
        raca = input("Digite a raça do seu animal: ").capitalize()
        data_nascimento = input("Digite a data de nascimento de seu animal (AAAA-MM-DD): ")
        data = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        peso = float(input("Digite o peso do seu animal: "))

        pet = {
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "data": data,
        "peso": peso,
        }

        pets = ler_dados("pets.txt")
        pets.append([pet["nome"], pet["especie"], pet["raca"], str(pet["data"]), str(pet["peso"])])
        escreve_dados("pets.txt", pets)
        print(f"Pet {nome} adicionado com sucesso!!")
        pausar()
    except:
            print("Erro na data, escreva dividida por '-' !")
            data_corrigida= data_nascimento.replace(" ","-")

# Função para listar todos os pets
def listar_pets():
    limpar_tela()
    print("-----Lista de pets-----")
    pets = ler_dados("pets.txt")
    if not pets:
        print("Não há pets cadastrados.")  
    else:
        for i, pet in enumerate(pets):
            print(f"{i + 1}. Nome: {pet[0]}, Espécie: {pet[1]}, Raça: {pet[2]}, Data de Nascimento: {pet[3]}, Peso: {pet[4]}")    
    pausar()

# Função para remover um pet
def remover_pets():
    limpar_tela()
    print("-----Remover pets-----")
    pets = ler_dados("pets.txt")
    if not pets:
        print("Não há pets cadastrados para remover!!")
        pausar()
        return

    listar_pets()
    nome_remover = input("Digite o nome do pet que você quer remover: ").capitalize()
    pet_removido = False
    for i in range(len(pets)):
        if pets[i][0] == nome_remover:
            confirmacao = input(f"Tem certeza que deseja remover o pet {nome_remover}? [S/N]: ").upper()
            if confirmacao == 'S':
                del pets[i]
                escreve_dados("pets.txt", pets)
                print(f"O pet {nome_remover} foi removido com sucesso!!")
                pet_removido = True
                break
            else:
                print("Remoção cancelada!")
                break
    if not pet_removido:
        print(f"Pet {nome_remover} não encontrado!")
    pausar()

# Função para editar um pet
def editar_pets():
    limpar_tela()
    print("-----Editar pets-----")
    pets = ler_dados("pets.txt")
    if not pets:
        print("Não há pets cadastrados para editar!!")
        pausar()
        return

    listar_pets()
    nome_editar = input("Digite o nome do pet que você deseja editar: ").capitalize()
    pet_editado = False
    for pet in pets:
        if pet[0] == nome_editar:
            print("--- Novas informações do pet ---")
            pet[0] = input(f"Novo nome (atual: {pet[0]}): ").capitalize() or pet[0]
            pet[1] = input(f"Nova espécie (atual: {pet[1]}): ").capitalize() or pet[1]
            pet[2] = input(f"Nova raça (atual: {pet[2]}): ").capitalize() or pet[2]
            pet[3] = input(f"Nova data de nascimento (atual: {pet[3]}): ") or pet[3]
            pet[4] = input(f"Novo peso (atual: {pet[4]}): ") or pet[4]
            escreve_dados("pets.txt", pets)
            print(f"Pet {nome_editar} editado com sucesso!")
            pet_editado = True
            break
    if not pet_editado:
        print(f"Pet {nome_editar} não encontrado.")
    pausar()

# Função para cadastrar eventos
def eventos():
    limpar_tela()
    print("-----Eventos-----")
    eventos = ler_dados("eventos.txt")
    if not eventos:
        print("Não há eventos cadastrados.")
    else:
        for evento in eventos:
            print(f"Pet: {evento[0]}, Data: {evento[1]}, Tipo: {evento[2]}, Obs: {evento[3]}")  
    pausar()

# Chama a função para cadastrar um pet ao iniciar o programa
if opcao == 1 :
    cria_pet()

elif opcao == 2: 
    listar_pets()