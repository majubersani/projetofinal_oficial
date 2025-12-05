import token
from turtle import pd

import pandas as pd
import plotly.express as px
import plotly.io as pio

from flask import Flask, render_template, request, redirect, url_for, session

from flask import Flask, render_template, redirect, url_for, flash, request, session
import requests  # <-- CORRETO

from flask import Flask, render_template, redirect, url_for, session
from rotas import get_consulta_produto

from flask import session, redirect, url_for, render_template

from rotas import (get_consulta_usuario, get_lista_blog, get_lista_produto, get_lista_pedido, get_lista_movimentacao,
                   get_consulta_produto, get_lista_usuario, get_consulta_blog_id, get_consulta_pedido_id,
                   get_consulta_movimentacao_id, post_cadastro_blog, post_cadastro_movimentacao, put_atualizar_produto,
                   put_atualizar_envio, put_atualizar_usuario, post_cadastrar_usuario, post_cadastro_cartao,
                   post_cadastro_envio, post_cadastro_produto, put_atualizar_cartao, post_cadastro_medicamento,
                   get_grafico_mais_vendidos, get_lista_envio, put_atualizar_blog, get_consulta_envio_id)


def verificar_login():
    if not session:
        flash('Você deve estar logado para visualizar esta página', 'error')
        return redirect(url_for('login'))


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def index():
    return render_template("pagina_inicial.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form('email')
        password = request.form('password')
        print(email, password, 'EMAILSENHA')
        usuario = login(email, password)
        print(usuario)
        if 'access_token' in usuario:
            session['token'] = usuario['access_token']
            session['username'] = usuario['nome']
            session['papel'] = usuario['papel']

            if session['papel'] == 'admin':
                flash('Seja bem vind admistrador', 'success')
                return redirect(url_for('usuario'))
            elif session['papel'] == 'usuario':
                flash('Seja bem vind usuario', 'success')
                return redirect(url_for('usuario'))
            else:
                flash('Voce nao ter permissao para o acesso', 'error')
                print(flash)
                return redirect(url_for('login'))
        else:
            if usuario['erro'] == '401':
                flash('verefique o email e a senha', 'error')
            else:
                flash('Email ou senha incorretos', 'error')
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/cadastros')
def cadastro():
    return render_template('cadastros.html')


@app.route('/listas')
def listas():
    return render_template('listas.html')


@app.route('/loja')
def loja():
    return render_template('loja.html')


@app.route('/medicinais')
def medicinais():
    return render_template('medicinais.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/medicinais_ervas')
def medicinais_ervas():
    return render_template('filtrar_med_ervas.html')


@app.route('/medicinais_plantas')
def medicinais_plantas():
    return render_template('filtrar_med_plantas.html')


@app.route('/loja_cocares')
def loja_cocares():
    return render_template('filtrar_loja_cocares.html')


@app.route('/loja_instrumentos')
def loja_instrumentos():
    return render_template('filtrar_loja_instrumentos.html')


@app.route('/loja_potes')
def loja_potes():
    return render_template('filtrar_loja_potes.html')


@app.route('/atualizar/usuario/<int:id>', methods=["POST", "GET"])
def atualizar_usuario(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    try:
        if request.method == "POST":
            # Atualiza os campos do produto
            nome = request.form.get('nome')
            cpf = request.form.get('cpf')
            email = request.form.get('email')
            papel = request.form.get('papel')

            if nome and cpf and email and papel:

                response = put_atualizar_usuario(nome, cpf, email, papel)

                print("mmm", response)
                if 'mensagem' in response:
                    flash("usuario atualizado com sucesso!")
                    return redirect(url_for("lista_usuario"))
                else:
                    flash(response["erro"])
                return redirect(url_for('lista_usuario'))
        usuario = get_consulta_usuario(id)
        return render_template("atualizar_cadastro_clientes.html", usuario=usuario)

    except Exception as e:
        flash(f"Erro ao atualizar: {str(e)}", "erro")
        return render_template("atualizar_cadastro_clientes.html")


@app.route('/atualizar/produto/<int:id>', methods=["POST", "GET"])
def atualizar_produto(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    try:
        if request.method == "POST":
            # Atualiza os campos do produto
            nome_produto = request.form.get('nome_produto')
            dimensao_produto = request.form.get('dimensao_produto')
            preco_produto = request.form.get('preco_produto')
            cor_produto = request.form.get('cor_produto')
            descricao_produto = request.form.get('descricao_produto')

            if nome_produto and dimensao_produto and preco_produto and cor_produto and descricao_produto:

                response = put_atualizar_produto(nome_produto, dimensao_produto, preco_produto, cor_produto,
                                                 descricao_produto, id)
                print("mmm", response)
                if 'mensagem' in response:
                    flash("produto atualizado com sucesso!")
                    return redirect(url_for("lista_produto"))
                else:
                    flash(response["erro"])
                return redirect(url_for('lista_produto'))
        produto = get_consulta_produto(id)
        print(produto)
        return render_template("atualizar_cadastro_produtos.html", produto=produto)
    except Exception as e:
        flash(f"Erro ao atualizar: {str(e)}", "erro")
        return render_template('atualizar_cadastro_produtos.html')

@app.route('/atualizar/blog/<int:id>', methods=["POST", "GET"])
def atualizar_blog(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    try:
        if request.method == "POST":
            # Atualiza os campos do produto
            titulo = request.form.get('titulo')
            data = request.form.get('data')
            comentario = request.form.get('comentario')
            usuario_id = request.form.get('usuario_id')

            if titulo and data and comentario and usuario_id:

                response = put_atualizar_blog(titulo, data, comentario, usuario_id)
                print("mmm", response)
                if 'mensagem' in response:
                    flash("blog atualizado com sucesso!")
                    return redirect(url_for("lista_blog"))
                else:
                    flash(response["erro"])
                return redirect(url_for('lista_blog'))
        blog = get_consulta_blog_id(id)
        return render_template('atualizar_cadastro_blog.html', blog=blog)
    except Exception as e:
        flash(f'erro ao atualizar: {str(e)}', 'erro')
        return render_template('atualizar_cadastro_blog.html')


@app.route('/atualizar/pedido/<int:id>', methods=["POST", "GET"])
def atualizar_pedido(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    try:
        if request.method == "POST":

            usuario_id = request.form.get('usuario_id')
            produto_id = request.form.get('produto_id')
            quantidade = request.form.get('quantidade')
            valor_total = request.form.get('valor_total')
            endereco = request.form.get('endereco')
            vendedor_id = request.form.get('vendedor_id')

            if usuario_id and produto_id and quantidade and valor_total and endereco and vendedor_id:

                response = put_atualizar_produto(usuario_id, produto_id, quantidade, valor_total,
                                                 endereco, vendedor_id)
                print("mmm", response)
                if 'mensagem' in response:
                    flash("pedido atualizado com sucesso!")
                    return redirect(url_for("lista_pedido"))
                else:
                    flash(response["erro"])
                    return redirect(url_for('lista_pedido'))
            pedido = get_consulta_pedido_id(id)
            return render_template('atualizar_pedido.html', pedido=pedido)
    except Exception as e:
        flash(f'erro ao atualizar: {str(e)}', 'erro')
        return render_template('atualizar_pedido.html')


@app.route('/atualizar/movimentacao/<int:id>', methods=["POST", "GET"])
def atualizar_movimentacao(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    try:
        if request.method == "POST":
            # Atualiza os campos do produto
            quantidade = request.form.get('quantidade')
            produto_id = request.form.get('produto_id')
            data = request.form.get('data')
            status = request.form.get('status')
            usuario_id = request.form.get('usuario_id')

            if quantidade and produto_id and data and status and usuario_id:

                response = put_atualizar_produto(quantidade, produto_id, data, status, usuario_id, id, token)
                print("mmm", response)
                if response:
                    flash("movimentacao atualizado com sucesso!")
                    return redirect(url_for("lista_movimentacao"))
                else:
                    flash(response["erro"])
                return  redirect(url_for('lista_movimentacao'))

        movimentacao = get_consulta_movimentacao_id(id)
        return render_template("atualizar_movimentacao.html", movimentacao=movimentacao)
    except Exception as e:
        flash(f"Erro ao atualizar: {str(e)}", "erro")
        print("erro", e)


@app.route("/cadastro/usuario", methods=["GET", "POST"])
def cadastrar_usuario():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        nome = request.form.get("nome")
        CPF = request.form.get("cpf")
        email = request.form.get("email")
        senha = request.form.get("senha")
        papel = request.form.get("papel")

        print('nome', nome)
        print('cpf', CPF)
        print('email', email)
        print('senha', senha)
        print('papel', papel)

        if nome and CPF and email and senha and papel:

            print("antes api")

            response = post_cadastrar_usuario(nome, CPF, email, senha, papel)

            print(response)

            print('passou api')
            if response:
                flash("usuario cadastrado com sucesso!")
                return redirect(url_for("lista_usuario"))
            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    print('erro')
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))
        else:
            print("preencha todos os campos app")
    return render_template("cadastro_cliente.html")


@app.route("/cadastro/cartao", methods=["GET", "POST"])
def cadastro_cartao():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        usuario_id = request.form.get("usuario_id")
        nome_titular = request.form.get("nome_titular")
        numero_cartao = request.form.get("numero_cartao")
        data_validade = request.form.get("data_validade")
        CVV = request.form.get("CVV")

        if  nome_titular and numero_cartao and data_validade and CVV:

            print('antes api')

            response = post_cadastro_cartao(usuario_id, nome_titular, numero_cartao, data_validade, CVV)
            print(response)
            print('passou api')

            if response:
                flash(" dados de cartao cadastrado com sucesso!")

            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    print('erro')
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))
        else:
            print("preencha todos os campos app")

    return render_template("cadastro_cartao_credito.html")


# @app.route("/cadastro/envio", methods=["GET", "POST"])
# def cadastro_envio():
#     if not token:
#         return redirect(url_for("pagina_inicial"))
#     if request.method == "POST":
#         nome_destinatario = request.form.get("nome_destinatario")
#         endereco = request.form.get("endereco")
#         cidade = request.form.get("cidade")
#         estado = request.form.get("estado")
#         CEP = request.form.get("CEP")
#         telefone = request.form.get("telefone")
#         email = request.form.get("email")
#
#         if nome_destinatario and endereco and cidade and estado and CEP and telefone and email:
#
#             response = post_cadastro_envio(nome_destinatario, endereco, cidade, estado, CEP, telefone, email, token)
#
#             if response:
#                 flash(" dados de envio cadastrado com sucesso!")
#                 return redirect(url_for("lista_envio"))
#
#             else:
#                 if "erro" in response:
#                     flash(response["erro"])
#                 else:
#                     flash(response["msg"])
#                 return redirect(url_for("pagina_inicial"))
#
#     return render_template("cadastro_infos_envio.html")

@app.route("/cadastro/envio", methods=["GET", "POST"])
def cadastro_envio():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        usuario_id = request.form.get("usuario_id")
        nome_destinatario = request.form.get("nome_destinatario")
        endereco = request.form.get("endereco")
        cidade = request.form.get("cidade")
        estado = request.form.get("estado")
        CEP = request.form.get("CEP")
        telefone = request.form.get("telefone")
        email = request.form.get("email")

        if usuario_id and nome_destinatario and endereco and cidade and estado and CEP and telefone and email:


            print("antes api")

            response = post_cadastro_envio(
               usuario_id,  nome_destinatario, endereco, cidade, estado, CEP, telefone, email
            )
            print(response)

            if response:
                    flash("Dados de envio cadastrados com sucesso!")
            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    print('erro')
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))
        else:
            print("preencha todos os campos app")

    return render_template("cadastro_infos_envio.html")

