from modelos.usuario import Usuario

class ControladorUsuario():

    def cadastrar_usuario(self, usuario, senha):
        if usuario is None or senha is None:
            print ("Você deve preencher o usuario e senha")
            return False

        novo_usuario = Usuario()
        novo_usuario.usuario = usuario
        novo_usuario.senha = senha
        novo_usuario.salvar()
        pass

    def excluir_usuario(self, id):
        excluir_usuario = Usuario(id)
        excluir_usuario.excluir()
        pass

    def atualizar_usuario(self, id, usuario, senha):
        atualizar_usuario = Usuario(id)
        atualizar_usuario.usuario = usuario
        atualizar_usuario.senha = senha
        atualizar_usuario.salvar()
        pass

    def buscar_usuario_por_nome(self, nome):
        busca_usuarios = Usuario()
        return busca_usuarios.obter_por_nome(nome)
   
    def buscar_todos_usuarios(self):
        todos_usuarios = Usuario()
        return todos_usuarios.obter_todos()

    def buscar_usuario_por_id(self, id):
        usuario = Usuario()
        return usuario.obter_por_id(id)

    def verificar_usuario_senha(self, usuario, senha):
        busca_usuarios = Usuario()
        retorno = busca_usuarios.obter_por_nome(usuario)
        if retorno is None:
            print("Usuário/Senha Inválidos!")
            return False
        else:
            senha_no_banco = retorno["senha"]
            if senha_no_banco == senha:
                print("Usuário/Senha Válidos!")
                return True
            else:
                print("Usuário/Senha Inválidos!")
                return False
        