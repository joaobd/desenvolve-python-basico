import os
import hashlib
import json

# Constantes
USUARIOS_FILE = 'usuarios.txt'
RESERVAS_FILE = 'reservas.txt'
QUADRAS = ['Alexandre Barcelar', 'C3', 'Campê', 'Clávis', 'Faísca', 'Live']

# Funções de utilidade
def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_usuarios():
    if os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, 'r') as file:
            return json.load(file)
    return {}

def salvar_usuarios(usuarios):
    with open(USUARIOS_FILE, 'w') as file:
        json.dump(usuarios, file)

def carregar_reservas():
    if os.path.exists(RESERVAS_FILE):
        with open(RESERVAS_FILE, 'r') as file:
            return json.load(file)
    return []

def salvar_reservas(reservas):
    with open(RESERVAS_FILE, 'w') as file:
        json.dump(reservas, file)

# Funções de gerenciamento de usuários
def criar_usuario(usuarios, nome, senha, grupo):
    if nome in usuarios:
        print("Usuário já existe.")
        return False
    usuarios[nome] = {'senha': criptografar_senha(senha), 'grupo': grupo}
    salvar_usuarios(usuarios)
    return True

def login(usuarios, nome, senha):
    if nome in usuarios and usuarios[nome]['senha'] == criptografar_senha(senha):
        return True
    return False

def editar_usuario(usuarios, nome, novo_nome=None, nova_senha=None, novo_grupo=None):
    if nome not in usuarios:
        print("Usuário não encontrado.")
        return False
    if novo_nome:
        usuarios[novo_nome] = usuarios.pop(nome)
        nome = novo_nome
    if nova_senha:
        usuarios[nome]['senha'] = criptografar_senha(nova_senha)
    if novo_grupo:
        usuarios[nome]['grupo'] = novo_grupo
    salvar_usuarios(usuarios)
    return True

def remover_usuario(usuarios, nome):
    if nome in usuarios:
        del usuarios[nome]
        salvar_usuarios(usuarios)
        return True
    print("Usuário não encontrado.")
    return False

def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for nome, dados in usuarios.items():
            print(f"Nome: {nome}, Grupo: {dados['grupo']}")

# Funções de gerenciamento de reservas
def criar_reserva(reservas, quadra, inicio, fim, responsavel, usuario):
    reserva = {
        'quadra': quadra,
        'inicio': inicio,
        'fim': fim,
        'responsavel': responsavel,
        'usuario': usuario,
        'confirmada': False
    }
    reservas.append(reserva)
    salvar_reservas(reservas)
    return True

def editar_reserva(reservas, indice, quadra=None, inicio=None, fim=None, responsavel=None):
    if 0 <= indice < len(reservas):
        if quadra:
            reservas[indice]['quadra'] = quadra
        if inicio:
            reservas[indice]['inicio'] = inicio
        if fim:
            reservas[indice]['fim'] = fim
        if responsavel:
            reservas[indice]['responsavel'] = responsavel
        salvar_reservas(reservas)
        return True
    print("Reserva não encontrada.")
    return False

def remover_reserva(reservas, indice):
    if 0 <= indice < len(reservas):
        reservas.pop(indice)
        salvar_reservas(reservas)
        return True
    print("Reserva não encontrada.")
    return False

def confirmar_reserva(reservas, indice, confirmar=True):
    if 0 <= indice < len(reservas):
        reservas[indice]['confirmada'] = confirmar
        salvar_reservas(reservas)
        return True
    print("Reserva não encontrada.")
    return False

def listar_reservas(reservas):
    if not reservas:
        print("Nenhuma reserva cadastrada.")
    else:
        for i, reserva in enumerate(reservas):
            print(f"Reserva {i}: Quadra: {reserva['quadra']}, Início: {reserva['inicio']}, Fim: {reserva['fim']}, Responsável: {reserva['responsavel']}, Usuário: {reserva['usuario']}, Confirmada: {reserva['confirmada']}")

