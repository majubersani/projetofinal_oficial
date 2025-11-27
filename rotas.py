import requests

url_mestra = f'http://127.0.0.1:5003'

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#
#         if "Authorization" in request.headers:
#             token = request.headers["Authorization"].replace("Bearer ", "")
#
#         if not token:
#             return jsonify({"erro": "Token não fornecido"}), 401
#
#         return f(token, *args, **kwargs)
#     return decorated


def get_consulta_usuario(id):
    url = f'{url_mestra}/consulta/usuario/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Usuario']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_consulta_produto(id):
    url = f'{url_mestra}/consulta/produto/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Produto']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_consulta_blog_id(id):
    url = f'{url_mestra}/consulta/blog/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Blog']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_consulta_pedido_id(id):
    url = f'{url_mestra}/consulta/pedido/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Pedido']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_consulta_movimentacao_id(id):
    url = f'{url_mestra}/consulta/movimentacao/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Movimentacao']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


# def get_lista_usuario():
#     url = f'{url_mestra}/lista/usuario/{id}'
#     response = requests.get(url)
#     if response.status_code == 200:
#         dados = response.json()
#         print(dados)
#         return dados
#     else:
#         print(f'erro:{response.status_code}')
#         return {'erro': response.json()}

def get_lista_usuario():
    url = f'{url_mestra}/lista/usuario/{id}'
    response = requests.get(url)

    print(f"Status da resposta: {response.status_code}")
    print(f"Conteúdo da resposta: {response.text}")

    if response.status_code == 200:
        try:
            dados = response.json()
            print("Dados JSON:", dados)
            return dados
        except ValueError:
            print("Erro: resposta não contém JSON válido.")
            return {'erro': 'Resposta inválida do servidor'}
    else:
        # Evita tentar fazer .json() em erro
        try:
            erro = response.json()
        except ValueError:
            erro = {'mensagem': response.text}
        return {'erro': f'Erro {response.status_code}', 'detalhes': erro}


def get_lista_produto():
    url = f'{url_mestra}/lista/produto'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_lista_blog():
    url = f'{url_mestra}/lista/blog'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_lista_pedido():
    url = f'{url_mestra}/lista/pedido'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_lista_movimentacao():
    url = f'{url_mestra}/lista/movimentacao'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def put_atualizar_usuario(nome, CPF, email, papel):
    url = f'{url_mestra}/atualizar/usuario/{id}'
    usuario = {
        'nome': nome,
        'cpf': CPF,
        'email': email,
        'papel': papel
    }
    response = requests.put(url, json=usuario)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def put_atualizar_produto(nome_produto, dimensao_produto,
                          preco_produto, peso_produto,
                          cor_produto, descricao_produto):
    url = f'{url_mestra}/atualizar/produto/{id}'
    produto = {
        'nome_produto': nome_produto,
        'dimensao_produto': dimensao_produto,
        'preco_produto': preco_produto,
        'peso_produto': peso_produto,
        'cor_produto': cor_produto,
        'descricao_produto': descricao_produto
    }
    response = requests.put(url, json=produto)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def put_atualizar_blog(titulo, data, comentario, usuario_id):
    url = f'{url_mestra}/atualizar/blog/{id}'
    blog = {
        'titulo': titulo,
        'data': data,
        'comentario': comentario,
        'usuario_id': usuario_id
    }
    response = requests.put(url, json=blog)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def put_atualizar_pedido(usuario_id, produto_id, quantidade,
                         valor_total, endereco, vendedor_id):
    url = f'{url_mestra}/atualizar/pedido/{id}'
    pedido = {
        'usuario_id': usuario_id,
        'produto_id': produto_id,
        'quantidade': quantidade,
        'valor_total': valor_total,
        'endereco': endereco,
        'vendedor_id': vendedor_id
    }
    response = requests.put(url, json=pedido)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def put_atualizar_movimentacao(quantidade, produto_id, data, status, usuario_id):
    url = f'{url_mestra}/atualizar/movimentacao/{id}'
    movimentacao = {
        'quantidade': quantidade,
        'produto_id': produto_id,
        'data': data,
        'status': status,
        'usuario_id': usuario_id
    }
    response = requests.put(url, json=movimentacao)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def post_cadastrar_usuario(nome, CPF, email, senha, papel):
    url = f'{url_mestra}/cadastro/usuario'
    input_usuario = {
        "nome": nome,
        "CPF": CPF,
        "email": email,
        "senha": senha,
        "papel": papel,
    }
    response = requests.post(url, json=input_usuario)
    if response.status_code == 201:
        dados = response.json()
        print(f'nome:{dados["nome"]}\n')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}


