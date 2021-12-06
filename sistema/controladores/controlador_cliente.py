from modelos.cliente import Cliente


class ControladorCliente():

    def cadastrar_cliente(self, nome, cpf, cidade, telefone, profissao):
        if nome is None or cpf is None:
            print("Você deve preencher o nome e CPF")
            return False

        novo_cliente = Cliente()
        novo_cliente.nome = nome
        novo_cliente.cpf = cpf
        novo_cliente.cidade = cidade
        novo_cliente.telefone = telefone
        novo_cliente.profissao = profissao
        novo_cliente.salvar()
        pass

    def excluir_cliente(self, id):
        excluir_cliente = Cliente(id)
        excluir_cliente.excluir()
        pass

    def atualizar_cliente(self, id, nome, cpf, cidade, telefone, profissao):
        atualizar_cliente = Cliente(id)
        atualizar_cliente.nome = nome
        atualizar_cliente.cpf = cpf
        atualizar_cliente.cidade = cidade
        atualizar_cliente.telefone = telefone
        atualizar_cliente.profissao = profissao
        atualizar_cliente.salvar()
        pass

    def buscar_cliente_por_nome(self, nome):
        busca_clientes = Cliente()
        return busca_clientes.obter_por_nome(nome)

    def buscar_todos_clientes(self):
        todos_clientes = Cliente()
        return todos_clientes.obter_todos()

    def buscar_cliente_por_id(self, id):
        cliente = Cliente()
        return cliente.obter_por_id(id)
