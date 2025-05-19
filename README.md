# Projeto_VidaPet
Programa de cadastro e agenda de pets

Vida Pet - Manual do Usuário
 Descrição:
 Vida Pet é um sistema simples, feito em Python, para ajudar tutores de animais a manterem a
 saúde e rotina dos seus pets sempre em dia. 
Funciona totalmente pelo terminal, sem bibliotecas externas, com dados salvos em arquivos .txt.
 Funcionalidades:
 1. Cadastro de Pets
   - Adicione pets com nome, espécie, raça, data de nascimento e peso.
 2. Edição, Remoção e Listagem de Pets
 3. Registro de Eventos
   - Registre vacinações, consultas veterinárias e aplicação de remédios.
 4. Definição de Metas de Saúde
   - Ex: "Levar ao veterinário a cada 6 meses".
 5. Sistema de Pontos
   - O pet ganha pontos ao cumprir metas.
 6. Sugestões de Cuidados
   - Com base na espécie, idade e peso do pet.
 Como usar:
 Pré-requisitos:- Python 3.x instalado no computador.
 Como rodar:
 1. Baixe o projeto ou clone o repositório:
   git clone https://github.com/SEU_USUARIO/vida-pet
   cd vida-pet
 2. Execute o script:
   python vida_pet.py
 Menu principal:
 1 - Cadastrar Pets
 2 - Listar Pets
 3 - Remover Pets
 4 - Editar Pets
 5 - Cadastrar Eventos
 6 - Listar Eventos
 7 - Criar Metas
 8 - Verificar Metas
 9 - Sugerir Cuidados
 10 - Sistema de Pontos
 0 - Sair
 Arquivos utilizados:- pets.txt -> Lista de pets cadastrados.- eventos.txt -> Histórico de eventos como vacinas e consultas.- metas.txt -> Metas definidas para cada pet.- pontos.txt -> Pontuação de cada pet ao cumprir metas.
 Esses arquivos são criados e atualizados automaticamente.
Formatos exigidos:- Datas: AAAA-MM-DD (ex: 2024-12-01)- Peso: use ponto, não vírgula (ex: 4.5)- Nomes: sensíveis a maiúsculas/minúsculas.
