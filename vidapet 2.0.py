import os
import datetime

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("Pressione Enter para continuar...")

def exibir_menu():
    while True:
        limpar_tela()
        print("----- Sistema Vida Pet -----")
        print("1 - Cadastrar Pets")
        print("2 - Listar Pets")
        print("3 - Remover Pets")
        print("4 - Editar Pets")
        print("5 - Cadastrar Eventos")
        print("6 - Listar Eventos")
        print("7 - Criar Metas")
        print("8 - Verificar Metas")
        print("9 - Sugerir Cuidados")
        print("10 - Sistema de Pontos")
        print("11 - Lojinha de Troca de Pontos") 
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cria_pet()
        elif opcao == '2':
            listar_pets()
        elif opcao == '3':
            remover_pets()
        elif opcao == '4':
            editar_pets()
        elif opcao == '5':
            cadastrar_eventos()
        elif opcao == '6':
            listar_eventos()
        elif opcao == '7':
            cria_metas()
        elif opcao == '8':
            verificar_metas()
        elif opcao == '9':
            cuidados()
        elif opcao == '10':
            sistema_pontos()
        elif opcao == '11':
            lojinha()
        elif opcao == '0':
            sair()
        else:
            print("Opção inválida!")
            pausar()

def ler_dados(nome_arquivo):
    dados = []
    try:
        with open(nome_arquivo, "a+", encoding="utf-8") as arquivo:
            arquivo.seek(0)
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    dados.append(linha.split(","))
    except FileNotFoundError:
        pass
    return dados

