import os
import datetime

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para pausar a execução
def pausar():
    input("Pressione enter para continuar.")
    return(exibir_menu)

# Função para exibir o menu
def exibir_menu():

    while True:
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
        print("11- Sistema de pontos")
        print("0- Sair")
        opcao=int(input("Digite a opção que deseja realizar no menu: "))
        if opcao == 1:
            cria_pet()
        elif opcao == 2:
            listar_pets()
        elif opcao == 3:
            remover_pets()   
        elif opcao == 4:
            editar_pets()  
        elif opcao == 5:
            eventos()      
        elif opcao == 6:
            listar_eventos()
        elif opcao == 7:
            cria_metas()
        elif opcao == 8:
            verificar_metas
        elif opcao == 9:
            cuidados() 
        elif opcao == 10:
            estatísticas()   
        elif opcao == 11:
            sistema_pontos() 
        else:
            sair()
                 
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

#Função para criar novas metas
def cria_metas(pets):
    limpar_tela()
    print("-----Criar metas-----")
    metas={}
    atribuir_meta=input("\nQual o pet que você deseja atribuir a meta? ").capitalize()
    pets = ler_dados("pets.txt")
    if atribuir_meta in pets:
        while True:
            try:
                data_meta=input("\nDigite a data de criação da meta(AAAAMMDD): ")
                data=datetime.datetime.strptime(data_meta, "%Y-%m-%d")
                qual_meta=input("Digite a sua meta (sem datas): ")
                comprimento=input("Você deseja realizar uma meta única ou contínua? ").lower()
                if comprimento == "continua" or comprimento == "contínua":
                    loop=input("Digite de quanto em quanto tempo deseja repetir o processo (quantidade-anos ou meses \
                    ou semanas ou dia): ")
                    metas[atribuir_meta]=(f"{qual_meta} a cada {loop[0]} {loop[2:]}, criada em {data_meta}")
                else:
                    unica=input("Digite em quanto tempo você planeja concluir a meta ex(3-meses): ")
                    metas[atribuir_meta]=(f"{qual_meta} em {unica[0]} {unica[2:]}, criada em {data_meta}") 
                pausar()
            except ValueError:
                print("\nNúmero Inválido, digite novamente!")  
    else:
        print(f"O pet {atribuir_meta} não está cadastrado")            

#Consulta das metas
def verificar_metas(metas,data_meta):
    limpar_tela()
    print("-----Verificar metas-----")
    consultar_meta=input("\nDigite o nome do pet que você atribuiu a meta: ")
    if consultar_meta in metas:
        while True:
            try:
                data_atual=int(input("Digite o dia da sua consulta (AAAAMMDD): "))
                data=datetime.datetime.strptime(data_meta, "%Y-%m-%d")
                print(f"Metas de: {consultar_meta}")
                for i in len(metas[consultar_meta]):
                    print(f"{i+1}: {metas[consultar_meta]}")
                selecao=int(input("\nDigite qual meta você deseja interagir: "))
                print(f"{metas[consultar_meta][selecao]}\tTempo passado: \
                \nAno: {int(data_atual[:3]) - int(data_meta[:3])} \n Mês: {int(data_atual[4:6]) - int(data_meta[4:6])}\
                \nDia: {int(data_atual[7:]) - int(data_meta[7:])}")

                cumprindo=input("Você está cumprindo a meta? [S/N]: ").upper()
                if cumprindo == "S":
                    adicionar_pontos(consultar_meta, 10) 
                    print(f"\nMeta cumprida! {consultar_meta} ganhou 10 pontos!")

                    remover=input("Deseja remover a meta? [S/N]: ").upper()
                    if remover == "S":
                        del metas[consultar_meta][selecao]
                        print("\nMeta removida!") 
                pausar()   
            except ValueError:
                print("Número inválido, digite novamente!")
    else:
        print(f"O pet {consultar_meta} não está cadastrado!")

#sistema de adicionar pontos
def adicionar_pontos(pet_nome, pontos_ganhos):
    pontuacoes = {}
    dados = ler_dados("pontos.txt")
    for linha in dados:
        pontuacoes[linha[0]] = int(linha[1])
    
    if pet_nome in pontuacoes:
        pontuacoes[pet_nome] += pontos_ganhos
    else:
        pontuacoes[pet_nome] = pontos_ganhos

    escreve_dados("pontos.txt", [[k, str(v)] for k, v in pontuacoes.items()])

#sistema de pontos
def sistema_pontos():
    limpar_tela()
    print("-----Sistema de Pontos-----")
    pontos = ler_dados("pontos.txt")
    if not pontos:
        print("Nenhum ponto registrado ainda.")
    else:
        for pet in pontos:
            print(f"Pet: {pet[0]} - Pontos: {pet[1]}")
    pausar()

#Define função cuidados
def cuidados():
    limpar_tela()
    print("-----Sugerir Cuidados-----")
    pets = ler_dados("pets.txt") #Verifica se existe algum pet resgistrado
    if not pets:
        print("Não há pets cadastrados.")
        pausar()
        return
    
    listar_pets()
    print("-----Sugerir Cuidados-----")
    pet_cuidados = input("Digite o nome do pet para o qual deseja sugestões de cuidados: ").capitalize()
    pet_encontrado = False


    for pet in pets:
        nome, especie, raca, data_str, peso_str = pet
        if nome == pet_cuidados:
            pet_encontrado = True
            try:
                data_nasc = datetime.datetime.strptime(data_str, "%Y-%m-%d").date()
                idade = calcular_idade(data_nasc)
                peso = float(peso_str)

                print(f"\nCuidados para {nome} ({especie}, {raca}, {idade} anos, {peso} kg):")

                if especie.lower() == "cachorro" or especie.lower() == "cão": #Sugestões para cães baseadas em idade e peso
                    if idade < 1:
                        print("- Visitas frequentes ao veterinário para vacinação.")
                        print("- Alimentação específica para filhotes.")
                        print("- Brinquedos interativos.")
                    elif idade < 7:
                        print("- Exercícios regulares (passeios, brincadeiras).")
                        print("- Ração balanceada.")
                    else:
                        print("- Acompanhamento de possíveis problemas articulares.")
                        print("- Check-ups mais frequentes.")
                    if peso > 25:
                        print("- Cuidado com articulações devido ao peso elevado.")
                elif especie.lower() == "gato": #Sugestões para gatos baseadas em idade e peso
                    if idade < 1:
                        print("- Visitas frequentes ao veterinário para vacinação.")
                        print("- Alimentação específica para filhotes.")
                        print("- Brinquedos interativos.")
                    elif idade < 10:
                        print("- Estímulo físico e mental.")
                        print("- Acesso a áreas seguras para explorar.")
                    else:
                        print("- Monitoramento renal e controle de peso.")
                    if peso > 6:
                        print("- Pode estar acima do peso ideal, considerar dieta especial.")
                else:
                    print("- Espécie não reconhecida, recomenda-se consultar um veterinário especializado.") #Saída caso o pet nao seja de uma especie suportada pelo sistema
            except Exception as e:
                print(f"Erro ao processar o pet {nome}: {e}")
            break

    if not pet_encontrado:
        print(f"Pet {pet_cuidados} não encontrado.")

    pausar()

def sair():
    print("Encerrando sistema, esperamos te ver novamente!")
    exit()

exibir_menu()   