def post_cadastro_medicamento( nome_produto, preco_produto, descricao_produto,
                              dimensao_produto, peso_produto, cor_produto, uso, parte_utilizada, forma_uso, imagem_url):
    url = f'{url_mestra}/cadastro/medicamento'
    input_produto = {
        "nome_produto": nome_produto,
        "preco_produto": preco_produto,
        "descricao_produto": descricao_produto,
        "dimensao_produto": dimensao_produto,
        "peso_produto": peso_produto,
        "cor_produto": cor_produto,
        "uso": uso,
        "parte_utilizada": parte_utilizada,
        "forma_uso": forma_uso,
        "imagem_url": imagem_url
    }
    response = requests.post(url, json=input_produto)
    if response.status_code == 201:
        dados = response.json()
        print(f'nome_produto:{dados["nome_produto"]}\n')
        print(f'preco_produto:{dados["preco_produto"]}\n')
        print(f'descricao_produto:{dados["descricao_produto"]}\n')
        print(f'dimensao_produto:{dados["dimensao_produto"]}')
        print(f'peso_produto:{dados["peso_produto"]}\n')
        print(f'cor_produto:{dados["cor_produto"]}\n')
        print(f'uso:{dados["uso"]}\n')
        print(f'parte_utilizada:{dados["parte_utilizada"]}')
        print(f'forma_uso:{dados["forma_uso"]}\n')
        print(f'imagem_url:{dados["imagem_url"]}')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}


def post_cadastro_produto(nome_produto, preco_produto, categoria_produto, descricao_produto, fabricante_produto,
                          dimensao_produto, peso_produto, cor_produto, uso, parte_utilizado, imagem_produto):
    url = f'{url_mestra}/cadastro/produto'
    print(url)
    input_produto = {
        "nome_produto": nome_produto,
        "preco_produto": preco_produto,
        "categoria_produto": categoria_produto,
        "descricao_produto": descricao_produto,
        "fabricante": fabricante_produto,
        "dimensao_produto": dimensao_produto,
        "peso_produto": peso_produto,
        "cor_produto": cor_produto,
        "uso": uso,
        "forma_uso": uso,
        "parte_utilizada": parte_utilizado,
        "imagem_url": imagem_produto
    }
    response = requests.post(url, json=input_produto)
    if response.status_code == 201:
        dados = response.json()
        print(f'nome_produto:{dados["nome_produto"]}\n')
        return dados
    else:
        print(f"erro:{response}")
        return {"erro": response.json()}


def post_cadastro_blog( usuario_id, comentario, titulo, data, link_video):
    url = f'{url_mestra}/cadastro/blog'
    input_blog = {
        "usuario_id": usuario_id,
        "comentario": comentario,
        "titulo": titulo,
        "data": data,
        "link_video": link_video,
    }
    response = requests.post(url, json=input_blog)
    if response.status_code == 201:
        dados = response.json()
        print(f'usuario_id:{dados["usuario_id"]}\n')
        print(f'comentario:{dados["comentario"]}\n')
        print(f'titulo:{dados["titulo"]}\n')
        print(f'data:{dados["data"]}\n')
        print(f'link_video:{dados['link_video']}\n')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}


