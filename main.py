import token

from flask import Flask, render_template, redirect, url_for, flash, request
from requests import session, utils
from flask import session as login_session

from rotas import (get_consulta_usuario, get_consulta_blog_id, get_consulta_produto, get_consulta_movimentacao_id, get_consulta_pedido_id,
                   get_lista_usuario, get_lista_blog, get_lista_produto, get_lista_pedido, get_lista_movimentacao,put_atualizar_blog, put_atualizar_produto,
                   put_atualizar_pedido, put_atualizar_movimentacao, put_atualizar_usuario, get_consulta_produto, get_lista_usuario, post_cadastrar_usuario, post_cadastro_pedido, post_cadastro_blog, post_cadastro_movimentacao,
                   post_cadastro_medicamento, post_cadastro_produto, post_login,
                   get_lista_usuario, get_consulta_blog_id, get_consulta_pedido_id, get_consulta_movimentacao_id)


def verificar_login():
    if not session:
        flash('Você deve estar logado para visualizar esta página', 'error')
        return redirect(url_for('login'))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form('email')
        password  = request.form('password')
        print(email, password, 'EMAILSENHA')
        usuario = utils.post_login(email, password)
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

@app.route('/atualizar/usuario/<int:id>', methods=["POST", "GET"])
def put_atualizar_usuario(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        try:
            # Atualiza os campos do produto
            nome = request.form.get('nome')
            CPF = request.form.get('cpf')
            email = request.form.get('email')
            papel = request.form.get('papel')

            if nome and CPF and email and papel:

                response = put_atualizar_usuario(nome, CPF, email, papel, id, token)
                print("mmm", response)
                if response:
                    flash("usuario atualizado com sucesso!")
                    return redirect(url_for("get_lista_usuario"))
                else:
                    flash(response["erro"])
        except Exception as e:
            flash(f"Erro ao atualizar: {str(e)}", "erro")

    response = get_consulta_usuario(id, token)

    if not response or "Usuario" not in response:  # evita KeyError
        flash(response.get("erro", response.get("msg", "Não foi possível carregar o usuario.")), "erro")
        return redirect(url_for('get_lista_usuario'))

    dados = response["Usuario"]

    return render_template("atualizar_usuario.html", var_usuario=dados)


@app.route('/atualizar/produto/<int:id>', methods=["POST", "GET"])
def put_atualizar_produto(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        try:
            # Atualiza os campos do produto
            nome_produto = request.form.get('nome_produto')
            dimensao_produto = request.form.get('dimensao_produto')
            preco_produto = request.form.get('preco_produto')
            cor_produto = request.form.get('cor_produto')
            descricao_produto = request.form.get('descricao_produto')

            if nome_produto and dimensao_produto and preco_produto and cor_produto and descricao_produto:

                response = put_atualizar_produto(nome_produto, dimensao_produto, preco_produto,cor_produto,
                                                 descricao_produto, id, token)
                print("mmm", response)
                if response:
                    flash("produto atualizado com sucesso!")
                    return redirect(url_for("get_lista_produto"))
                else:
                    flash(response["erro"])
        except Exception as e:
            flash(f"Erro ao atualizar: {str(e)}", "erro")

    response = get_consulta_produto(id, token)

    if not response or "Produto" not in response:  # evita KeyError
        flash(response.get("erro", response.get("msg", "Não foi possível carregar o produto.")), "erro")
        return redirect(url_for('get_lista_profuto'))

    dados = response["Produto"]

    return render_template("atualizar_produto.html", var_produto=dados)

@app.route('/atualizar/blog/<int:id>', methods=["POST", "GET"])
def put_atualizar_blog(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        try:
            # Atualiza os campos do produto
            titulo = request.form.get('titulo')
            data = request.form.get('data')
            comentario = request.form.get('comentario')
            usuario_id = request.form.get('usuario_id')

            if titulo and data and comentario and usuario_id:

                response = put_atualizar_produto(titulo, data, comentario, usuario_id, id, token)
                print("mmm", response)
                if response:
                    flash("blog atualizado com sucesso!")
                    return redirect(url_for("get_lista_blog"))
                else:
                    flash(response["erro"])
        except Exception as e:
            flash(f"Erro ao atualizar: {str(e)}", "erro")

    response = get_consulta_blog_id(id, token)

    if not response or "Produto" not in response:  # evita KeyError
        flash(response.get("erro", response.get("msg", "Não foi possível carregar o blog.")), "erro")
        return redirect(url_for('get_lista_blog'))

    dados = response["Blog"]

    return render_template("atualizar_blog.html", var_blog=dados)


@app.route('/atualizar/pedido/<int:id>', methods=["POST", "GET"])
def put_atualizar_pedido(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        try:
            # Atualiza os campos do produto
            usuario_id = request.form.get('usuario_id')
            produto_id = request.form.get('produto_id')
            quantidade = request.form.get('quantidade')
            valor_total = request.form.get('valor_total')
            endereco = request.form.get('endereco')
            vendedor_id = request.form.get('vendedor_id')

            if usuario_id and produto_id and quantidade and valor_total and endereco and vendedor_id:

                response = put_atualizar_produto(usuario_id, produto_id, quantidade, valor_total,
                                                 endereco, vendedor_id, id, token)
                print("mmm", response)
                if response:
                    flash("pedido atualizado com sucesso!")
                    return redirect(url_for("get_lista_pedido"))
                else:
                    flash(response["erro"])
        except Exception as e:
            flash(f"Erro ao atualizar: {str(e)}", "erro")

    response = get_consulta_pedido_id(id, token)

    if not response or "Pedido" not in response:  # evita KeyError
        flash(response.get("erro", response.get("msg", "Não foi possível carregar o pedido.")), "erro")
        return redirect(url_for('get_lista_pedido'))

    dados = response["Pedido"]

    return render_template("atualizar_pedido.html", var_pedido=dados)


@app.route('/atualizar/movimentacao/<int:id>', methods=["POST", "GET"])
def put_atualizar_movimentacao(id):
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        try:
            # Atualiza os campos do produto
            quantidade = request.form.get('quantidade')
            produto_id = request.form.get('produto_id')
            data = request.form.get('data')
            status = request.form.get('status')
            usuario_id = request.form.get('usuario_id')

            if quantidade and produto_id and data and status and usuario_id:

                response = put_atualizar_produto(quantidade,produto_id, data, status, usuario_id, id, token)
                print("mmm", response)
                if response:
                    flash("movimentacao atualizado com sucesso!")
                    return redirect(url_for("get_lista_movimentacao"))
                else:
                    flash(response["erro"])
        except Exception as e:
            flash(f"Erro ao atualizar: {str(e)}", "erro")

    response = get_consulta_movimentacao_id(id, token)

    if not response or "Movimentacao" not in response:  # evita KeyError
        flash(response.get("erro", response.get("msg", "Não foi possível carregar o movimentacao.")), "erro")
        return redirect(url_for('get_lista_movimentacao'))

    dados = response["Movimentacao"]

    return render_template("atualizar_movimentacao.html", var_movimentacao=dados)

@app.route("/cadastrar/usuario", methods=["GET", "POST"])
def post_cadastrar_usuario():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        nome = request.form.get("nome")
        CPF = request.form.get("CPF")
        email = request.form.get("email")
        papel = request.form.get("papel")

        if nome and CPF and email and papel:

            response = post_cadastrar_usuario(nome, CPF, email, papel, token)

            if response:
                flash("usuario cadastrado com sucesso!")
                return redirect(url_for("get_lista_usuario"))

            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))

    return render_template("cadastro_usuario.html")

@app.route("/cadastro/medicamento", methods=["GET", "POST"])
def post_cadastro_medicamento():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        nome_produto = request.form.get("nome")
        preco_produto = request.form.get("preco")
        descricao_produto = request.form.get("descricao")
        dimensao_produto = request.form.get("dimensao")
        peso_produto = request.form.get("peso")
        cor_produto = request.form.get("cor")
        uso = request.form.get("uso")
        parte_utilizada = request.form.get("parte_utilizada")
        forma_uso = request.form.get("forma_uso")
        imagem_url = request.form.get("imagem_url")

        if (nome_produto and preco_produto and descricao_produto and dimensao_produto and peso_produto
                and cor_produto and uso and parte_utilizada and forma_uso and imagem_url):

            response = post_cadastrar_usuario(nome_produto, preco_produto, descricao_produto,
                                              dimensao_produto, peso_produto, cor_produto, uso,
                                              parte_utilizada, forma_uso, imagem_url, token)

            if response:
                flash("medicamento cadastrado com sucesso!")
                return redirect(url_for("get_lista_produto"))

            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))

    return render_template("loja.html")