@app.route("/cadastro/medicamento", methods=["GET", "POST"])
def cadastro_medicamento():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        nome_produto = request.form.get("nome")
        preco_produto = request.form.get("preco")
        descricao_produto = request.form.get("descricao")
        fabricante = request.form.get("fabricante")
        categoria_produto = request.form.get("categoria")
        dimensao_produto = request.form.get("dimensao")
        peso_produto = request.form.get("peso")
        cor_produto = request.form.get("cor")
        uso = request.form.get("uso")
        parte_utilizada = request.form.get("parte_utilizada")
        forma_uso = request.form.get("forma_uso")
        imagem_url = request.form.get("imagem_url")

        if nome_produto and preco_produto and descricao_produto and fabricante and categoria_produto and dimensao_produto and peso_produto and cor_produto and uso and parte_utilizada and forma_uso and imagem_url:
            print('antes api')
            response = post_cadastro_medicamento(nome_produto, preco_produto, descricao_produto, fabricante,
                                                 categoria_produto, dimensao_produto, peso_produto, cor_produto,
                                                 uso, parte_utilizada, forma_uso, imagem_url)
            print(response)

            if response:
                flash("medicamento cadastrado com sucesso!")
            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    print('erro')
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))
        else:
            print("preencha todos os campos app")


    return render_template("cadastro_medicinais.html")