def post_cadastro_movimentacao(quantidade, produto_id, data, status, usuario_id):
    url = f'{url_mestra}/cadastro/movimentacao'
    input_movimentacao = {
        "quantidade": quantidade,
        "produto_id": produto_id,
        "data": data,
        "status": status,
        "usuario_id": usuario_id,
    }
    response = requests.post(url, json=input_movimentacao)
    if response.status_code == 201:
        dados = response.json()
        print(f'quantidade:{dados["quantidade"]}\n')
        print(f'produto_id:{dados["produto_id"]}\n')
        print(f'data:{dados["data"]}\n')
        print(f'status:{dados["status"]}\n')
        print(f'usuario_id:{dados["usuario_id"]}\n')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}


def post_cadastro_pedido(id, produto_id, vendedor_id, quantidade,
                         valor_total, endereco, usuario_id):
    url = f'{url_mestra}/cadastro/pedido/{id}'
    input_pedido = {
        "produto_id": produto_id,
        "vendedor_id": vendedor_id,
        "quantidade": quantidade,
        "valor_total": valor_total,
        "endereco": endereco,
        "usuario_id": usuario_id,
    }
    response = requests.post(url, json=input_pedido)
    if response.status_code == 201:
        dados = response.json()
        print(f'produto_id:{dados["produto_id"]}\n')
        print(f'vendedor_id:{dados["vendedor_id"]}\n')
        print(f'quantidade:{dados["quantidade"]}\n')
        print(f'valor_total:{dados["valor_total"]}\n')
        print(f'endereco:{dados["endereco"]}\n')
        print(f'usuario_id:{dados["usuario_id"]}\n')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}


def post_login(email, password):
    url = f'{url_mestra}/login/'
    input_login = {
        'email': email,
        'password': password
    }
    response = requests.post(url, json=input_login)
    if response.status_code == 200:
        dados = response.json()
        print(f'email:{dados["email"]}\n')
        print(f'password:{dados["password"]}\n')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}


def post_cadastro_medicamento(id_produto, nome_produto, preco_produto, descricao_produto,
                              fabricante, categoria_produto, dimensao_produto, peso_produto, cor_produto,
                              uso, parte_utilizada, forma_usu, imagem_url):
    url = f'{url_mestra}/cadastro/medicamento'
    input_medicamento = {
        "nome_produto": nome_produto,
        "preco_produto": preco_produto,
        "descricao_produto": descricao_produto,
        "fabricante": fabricante,
        "categoria_produto": categoria_produto,
        "dimensao_produto": dimensao_produto,
        "peso_produto": peso_produto,
        "cor_produto": cor_produto,
        "uso": uso,
        "parte_utilizada": parte_utilizada,
        "forma_usu": forma_usu,
        "imagem_url": imagem_url
    }
    response = requests.post(url, json=input_medicamento)
    if response.status_code == 201:
        dados = response.json()
        print(f'nome_produto:{dados["nome_produto"]}\n')
        print(f'preco_produto:{dados["preco_produto"]}\n')
        print(f'descricao_produto:{dados["descricao_produto"]}\n')
        print(f'fabricante:{dados["fabricante"]}\n')
        print(f'categoria_produto:{dados["categoria_produto"]}\n')
        print(f'dimensao_produto:{dados["dimensao_produto"]}')
        print(f'peso_produto:{dados["peso_produto"]}\n')
        print(f'cor_produto:{dados["cor_produto"]}\n')
        print(f'uso:{dados["uso"]}\n')
        print(f'parte_utilizada:{dados["parte_utilizada"]}\n')
        print(f'forma_usu:{dados["forma_usu"]}\n')
        print(f'imagem_url:{dados["imagem_url"]}')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}


