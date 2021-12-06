from base.modelo import Modelo


class Profissao(Modelo):
    Tabela = "Profissoes"

    def __init__(self, id=None):
        super().__init__(self.Tabela)
        self.id = id
        if id:
            dado = self.obter_por_id(id)
            if dado:
                self.profissao = dado["profissao"]
            else:
                self.id = None
                self.profissao = None
        else:
            self.profissao = None

    def salvar(self):
        try:
            if self.id:
                instrucao = """UPDATE {tabela} SET profissao=%s
                    WHERE id=%s""".format(tabela=self.Tabela)
                self.obter_cursor().execute(instrucao, [
                    self.profissao,
                    self.id])
            else:
                instrucao = """INSERT INTO {tabela} (profissao)
                    VALUES (%s)""".format(tabela=self.Tabela)
                self.obter_cursor().execute(instrucao, [self.profissao])
                self.id = self.obter_cursor().lastrowid
            return True
        except Exception as e:
            print("Ocorreu um erro ao executar: ",
                  self.obter_cursor()._last_executed)
            print(e)
            return False

    def excluir(self):
        if self.id:
            self.excluir_por_id(self.id)
            return True
        else:
            print(f"Não é possível excluir {self.id}")
            return False

    def obter_por_nome(self, nome):
        try:
            instrucao = """SELECT * FROM {tabela}
                WHERE nome LIKE %s""".format(tabela=self.Tabela)
            self.obter_cursor().execute(instrucao, nome)
            resultado = self.obter_cursor().fetchone()
            return resultado
        except Exception as e:
            print("Ocorreu um erro ao executar: ",
                  self.obter_cursor()._last_executed)
            print(e)
            return None