@app.route("/cadastro/produto", methods=["GET", "POST"])
def cadastro_produto():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        nome_produto = request.form.get("nome")
        preco_produto = request.form.get("preco")
        categoria_produto = request.form.get("categoria")
        descricao_produto = request.form.get("descricao")
        fabricante_produto = request.form.get("fabricante")
        dimensao_produto = request.form.get("dimensao")
        peso_produto = request.form.get("peso")
        cor_produto = request.form.get("cor")
        uso = request.form.get("uso")
        parte_utilizada = request.form.get("parte_utilizada")
        imagem_produto = request.form.get("imagem")

        if (nome_produto and preco_produto and categoria_produto and descricao_produto and fabricante_produto
                and dimensao_produto and peso_produto and cor_produto and uso and parte_utilizada and imagem_produto):

            print("antes api")

            response = post_cadastro_produto(nome_produto, preco_produto, categoria_produto, descricao_produto,
                                             fabricante_produto, dimensao_produto, peso_produto, cor_produto, uso,
                                             parte_utilizada, imagem_produto)
            print(response)

            print("passou api")
            if response:
                flash("produto cadastrado com sucesso!")
                return redirect(url_for("lista_produto"))
            else:
                if "error" in response:
                    flash(response["erro"])
                else:
                    print("erro")
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))
        else:
            print("Preencha todos os campos")

    return render_template("cadastro_produtos.html")