@app.route("/cadastro/produto", methods=["GET", "POST"])
def post_cadastro_produto():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        nome_produto = request.form.get("nome")
        preco_produto = request.form.get("preco")
        descricao_produto = request.form.get("descricao")
        dimensao_produto = request.form.get("dimensao")
        peso_produto = request.form.get("peso")
        cor_produto = request.form.get("cor")

        if nome_produto and preco_produto and descricao_produto and dimensao_produto and peso_produto and cor_produto:

            response = post_cadastro_produto(nome_produto, preco_produto, descricao_produto,
                                              dimensao_produto, peso_produto, cor_produto, token)

            if response:
                flash("produto cadastrado com sucesso!")
                return redirect(url_for("get_lista_produto"))

            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))

    return render_template("cadastro_produto.html")

@app.route("/cadastro/blog", methods=["GET", "POST"])
def post_cadastro_blog():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        usuario_id = request.form.get("usuario_id")
        comentario = request.form.get("comentario")
        titulo = request.form.get("titulo")
        data = request.form.get("data")

        if usuario_id and comentario and titulo and data:

            response = post_cadastro_blog( usuario_id, comentario, titulo, data, token)

            if response:
                flash("blog cadastrado com sucesso!")
                return redirect(url_for("get_lista_blog"))

            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))

    return render_template("cadastro_blog.html")