def escreve_dados(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for linha in dados:
                arquivo.write(",".join(linha) + "\n")
    except Exception as e:
        print(f"Erro ao escrever no arquivo {nome_arquivo}: {e}")

def calcular_idade(data_nascimento):
    hoje = datetime.date.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

def cria_pet():
    try:
        limpar_tela()
        print("----- Cadastrar Pet -----")
        nome = input("Nome do pet: ").capitalize()
        especie = input("Espécie: ").capitalize()
        raca = input("Raça: ").capitalize()
        data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
        data = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        peso = float(input("Peso (kg): "))
        pets = ler_dados("pets.txt")
        pets.append([nome, especie, raca, str(data), str(peso)])
        escreve_dados("pets.txt", pets)
        print(f"Pet {nome} adicionado com sucesso!")
    except ValueError:
        print("Data inválida! Use o formato AAAA-MM-DD.")
    pausar()

def listar_pets():
    limpar_tela()
    print("----- Lista de Pets -----")
    pets = ler_dados("pets.txt")
    if not pets:
        print("Nenhum pet cadastrado.")
    else:
        for i, pet in enumerate(pets):
            print(f"{i + 1}. Nome: {pet[0]}, Espécie: {pet[1]}, Raça: {pet[2]}, Nascimento: {pet[3]}, Peso: {pet[4]}")
    pausar()

def remover_pets():
    limpar_tela()
    print("----- Remover Pet -----")
    pets = ler_dados("pets.txt")
    listar_pets()
    nome_remover = input("Nome do pet a remover: ").capitalize()
    novo_pets = [pet for pet in pets if pet[0] != nome_remover]
    if len(novo_pets) != len(pets):
        escreve_dados("pets.txt", novo_pets)
        print(f"Pet {nome_remover} removido.")
    else:
        print("Pet não encontrado.")
    pausar()

def editar_pets():
    limpar_tela()
    print("----- Editar Pet -----")
    pets = ler_dados("pets.txt")
    listar_pets()
    nome_editar = input("Nome do pet para editar: ").capitalize()
    for pet in pets:
        if pet[0] == nome_editar:
            pet[0] = input(f"Novo nome ({pet[0]}): ").capitalize() or pet[0]
            pet[1] = input(f"Nova espécie ({pet[1]}): ").capitalize() or pet[1]
            pet[2] = input(f"Nova raça ({pet[2]}): ").capitalize() or pet[2]
            pet[3] = input(f"Nova data de nascimento ({pet[3]}): ") or pet[3]
            pet[4] = input(f"Novo peso ({pet[4]}): ") or pet[4]
            escreve_dados("pets.txt", pets)
            print("Pet editado com sucesso.")
            break
    else:
        print("Pet não encontrado.")
    pausar()

def cadastrar_eventos():
    limpar_tela()
    print("----- Cadastrar Evento -----")
    pets = ler_dados("pets.txt")
    if not pets:
        print("Cadastre um pet primeiro.")
        pausar()
        return
    listar_pets()
    try:
        indice = int(input("Número do pet: ")) - 1
        data = input("Data do evento (DD/MM/AAAA): ")
        tipo = input("Tipo (Vacinação, Consulta, Remédio): ")
        obs = input("Observações: ")
        eventos = ler_dados("eventos.txt")
        eventos.append([pets[indice][0], data, tipo, obs])
        escreve_dados("eventos.txt", eventos)
        print("Evento registrado.")
    except:
        print("Erro ao cadastrar evento.")
    pausar()

def listar_eventos():
    limpar_tela()
    print("----- Eventos -----")
    eventos = ler_dados("eventos.txt")
    if not eventos:
        print("Nenhum evento cadastrado.")
    else:
        for evento in eventos:
            print(f"Pet: {evento[0]}, Data: {evento[1]}, Tipo: {evento[2]}, Obs: {evento[3]}")
    pausar()

def cria_metas():
    limpar_tela()
    print("----- Criar Metas -----")
    pet = input("Nome do pet: ").capitalize()
    meta = input("Descreva a meta (ex: visitar o vet a cada 6 meses): ")
    data_criacao = input("Data de criação (AAAA-MM-DD): ")
    metas = ler_dados("metas.txt")
    metas.append([pet, meta, data_criacao])
    escreve_dados("metas.txt", metas)
    print("Meta adicionada.")
    pausar()

def verificar_metas():
    limpar_tela()
    print("----- Verificar Metas -----")
    metas = ler_dados("metas.txt")
    if not metas:
        print("Nenhuma meta encontrada.")
        pausar()
        return
    nome = input("Nome do pet: ").capitalize()
    encontrou = False
    for i, meta in enumerate(metas):
        if meta[0] == nome:
            print(f"{i+1}. Meta: {meta[1]} | Criada em: {meta[2]}")
            encontrou = True
    if not encontrou:
        print("Nenhuma meta para esse pet.")
    else:
        cumprir = input("Você cumpriu uma dessas metas? [S/N]: ").upper()
        if cumprir == "S":
            adicionar_pontos(nome, 10)
            print(f"{nome} ganhou 10 pontos!")
    pausar()

def cuidados():
    limpar_tela()
    print("----- Sugerir Cuidados -----")
    pets = ler_dados("pets.txt")
    nome = input("Nome do pet: ").capitalize()
    for pet in pets:
        if pet[0] == nome:
            data_nasc = datetime.datetime.strptime(pet[3], "%Y-%m-%d").date()
            idade = calcular_idade(data_nasc)
            peso = float(pet[4])
            especie = pet[1].lower()
            print(f"Cuidados para {nome} ({especie}, {idade} anos, {peso} kg):")
            if especie in ["cachorro", "cão"]:
                if idade < 1:
                    print("- Vacinação frequente e ração para filhote.")
                elif idade < 7:
                    print("- Exercício diário e ração balanceada.")
                else:
                    print("- Check-up semestral e suporte articular.")
                if peso > 25:
                    print("- Cuidado com articulações devido ao peso.")
            elif especie == "gato":
                if idade < 1:
                    print("- Ração para filhote e brinquedos.")
                elif idade < 10:
                    print("- Estímulo físico e janelas com redes.")
                else:
                    print("- Check-up renal anual.")
                if peso > 6:
                    print("- Pode estar acima do peso.")
            else:
                print("Espécie não reconhecida.")
            break
    else:
        print("Pet não encontrado.")
    pausar()

def adicionar_pontos(pet_nome, pontos_ganhos):
    pontos = ler_dados("pontos.txt")
    pontuacoes = {linha[0]: int(linha[1]) for linha in pontos}
    if pet_nome in pontuacoes:
        pontuacoes[pet_nome] += pontos_ganhos
        if pontuacoes[pet_nome] < 0:
            pontuacoes[pet_nome] = 0 
        pontuacoes[pet_nome] = max(pontos_ganhos,0)
    escreve_dados("pontos.txt", [[nome, str(ponto)] for nome, ponto in pontuacoes.items()])

def trocar_pontos(pet_nome, pontos):
    descontos = {
        "10": "Desconto de 10% em serviços",
        "20": "Desconto de 20% em produtos",
        "50": "Brinde de um brinquedo para o pet",
        "100": "Desconto de 50% em serviços"
    }

    print("----- Trocar Pontos -----")
    print("Descontos e prêmios disponíveis:")
    for ponto, premio in descontos.items():
        print(f"{ponto} pontos: {premio}")

    escolha = input("Digite a quantidade de pontos que deseja trocar: ")
    
    if escolha in descontos and pontos >= int(escolha):
        pontos -= int(escolha)
        adicionar_pontos(pet_nome, -int(escolha))  
        print(f"Você trocou {escolha} pontos por {descontos[escolha]}!")
        print(f"Pontos restantes de {pet_nome}: {pontos}")
    else:
        print("Pontos insuficientes ou opção inválida.")
    
    pausar()

def sistema_pontos():
    limpar_tela()
    print("----- Sistema de Pontos -----")
    pontos = ler_dados("pontos.txt")
    if not pontos:
        print("Nenhum ponto registrado ainda.")
        pausar()
        return
    for pet in pontos:
        print(f"Pet: {pet[0]} - Pontos: {pet[1]}")
    pausar()

def lojinha():
    limpar_tela()
    print("----- Lojinha de Troca de Pontos -----")
    pontos = ler_dados("pontos.txt")
    if not pontos:
        print("Nenhum ponto registrado. Cadastre um pet e acumule pontos antes de usar a lojinha.")
        pausar()
        return
    nome_pet = input("Digite o nome do pet para acessar a lojinha: ").capitalize()
    for pet in pontos:
        if pet[0] == nome_pet:
            pontos_pet = int(pet[1])
            print(f"{nome_pet} possui {pontos_pet} pontos.")
            trocar_pontos(nome_pet, pontos_pet)
            break
    else:
        print(f"O pet {nome_pet} não está cadastrado.")
        pausar()

def sair():
    print("Obrigado por usar o Vida Pet!")
    exit()

exibir_menu()