@app.route("/cadastro/blog", methods=["GET", "POST"])
def cadastro_blog():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        usuario_id = request.form.get("usuario_id")
        comentario = request.form.get("comentario")
        titulo = request.form.get("titulo")
        data = request.form.get("data")
        link_video = request.form.get("link_video")

        if usuario_id and comentario and titulo and data and link_video:

            print('antes api')

            response = post_cadastro_blog(usuario_id,comentario, titulo, data, link_video)
            print(response)
            if response:
                flash("blog cadastrado com sucesso!")
            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    print('erro')
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))
        else:
            print("preencha todos os campos app")

    return render_template("cadastro_blog.html")


@app.route("/cadastro/movimentacao", methods=["GET", "POST"])
def cadastro_movimentacao():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        quantidade = request.form.get("quantidade")
        produto_id = request.form.get("produto_id")
        data = request.form.get("data")
        status = request.form.get("status")
        usuario_id = request.form.get("usuario_id")

        if quantidade and produto_id and data and status and usuario_id:

            print('antes api')

            response = post_cadastro_movimentacao(quantidade, produto_id, data, status, usuario_id)

            print(response)

            print("passou api")

            if response:
                flash("movimentacao cadastrado com sucesso!")
                return redirect(url_for("lista_movimentacao"))

            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    print("erro")
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))
        else:
            print("Preencha todos os campos")

    return render_template("movimentacao.html")


