class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, ISBN: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = ISBN
        self.disponivel = disponivel
    
    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

    def informacoes(self):
        print(f'Título do livro: {self.titulo}')
        print(f'Autor do livro: {self.autor}')
        print(f'Ano: {self.ano}')
        print(f'ISBN: {self.isbn}')
        status = 'Disponivel' if self.disponivel else "Emprestado"
        print(f"Status: {status}")

class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')


class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.livros_emprestados = []

    def pegar_livro(self, livro: Livro):
        if len(self.livros_emprestados) >= 3:
            print(f"{self.nome} já tem 3 livros emprestados!")
            return
        
        if not livro.disponivel:
            print(f"O livro '{livro.titulo}' não está disponível!")
            return
        

        livro.emprestar()
        self.livros_emprestados.append(livro)
        print(f"{self.nome} pegou o livro '{livro.titulo}' emprestado!")


    def devolver_livro(self, livro: Livro):
        if livro in self.livros_emprestados:
            livro.devolver()  # Marca o livro como disponível
            self.livros_emprestados.remove(livro)  # Remove da lista do cliente
            print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
        else:
            print(f"{self.nome} não possui o livro '{livro.titulo}'.")

    def listar_livros(self):
        if not self.livros_emprestados:
            print(f"{self.nome} não possui livros emprestados.")
        else:
            print(f"Livros emprestados por {self.nome}:")
            for livro in self.livros_emprestados:
                print(f"- {livro.titulo}")

def painel_simples():
    clientes = []
    livros = []

    while True:
        print("\n=== Painel da Biblioteca ===")
        print("1. Criar um cliente novo")
        print("2. Criar um livro novo")
        print("3. Cliente pegar um livro emprestado")
        print("4. Cliente devolver um livro")
        print("5. Mostrar os livros que o cliente está com")
        print("6. Mostrar status de todos os livros")
        print("0. Sair")

        escolha = input("O que você quer fazer? ")

        if escolha == "1":
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            cliente = Cliente(nome, cpf)
            clientes.append(cliente)
            print(f"Cliente {nome} criado com sucesso.")

        elif escolha == "2":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = int(input("Ano do livro: "))
            isbn = input("ISBN do livro: ")
            livro = Livro(titulo, autor, ano, isbn)
            livros.append(livro)
            print(f"Livro '{titulo}' criado com sucesso.")

        elif escolha == "3":
            if not clientes or not livros:
                print("Crie clientes e livros primeiro.")
                continue

            print("Escolha o cliente:")
            for i, c in enumerate(clientes):
                print(f"{i}: {c.nome}")
            idx_cliente = int(input("Número do cliente: "))

            print("Escolha o livro:")
            for i, l in enumerate(livros):
                status = "Disponível" if l.disponivel else "Emprestado"
                print(f"{i}: {l.titulo} - {status}")
            idx_livro = int(input("Número do livro: "))

            clientes[idx_cliente].pegar_livro(livros[idx_livro])

        elif escolha == "4":
            if not clientes:
                print("Crie um cliente primeiro.")
                continue

            print("Escolha o cliente:")
            for i, c in enumerate(clientes):
                print(f"{i}: {c.nome}")
            idx_cliente = int(input("Número do cliente: "))

            cliente = clientes[idx_cliente]
            if not cliente.livros_emprestados:
                print(f"{cliente.nome} não tem livros para devolver.")
                continue

            print("Escolha o livro para devolver:")
            for i, l in enumerate(cliente.livros_emprestados):
                print(f"{i}: {l.titulo}")
            idx_livro = int(input("Número do livro: "))

            cliente.devolver_livro(cliente.livros_emprestados[idx_livro])

        elif escolha == "5":
            if not clientes:
                print("Crie um cliente primeiro.")
                continue

            for c in clientes:
                c.listar_livros()

        elif escolha == "6":
            if not livros:
                print("Crie alguns livros primeiro.")
                continue

            print("Status dos livros:")
            for l in livros:
                status = "Disponível" if l.disponivel else "Emprestado"
                print(f"- {l.titulo}: {status}")

        elif escolha == "0":
            print("Até mais!")
            break

        else:
            print("Opção inválida, tente novamente.")
painel_simples()
