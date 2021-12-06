from modelos.profissao import Profissao


class ControladorProfissao():

    def cadastrar_profissao(self, profissao):
        if profissao is None:
            print("Você deve preencher o nome da profissão")
            return False

        novo_profissao = Profissao()
        novo_profissao.profissao = profissao
        novo_profissao.salvar()
        pass

    def excluir_profissao(self, id):
        excluir_profissao = Profissao(id)
        excluir_profissao.excluir()
        pass

    def atualizar_profissao(self, id, profissao):
        atualizar_profissao = Profissao(id)
        atualizar_profissao.profissao = profissao
        atualizar_profissao.salvar()
        pass

    def buscar_profissao_por_nome(self, nome):
        busca_profissao = Profissao()
        return busca_profissao.obter_por_nome(nome)

    def buscar_todos_profissoes(self):
        todos_profissoes = Profissao()
        return todos_profissoes.obter_todos()

    def buscar_profissao_por_id(self, id):
        profissao = Profissao()
        return profissao.obter_por_id(id)
