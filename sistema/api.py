from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

from controladores.controlador_usuario import ControladorUsuario
from controladores.controlador_profissao import ControladorProfissao
from controladores.controlador_cliente import ControladorCliente

app = Flask(__name__)
run_with_ngrok(app)

controladorUsuario = ControladorUsuario()
controladorProfissao = ControladorProfissao()
controladorCliente = ControladorCliente()


@app.route("/profissao", methods=["POST"])
def cadastrar_profissao():
    try:
        dados = request.get_json()
        profissao = dados["profissao"]
        controladorProfissao.cadastrar_profissao(profissao)
        return {"status": "OK", "mensagem": "Cadastrado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar"}


@app.route("/cliente", methods=["POST"])
def cadastrar_cliente():
    try:
        dados = request.get_json()
        nome = dados["nome"]
        cpf = dados["cpf"]
        cidade = dados["cidade"]
        telefone = dados["telefone"]
        profissao = dados["profissao"]
        controladorCliente.cadastrar_cliente(
                    nome,
                    cpf,
                    cidade,
                    telefone,
                    profissao
                )
        return {"status": "OK", "mensagem": "Cadastrado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao cadastrar"}


@app.route("/profissao/<id>", methods=["PUT"])
def atualizar_profissao(id):
    try:
        dados = request.get_json()
        profissao = dados["profissao"]
        controladorProfissao.atualizar_profissao(id, profissao)
        return {"status": "OK", "mensagem": "Atualizado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao atualizar"}


@app.route("/cliente/<id>", methods=["PUT"])
def atualizar_cliente(id):
    try:
        dados = request.get_json()
        nome = dados["nome"]
        cpf = dados["cpf"]
        cidade = dados["cidade"]
        telefone = dados["telefone"]
        profissao = dados["profissao"]
        controladorCliente.cadastrar_cliente(
                    nome,
                    cpf,
                    cidade,
                    telefone,
                    profissao
                )
        return {"status": "OK", "mensagem": "Atualizado com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao atualizar"}


@app.route("/usuario/<id>", methods=["DELETE"])
def excluir_usuario(id):
    try:
        controladorUsuario.excluir_usuario(id)
        return {"status": "OK", "mensagem": "Excluído com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao excluir"}


@app.route("/profissao/<id>", methods=["DELETE"])
def excluir_profissao(id):
    try:
        controladorProfissao.excluir_profissao(id)
        return {"status": "OK", "mensagem": "Excluído com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao excluir"}


@app.route("/cliente/<id>", methods=["DELETE"])
def excluir_cliente(id):
    try:
        controladorCliente.excluir_cliente(id)
        return {"status": "OK", "mensagem": "Excluído com Sucesso"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao excluir"}


@app.route("/login", methods=["POST"])
def verificar_usuario_senha():
    try:
        dados = request.get_json()
        usuario = dados["usuario"]
        senha = dados["senha"]
        if controladorUsuario.verificar_usuario_senha(usuario, senha):
            return {"status": "OK", "mensagem": "Acesso OK!"}
        else:
            return {"status": "ERRO", "mensagem": "Usuário/Senha Inválidos!"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao efetuar o login"}


@app.route("/profissao")
def listar_todos_profissoes():
    try:
        todos = controladorProfissao.buscar_todos_profissoes()
        return jsonify(todos)
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter profissões"}


@app.route("/cliente", methods=["GET"])
def listar_todos_clientes():
    try:
        todos = controladorCliente.buscar_todos_clientes()
        return jsonify(todos)
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter clientes"}


@app.route("/profissao/<id>")
def listar_profissao(id):
    try:
        profissao = controladorProfissao.buscar_profissao_por_id(id)
        if profissao:
            return jsonify(profissao)
        else:
            return {"status": "ERRO", "mensagem": f"Erro ao obter profissão {id}"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter profissão"}


@app.route("/cliente/<id>")
def listar_cliente(id):
    try:
        cliente = controladorCliente.buscar_cliente_por_id(id)
        if cliente:
            return jsonify(cliente)
        else:
            return {"status": "ERRO", "mensagem": f"Erro ao obter cliente {id}"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter cliente"}


@app.route("/cliente-buscar/<nome>")
def listar_cliente_nome(nome):
    try:
        cliente = controladorCliente.buscar_cliente_por_nome(nome)
        if cliente:
            return jsonify(cliente)
        else:
            return {"status": "ERRO", "mensagem": f"Erro ao obter cliente {nome}"}
    except:
        return {"status": "ERRO", "mensagem": "Erro ao obter cliente"}


if __name__ == "__main__":
    app.run(debug=True)
