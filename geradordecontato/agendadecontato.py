import sqlite3

def criar_tabela_contatos(conexao):
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contatos (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        telefone TEXT,
                        email TEXT
                    )''')
    conexao.commit()

def adicionar_contato(conexao, nome, telefone, email):
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)''', (nome, telefone, email))
    conexao.commit()

def remover_contato(conexao, id_contato):
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM contatos WHERE id=?''', (id_contato,))
    conexao.commit()

def atualizar_contato(conexao, id_contato, nome, telefone, email):
    cursor = conexao.cursor()
    cursor.execute('''UPDATE contatos SET nome=?, telefone=?, email=? WHERE id=?''', (nome, telefone, email, id_contato))
    conexao.commit()

def visualizar_contatos(conexao):
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM contatos''')
    contatos = cursor.fetchall()
    print("Lista de Contatos:")
    for contato in contatos:
        print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")

def main():
    conexao = sqlite3.connect('agenda.db')
    criar_tabela_contatos(conexao)

    while True:
        print("\n1. Adicionar contato")
        print("2. Remover contato")
        print("3. Atualizar contato")
        print("4. Visualizar contatos")
        print("5. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_contato(conexao, nome, telefone, email)
            print("Contato adicionado com sucesso!")
        elif escolha == '2':
            id_contato = input("ID do contato a ser removido: ")
            remover_contato(conexao, id_contato)
            print("Contato removido com sucesso!")
        elif escolha == '3':
            id_contato = input("ID do contato a ser atualizado: ")
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")
            atualizar_contato(conexao, id_contato, nome, telefone, email)
            print("Contato atualizado com sucesso!")
        elif escolha == '4':
            visualizar_contatos(conexao)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conexao.close()

if __name__ == "__main__":
    main()