def post_cadastro_envio(usuario_id, nome_destinatario,
                        endereco, cidade, estado, CEP, telefone, email):

    url = f'{url_mestra}/cadastro/envio'  # corrigido

    input_envio = {
        "usuario_id": usuario_id,
        "nome_destinatario": nome_destinatario,
        "endereco": endereco,
        "cidade": cidade,
        "estado": estado,
        "CEP": CEP,
        "telefone": telefone,
        "email": email
    }

    response = requests.post(url, json=input_envio)

    if response.status_code == 201:
        dados = response.json()

        print(f'usuario_id: {dados.get("usuario_id")}')
        print(f'nome_destinatario: {dados.get("nome_destinatario")}')
        print(f'endereco: {dados.get("endereco")}')
        print(f'cidade: {dados.get("cidade")}')
        print(f'estado: {dados.get("estado")}')
        print(f'CEP: {dados.get("CEP")}')
        print(f'telefone: {dados.get("telefone")}')
        print(f'email: {dados.get("email")}')

        return dados
    else:
        print(f"erro:{response}")
        return {"erro": response.json()}


def post_cadastro_cartao(usuario_id, nome_titular, numero_cartao, data_validade, CVV):
    url = f'{url_mestra}/cadastro/cartao'
    input_cartao = {
        "usuario_id": usuario_id,
        "nome_titular": nome_titular,
        "numero_cartao": numero_cartao,
        "data_validade": data_validade,
        "CVV": CVV
    }
    response = requests.post(url, json=input_cartao)
    if response.status_code == 201:
        dados = response.json()
        print("usuario_id:", dados.get("usuario_id"))
        print(f'nome_titular:{dados["nome_titular"]}\n')
        print(f'numero_cartao:{dados["numero_cartao"]}\n')
        print(f'data_validade:{dados["data_validade"]}\n')
        print(f'CVV:{dados["CVV"]}\n')
        return dados
    else:
        print(f"erro:{response}")
        return {"erro": response.json()}


def put_atualizar_envio(nome_destinatario, endereco, cidade, estado, CEP, telefone, email):
    url = f'{url_mestra}/atualizar/envio/{id}'
    envio = {
        'nome_destinatario': nome_destinatario,
        'endereco': endereco,
        'cidade': cidade,
        'estado': estado,
        'CEP': CEP,
        'telefone': telefone,
        'email': email
    }
    response = requests.put(url, json=envio)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def put_atualizar_cartao(nome_titular, numero_cartao, data_validade, CVV):
    url = f'{url_mestra}/atualizar/cartao/{id}'
    cartao = {
        'nome_titular': nome_titular,
        'numero_cartao': numero_cartao,
        'data_validade': data_validade,
        'CVV': CVV
    }
    response = requests.put(url, json=cartao)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_consulta_envio(id):
    url = f'{url_mestra}/consulta/envio/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Envio']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}

# ---------------------------------
# Função da API (igual você enviou)
# ---------------------------------
def get_grafico_mais_vendidos(token):
    try:
        url = f"{url_mestra}/pedido"
        headers = {"Authorization": f"Bearer {token}"}
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status()
        data = resposta.json()

        if "erro" in data:
            return {"erro": data["erro"]}

        pedidos = data.get("pedidos", [])
        if not pedidos:
            return {"produtos_mais_vendidos": []}

        import pandas as pd
        df = pd.DataFrame(pedidos)

        if 'nome_pedido' not in df.columns or 'quantidade_pedido' not in df.columns:
            return {"erro": "Dados de pedidos incompletos."}

        df_vendidos = (
            df.groupby('nome_pedido', as_index=False)['quantidade_pedido']
            .sum()
            .sort_values(by='quantidade_pedido', ascending=False)
            .head(5)
        )

        produtos_mais_vendidos = df_vendidos.to_dict(orient='records')
        return {"produtos_mais_vendidos": produtos_mais_vendidos}

    except Exception as e:
        return {"erro": str(e)}