# Função principal
def main():
    usuarios = carregar_usuarios()
    reservas = carregar_reservas()
    usuario_logado = None

    if not usuarios:
        print("Nenhum usuário encontrado. Crie o primeiro usuário (Administrador).")
        nome = input("Nome: ")
        senha = input("Senha: ")
        criar_usuario(usuarios, nome, senha, 'Administrador')

    while True:
        if not usuario_logado:
            print("\nLogin")
            nome = input("Nome: ")
            senha = input("Senha: ")
            if login(usuarios, nome, senha):
                usuario_logado = nome
                print(f"Bem-vindo, {nome}!")
            else:
                print("Nome ou senha incorretos.")
                continue

        print("\nMenu Principal")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Reservas")
        print("3. Logout")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            if usuarios[usuario_logado]['grupo'] != 'Administrador':
                print("Acesso negado. Apenas administradores podem gerenciar usuários.")
                continue

            print("\nGerenciar Usuários")
            print("1. Criar Usuário")
            print("2. Editar Usuário")
            print("3. Remover Usuário")
            print("4. Listar Usuários")
            print("5. Voltar")
            sub_opcao = input("Escolha uma opção: ")

            if sub_opcao == '1':
                nome = input("Nome: ")
                senha = input("Senha: ")
                grupo = input("Grupo (Administrador/Operador): ")
                criar_usuario(usuarios, nome, senha, grupo)
            elif sub_opcao == '2':
                nome = input("Nome do usuário a ser editado: ")
                novo_nome = input("Novo nome (deixe em branco para não alterar): ")
                nova_senha = input("Nova senha (deixe em branco para não alterar): ")
                novo_grupo = input("Novo grupo (deixe em branco para não alterar): ")
                editar_usuario(usuarios, nome, novo_nome, nova_senha, novo_grupo)
            elif sub_opcao == '3':
                nome = input("Nome do usuário a ser removido: ")
                remover_usuario(usuarios, nome)
            elif sub_opcao == '4':
                listar_usuarios(usuarios)
            elif sub_opcao == '5':
                continue

        elif opcao == '2':
            print("\nGerenciar Reservas")
            print("1. Criar Reserva")
            print("2. Editar Reserva")
            print("3. Remover Reserva")
            print("4. Confirmar/Cancelar Confirmação de Reserva")
            print("5. Listar Reservas")
            print("6. Voltar")
            sub_opcao = input("Escolha uma opção: ")

            if sub_opcao == '1':
                print("Quadras disponíveis:")
                for quadra in QUADRAS:
                    print(f"- {quadra}")
                quadra = input("Nome da quadra: ")
                inicio = input("Horário de início: ")
                fim = input("Horário de fim: ")
                responsavel = input("Nome do responsável: ")
                criar_reserva(reservas, quadra, inicio, fim, responsavel, usuario_logado)
            elif sub_opcao == '2':
                indice = int(input("Índice da reserva a ser editada: "))
                quadra = input("Novo nome da quadra (deixe em branco para não alterar): ")
                inicio = input("Novo horário de início (deixe em branco para não alterar): ")
                fim = input("Novo horário de fim (deixe em branco para não alterar): ")
                responsavel = input("Novo nome do responsável (deixe em branco para não alterar): ")
                editar_reserva(reservas, indice, quadra, inicio, fim, responsavel)
            elif sub_opcao == '3':
                indice = int(input("Índice da reserva a ser removida: "))
                remover_reserva(reservas, indice)
            elif sub_opcao == '4':
                indice = int(input("Índice da reserva a ser confirmada/cancelada: "))
                confirmar = input("Confirmar reserva? (s/n): ").lower() == 's'
                confirmar_reserva(reservas, indice, confirmar)
            elif sub_opcao == '5':
                listar_reservas(reservas)
            elif sub_opcao == '6':
                continue

        elif opcao == '3':
            print(f"Logout realizado. Até logo, {usuario_logado}!")
            usuario_logado = None

if __name__ == "__main__":
    main()
