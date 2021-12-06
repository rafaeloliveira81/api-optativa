from controladores.controlador_usuario import ControladorUsuario

def main():
    # # Novo Usuario
    # novo_usuario = Usuario()
    # novo_usuario.usuario = "Teste1"
    # novo_usuario.senha = "Teste1"
    # novo_usuario.salvar()

    # print("novo_usuario.id = "      , novo_usuario.id)
    # print("novo_usuario.usuario = " , novo_usuario.usuario)
    # print("novo_usuario.senha = "   , novo_usuario.senha)

    # # Editando o usuário recem criado
    # novo_usuario.senha = "NovaSenha"
    # novo_usuario.salvar()
    # print("novo_usuario.id = "      , novo_usuario.id)
    # print("novo_usuario.usuario = " , novo_usuario.usuario)
    # print("novo_usuario.senha = "   , novo_usuario.senha)

    # # Editando um usuário existente
    # usuario_teste = Usuario(1)
    # usuario_teste.senha = "SuperSecreta"
    # usuario_teste.salvar()

    # # Excluindo um usuário
    # usuario_invalido = Usuario(10000)
    # usuario_invalido.excluir()

    # excluir_usuario1 = Usuario(1)
    # excluir_usuario1.excluir()

    controladorUsuario = ControladorUsuario()
    controladorUsuario.cadastrar_usuario("wariston", "123456")
    controladorUsuario.atualizar_usuario(1, "wariston", "novasenha")
    controladorUsuario.excluir_usuario(1)
    todos = controladorUsuario.buscar_todos_usuarios()
    print(todos)
    usuario = controladorUsuario.buscar_usuario_por_nome("wariston")
    print(usuario)
    controladorUsuario.verificar_usuario_senha("wariston", "123456")

main()