# @app.route("/cadastro/pedido", methods=["GET", "POST"])
# def post_cadastro_pedido():
#     if not token:
#         return redirect(url_for("pagina_inicial"))
#     if request.method == "POST":
#         produto_id = request.form.get("produto_id")
#         vendedor_id = request.form.get("vendedor_id")
#         quantidade = request.form.get("quantidade")
#         valor_total = request.form.get("valor_total")
#         endereco = request.form.get("endereco")
#         usuario_id = request.form.get("usuario_id")
#
#         if produto_id and vendedor_id and quantidade and valor_total and endereco and usuario_id:
#
#             response = post_cadastro_pedido( produto_id, vendedor_id, quantidade, valor_total, endereco, usuario_id, token)
#
#             if response:
#                 flash("movimentacao cadastrado com sucesso!")
#                 return redirect(url_for("get_lista_movimentacao"))
#
#             else:
#                 if "erro" in response:
#                     flash(response["erro"])
#                 else:
#                     flash(response["msg"])
#                 return redirect(url_for("pagina_inicial"))
#
#     return render_template("movimentacao.html")

# @app.route("/consulta/usuario/<int:id>")
# def get_consulta_usuario(id):
#     dados = get_consulta_usuario(id)
#     print("Dados recebidos:", dados)
#
#     if "Usuario" in dados:
#         usuario = dados["Usuario"]
#     else:
#         if "erro" in dados:
#             flash(dados["erro"])
#         else:
#             flash("Não foi possível encontrar o usuário.")
#         return redirect(url_for("home"))
#
#     return render_template("consulta_usuario.html", usuario=usuario)

# @app.route("/consulta/produto/<int:id>")
# def consulta_produto(id):
#     dados = get_consulta_produto(id)
#     print("Dados recebidos:", dados)
#
#     if "Produto" in dados:
#         produto = dados["Produto"]
#     else:
#         if "erro" in dados:
#             flash(dados["erro"])
#         else:
#             flash("Não foi possível encontrar o produto.")
#         return redirect(url_for("index"))
#
#     return render_template("detalhes_produtos.html", produto=produto)


# @app.route("/consulta/blog/<int:id>")
# def get_consulta_blog(id):
#     dados = get_consulta_blog_id(id)
#     print("Dados recebidos:", dados)
#
#     if "Blog" in dados:
#         blog = dados["Blog"]
#     else:
#         if "erro" in dados:
#             flash(dados["erro"])
#         else:
#             flash("Não foi possível encontrar o blog.")
#         return redirect(url_for("home"))
#
#     return render_template("consulta_blog.html", blog=blog)

# @app.route("/consulta/pedido/<int:id>")
# def get_consulta_pedido(id):
#     dados = get_consulta_pedido_id(id)
#     print("Dados recebidos:", dados)
#
#     if "Pedido" in dados:
#         pedido = dados["Pedido"]
#     else:
#         if "erro" in dados:
#             flash(dados["erro"])
#         else:
#             flash("Não foi possível encontrar o pedido.")
#         return redirect(url_for("home"))
#
#     return render_template("consulta_pedido.html", pedido=pedido)

