from base.modelo import Modelo

class Usuario(Modelo):
    Tabela = "usuarios"

    def __init__(self, id=None):
        super().__init__(self.Tabela);
        # Atributos da tabela 'usuarios'
        self.id = id;
        if id:
            dado = self.obter_por_id(id)
            if dado:
                self.usuario = dado["usuario"];
                self.senha = dado["senha"];
            else:
                self.id = None;
                self.usuario = None;
                self.senha = None;
        else:
            self.usuario = None;
            self.senha = None;

    def salvar(self):
        try:
            if self.id:
                instrucao = "UPDATE {tabela} SET usuario=%s, senha=%s WHERE id=%s".format(tabela = self.Tabela)
                self.obter_cursor().execute(instrucao, [self.usuario, self.senha, self.id])
            else:
                instrucao = "INSERT INTO {tabela} (usuario, senha) VALUES (%s, %s)".format(tabela = self.Tabela)
                self.obter_cursor().execute(instrucao, [self.usuario, self.senha])
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
            instrucao = "SELECT * FROM {tabela} WHERE usuario LIKE %s".format(tabela = self.Tabela)
            self.obter_cursor().execute(instrucao, nome)
            resultado = self.obter_cursor().fetchone()
            return resultado
        except:
            print ("Ocorreu um erro ao executar: ", self.obter_cursor()._last_executed)
            return None