@app.route("/cadastro/movimentacao", methods=["GET", "POST"])
def post_cadastro_movimentacao():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        quantidade = request.form.get("quantidade")
        produto_id = request.form.get("produto_id")
        data = request.form.get("data")
        status = request.form.get("status")
        usuario_id = request.form.get("usuario_id")

        if quantidade and produto_id and data and status and usuario_id:

            response = post_cadastro_movimentacao( quantidade, produto_id, data, status, usuario_id, token)

            if response:
                flash("movimentacao cadastrado com sucesso!")
                return redirect(url_for("get_lista_movimentacao"))

            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))

    return render_template("cadastro_movimentacao.html")


@app.route("/cadastro/pedido", methods=["GET", "POST"])
def post_cadastro_pedido():
    if not token:
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        produto_id = request.form.get("produto_id")
        vendedor_id = request.form.get("vendedor_id")
        quantidade = request.form.get("quantidade")
        valor_total = request.form.get("valor_total")
        endereco = request.form.get("endereco")
        usuario_id = request.form.get("usuario_id")

        if produto_id and vendedor_id and quantidade and valor_total and endereco and usuario_id:

            response = post_cadastro_pedido( produto_id, vendedor_id, quantidade, valor_total, endereco, usuario_id, token)

            if response:
                flash("movimentacao cadastrado com sucesso!")
                return redirect(url_for("get_lista_movimentacao"))

            else:
                if "erro" in response:
                    flash(response["erro"])
                else:
                    flash(response["msg"])
                return redirect(url_for("pagina_inicial"))

    return render_template("cadastro_movimentacao.html")

@app.route("/consulta/usuario/<int:id>")
def get_consulta_usuario(id):
    dados = get_consulta_usuario(id)
    print("Dados recebidos:", dados)

    if "Usuario" in dados:
        usuario = dados["Usuario"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível encontrar o usuário.")
        return redirect(url_for("home"))

    return render_template("consulta_usuario.html", usuario=usuario)

@app.route("/consulta/produto/<int:id>")
def get_consulta_produto(id):
    dados = get_consulta_produto(id)
    print("Dados recebidos:", dados)

    if "Produto" in dados:
        produto = dados["Produto"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível encontrar o produto.")
        return redirect(url_for("home"))

    return render_template("consulta_produto.html", produto=produto)

@app.route("/consulta/blog/<int:id>")
def get_consulta_blog(id):
    dados = get_consulta_blog_id(id)
    print("Dados recebidos:", dados)

    if "Blog" in dados:
        blog = dados["Blog"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível encontrar o blog.")
        return redirect(url_for("home"))

    return render_template("consulta_blog.html", blog=blog)

@app.route("/consulta/pedido/<int:id>")
def get_consulta_pedido(id):
    dados = get_consulta_pedido_id(id)
    print("Dados recebidos:", dados)

    if "Pedido" in dados:
        pedido = dados["Pedido"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível encontrar o pedido.")
        return redirect(url_for("home"))

    return render_template("consulta_pedido.html", pedido=pedido)

@app.route("/consulta/movimentacao/<int:id>")
def get_consulta_movimentacao(id):
    dados = get_consulta_movimentacao_id(id)
    print("Dados recebidos:", dados)

    if "Movimentacao" in dados:
        movimentacao = dados["Movimentacao"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível encontrar a movimentação.")
        return redirect(url_for("home"))

    return render_template("consulta_movimentacao.html", movimentacao=movimentacao)

@app.route("/lista/usuario")
def get_lista_usuario():
    dados = get_lista_usuario()
    print("Dados recebidos:", dados)

    if "usuarios" in dados:
        usuarios = dados["usuarios"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar os usuários.")
        return redirect(url_for("home"))

    return render_template("lista_usuario.html", usuarios=usuarios)

@app.route("/lista/produto")
def get_lista_produto():
    dados = get_lista_produto()
    print("Dados recebidos:", dados)

    if "produtos" in dados:
        produtos = dados["produtos"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar os produtos.")
        return redirect(url_for("home"))

    return render_template("lista_produto.html", produtos=produtos)

@app.route("/lista/blog")
def get_lista_blog():
    dados = get_lista_blog()
    print("Dados recebidos:", dados)

    if "blogs" in dados:
        blogs = dados["blogs"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar os blogs.")
        return redirect(url_for("home"))

    return render_template("lista_blog.html", blogs=blogs)

@app.route("/lista/pedido")
def get_lista_pedido():
    dados = get_lista_pedido()
    print("Dados recebidos:", dados)

    if "pedidos" in dados:
        pedidos = dados["pedidos"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar os pedidos.")
        return redirect(url_for("home"))

    return render_template("lista_pedido.html", pedidos=pedidos)

@app.route("/lista/movimentacao")
def get_lista_movimentacao():
    dados = get_lista_movimentacao()
    print("Dados recebidos:", dados)

    if "movimentacoes" in dados:
        movimentacoes = dados["movimentacoes"]
    else:
        if "erro" in dados:
            flash(dados["erro"])
        else:
            flash("Não foi possível listar as movimentações.")
        return redirect(url_for("home"))

    return render_template("lista_movimentacao.html", movimentacoes=movimentacoes)



if __name__ == '__main__':
    app.run(debug=True)