# @app.route("/consulta/movimentacao/<int:id>")
# def get_consulta_movimentacao(id):
#     dados = get_consulta_movimentacao_id(id)
#     print("Dados recebidos:", dados)
#
#     if "Movimentacao" in dados:
#         movimentacao = dados["Movimentacao"]
#     else:
#         if "erro" in dados:
#             flash(dados["erro"])
#         else:
#             flash("Não foi possível encontrar a movimentação.")
#         return redirect(url_for("home"))
#
#     return render_template("consulta_movimentacao.html", movimentacao=movimentacao)

@app.route("/lista/usuario")
def lista_usuario():
    dados = get_lista_usuario()
    print("Dados recebidos:", dados)

    if "usuarios" in dados:
        usuarios = dados["usuarios"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar os usuários.")
        return redirect(url_for("index"))

    return render_template("lista_clientes.html", usuarios=usuarios)

@app.route("/lista/envio")
def lista_envio():
    dados = get_lista_envio()
    print("Dados recebidos:", dados)

    if "envio" in dados:
        envios = dados["envio"]
        print(envios)
        return render_template("lista_infos_envio.html", envios=envios)
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar os envios.")
        return redirect(url_for("index"))



@app.route("/lista/produto")
def lista_produto():
    dados = get_lista_produto()
    print("Dados recebidos:", dados)

    if "produtos" in dados:
        produtos = dados["produtos"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar os produtos.")
        return redirect(url_for("index"))

    return render_template("lista_produtos.html", produtos=produtos)


@app.route("/lista/blog")
def lista_blog():
    dados = get_lista_blog()
    print("Dados recebidos:", dados)

    if "blog" in dados:
        blogg = dados["blog"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar os blogs.")
        return redirect(url_for("index"))

    return render_template("lista_blog.html", blogs=blogg)


@app.route("/lista/pedido")
def lista_pedido():
    dados = get_lista_pedido()
    print("Dados recebidos:", dados)

    if "pedidos" in dados:
        pedidos = dados["pedidos"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar os pedidos.")
        return redirect(url_for("index"))

    return render_template("lista_pedidos.html", pedidos=pedidos)


@app.route("/lista/movimentacao")
def lista_movimentacao():
    dados = get_lista_movimentacao()
    print("Dados recebidos:", dados)

    if "movimentacoes" in dados:
        movimentacoes = dados["movimentacoes"]
        return render_template("lista_movimentacao.html", movimentacoes=movimentacoes)
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar as movimentações.")

    return render_template("lista_movimentacao.html")


@app.route('/atualizar/cartao/<int:id>', methods=["POST", "GET"])
def atualizar_cartao(id):
    global response
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        try:
            # Atualiza os campos do produto
            nome_titular = request.form.get('nome_titular')
            numero_cartao = int(request.form.get('numero_cartao'))
            data_validade = request.form.get('data_validade')
            CVV = request.form.get('CVV')

            if nome_titular and numero_cartao and data_validade and CVV:

                response = put_atualizar_cartao(nome_titular, numero_cartao, data_validade, id, token)
                print("mmm", response)
                if response:
                    flash("Cartao atualizado com sucesso!")
                else:
                    flash(response["erro"])
        except Exception as e:
            flash(f"Erro ao atualizar: {str(e)}", "erro")

    dados = response["Cartao"]

    return render_template("atualizar_cadastro_cartao_credito.html", var_cartao=dados)


@app.route('/atualizar/envio/<int:id>', methods=["POST", "GET"])
def atualizar_envio(id):
    if not token:
        return redirect(url_for("pagina_inicial"))

    try:
        if request.method == "POST":

            # Atualiza os campos do produto
            nome_destinatario = request.form.get('nome_destinatario')
            endereco = request.form.get('endereco')
            cidade = request.form.get('cidade')
            estado = request.form.get('estado')
            CEP = request.form.get('CEP')
            telefone = request.form.get('telefone')
            email = request.form.get('email')

            if nome_destinatario and endereco and cidade and estado and CEP and telefone and email:

                response = put_atualizar_envio(nome_destinatario, endereco, cidade, estado, CEP, telefone, email)
                print("mmm", response)
                if 'mensagem' in response:
                    flash("Envio atualizado com sucesso!")
                    return redirect(url_for("lista_envio"))
                else:
                    flash(response["erro"])
                    return redirect(url_for("lista_envio"))

        envio = get_consulta_envio_id(id)
        print("passou")
        return render_template("atualizar_infos_envio.html", envio=envio)

    except Exception as e:
        flash(f"Erro ao atualizar: {str(e)}", "erro")
        print("erro", e)
        return render_template("atualizar_infos_envio.html")
    ###hhhhhh


@app.route('/grafico', methods=['GET'])
def grafico():
    token = session.get('access_token')
    if not token:
        flash("Faça login para acessar o relatório.", "warning")
        return redirect(url_for('login'))

    try:
        # Busca os 5 produtos mais vendidos usando SUA FUNÇÃO
        acessar_vendidos = get_grafico_mais_vendidos(token)
        vendidos = acessar_vendidos.get("produtos_mais_vendidos", [])

        df_vendidos = pd.DataFrame(vendidos) if vendidos else pd.DataFrame(columns=['nome_pedido', 'quantidade_pedido'])
        grafico_vendidos = None

        if not df_vendidos.empty:
            # Agrupa e ordena
            df_vendidos_aggregated = (
                df_vendidos.groupby('nome_pedido', as_index=False)['quantidade_pedido']
                .sum()
                .sort_values(by='quantidade_pedido', ascending=False)
            )

            # Cria gráfico (Plotly)
            fig_vendidos = px.bar(
                df_vendidos_aggregated,
                x="nome_pedido",
                y="quantidade_pedido",
                title="Top 5 Produtos Mais Vendidos",
                labels={"nome_pedido": "Produto", "quantidade_pedido": "Quantidade Vendida"}
            )

            fig_vendidos.update_traces(marker_color='orange')
            fig_vendidos.update_layout(
                template="plotly_dark",
                xaxis={'categoryorder': 'total descending'}
            )

            # Converte para HTML para o template Jinja
            grafico_vendidos = pio.to_html(fig_vendidos, full_html=False, include_plotlyjs="cdn")

        return render_template(
            "grafico.html",
            grafico_vendidos=grafico_vendidos
        )

    except Exception as e:
        flash(f"Erro ao gerar relatório: {str(e)}", "danger")
        return render_template("grafico.html", grafico_vendidos=None)


def iniciar_carrinho():
    if "carrinho" not in session:
        session["carrinho"] = {}

# @app.route("/add_carrinho/<int:produto_id>")
# def add_carrinho(produto_id):
#     iniciar_carrinho()
#
#     db = SessionLocal()
#     produto = db.query(Produto).filter_by(id=produto_id).first()
#
#     if not produto:
#         return redirect(url_for("loja"))
#
#     carrinho = session["carrinho"]
#
#     if str(produto_id) in carrinho:
#         carrinho[str(produto_id)]["quantidade"] += 1
#     else:
#         carrinho[str(produto_id)] = {
#             "nome": produto.nome,
#             "preco": float(produto.preco),
#             "quantidade": 1
#         }
#
#     session.modified = True
#     return redirect(url_for("carrinho"))


@app.route("/carrinho")
def carrinho():
    iniciar_carrinho()
    carrinho = session["carrinho"]

    total = sum(item["preco"] * item["quantidade"] for item in carrinho.values())

    return render_template("carrinho.html", carrinho=carrinho, total_carrinho=total)


@app.route("/remover_item/<int:produto_id>")
def remover_item(produto_id):
    iniciar_carrinho()

    carrinho = session["carrinho"]
    carrinho.pop(str(produto_id), None)

    session.modified = True
    return redirect(url_for("carrinho"))


if __name__ == '__main__':
    app.run(debug=True, port=5008)
