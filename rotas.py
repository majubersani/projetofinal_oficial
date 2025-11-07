import requests

def get_consulta_usuario(id):
    url = f'http://10.135.235.31:5002/consulta/usuario/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Usuario']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}

def get_consulta_produto(id):
    url = f'http://10.135.235.31:5002/consulta/produto/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Produto']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}

def get_consulta_blog_id(id):
    url = f'http://10.135.235.31:5002/consulta/blog/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Blog']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}

def get_consulta_pedido_id(id):
    url = f'http://10.135.235.31:5002/consulta/pedido/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Pedido']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}

def get_consulta_movimentacao_id(id):
    url = f'http://10.135.235.31:5002/consulta/movimentacao/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Movimentacao']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_lista_usuario():
    url = f'http://10.135.235.31:5002/lista/usuario'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}

def get_lista_produto():
    url = f'http://10.135.235.31:5002/lista/produto'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}

def get_lista_blog():
    url = f'http://10.135.235.31:5002/lista/blog'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def get_lista_pedido():
    url = f'http://10.135.235.31:5002/lista/pedido'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}

def get_lista_movimentacao():
    url = f'http://10.135.235.31:5002/lista/movimentacao'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}

def put_atualizar_usuario(nome, CPF, email, papel):
    url = f'http://10.135.235.31:5002/atualizar/usuario/{id}'
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
    url = f'http://10.135.235.31:5002/atualizar/produto/{id}'
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
    url = f'http://10.135.235.31:5002/atualizar/blog/{id}'
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
    url = f'http://10.135.235.31:5002/atualizar/pedido/{id}'
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
    url = f'http://10.135.235.31:5002/atualizar/movimentacao/{id}'
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

def post_cadastrar_usuario(id,nome,CPF,email,papel):
    url= f'http://127.0.0.1:5003/cadastro/usuario{id}'
    input_usuario = {
        "nome":nome,
        "CPF":CPF,
        "email":email,
        "papel":papel,
    }
    response = requests.post(url, json=input_usuario)
    if response.status_code == 201:
        dados = response.json()
        print(f'nome:{dados["nome"]}\n')
        print(f'CPF:{dados["CPF"]}\n')
        print(f'email:{dados["email"]}\n')
        print(f'papel:{dados["papel"]}\n')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}

def post_cadastro_medicamento(id,nome_produto,preco_produto,descricao_produto,
                              dimensao_produto,peso_produto,cor_produto,uso,parte_utilizada,forma_uso,imagem_url):
    url= f'http://127.0.0.1:5003/cadastro/medicamento{id}'
    input_produto = {
        "nome_produto":nome_produto,
        "preco_produto":preco_produto,
        "descricao_produto":descricao_produto,
        "dimensao_produto":dimensao_produto,
        "peso_produto":peso_produto,
        "cor_produto":cor_produto,
        "uso":uso,
        "parte_utilizada":parte_utilizada,
        "forma_uso":forma_uso,
        "imagem_url":imagem_url
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

def post_cadastro_produto(id,nome_produto,preco_produto,descricao_produto,
                              dimensao_produto,peso_produto,cor_produto):
    url= f'http://127.0.0.1:5003/cadastro/produto{id}'
    input_produto = {
        "nome_produto": nome_produto,
        "preco_produto": preco_produto,
        "descricao_produto": descricao_produto,
        "dimensao_produto": dimensao_produto,
        "peso_produto": peso_produto,
        "cor_produto": cor_produto,
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
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}

def post_cadastro_blog(id,usuario_id,comentario,titulo,data):
    url= f'http://127.0.0.1:5003/cadastro/blog/{id}'
    input_blog = {
        "usuario_id":usuario_id,
        "comentario":comentario,
        "titulo":titulo,
        "data":data,
    }
    response = requests.post(url, json=input_blog)
    if response.status_code == 201:
        dados = response.json()
        print(f'usuario_id:{dados["usuario_id"]}\n')
        print(f'comentario:{dados["comentario"]}\n')
        print(f'titulo:{dados["titulo"]}\n')
        print(f'data:{dados["data"]}\n')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}

def post_cadastro_movimentacao(id,quantidade,produto_id,data,status,usuario_id):
    url = f'http://127.0.0.1:5003/cadastro/movimentacao/{id}'
    input_movimentacao = {
        "quantidade":quantidade,
        "produto_id":produto_id,
        "data":data,
        "status":status,
        "usuario_id":usuario_id,
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

def post_cadastro_pedido(id,produto_id,vendedor_id,quantidade,
                         valor_total,endereco,usuario_id):
    url = f'http://127.0.0.1:5003/cadastro/pedido/{id}'
    input_pedido = {
        "produto_id":produto_id,
        "vendedor_id":vendedor_id,
        "quantidade":quantidade,
        "valor_total":valor_total,
        "endereco":endereco,
        "usuario_id":usuario_id,
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
    url = f'http://10.135.235.31:5002/login/'
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


def post_cadastro_medicamento(id_produto,nome_produto,preco_produto,descricao_produto,
                              fabricante,categoria_produto,dimensao_produto,peso_produto,cor_produto,
                              uso,parte_utilizada,forma_usu,imagem_url):
    url = f'http://127.0.0.1:5003/cadastro/medicamento/{id}'
    input_medicamento = {
        "nome_produto":nome_produto,
        "preco_produto":preco_produto,
        "descricao_produto":descricao_produto,
        "fabricante":fabricante,
        "categoria_produto":categoria_produto,
        "dimensao_produto":dimensao_produto,
        "peso_produto":peso_produto,
        "cor_produto":cor_produto,
        "uso":uso,
        "parte_utilizada":parte_utilizada,
        "forma_usu":forma_usu,
        "imagem_url":imagem_url
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

def post_cadastro_envio(id_envio,usuario_id,nome_destinatario,
                        endereco,cidade,estado,CEP,telefone,email):
    url = f'http://127.0.0.1:5003/cadastro/envio/{id}'
    input_envio = {
        "id_envio":id_envio,
        "usuario_id":usuario_id,
        "nome_destinatario":nome_destinatario,
        "endereco":endereco,
        "cidade":cidade,
        "estado":estado,
        "CEP":CEP,
        "telefone":telefone,
        "email":email
    }
    response = requests.post(url, json=input_envio)
    if response.status_code == 200:
        dados = response.json()
        print(f'id_envio:{dados["id_envio"]}\n')
        print(f'usuario_id:{dados["usuario_id"]}\n')
        print(f'nome_destinatario:{dados["nome_destinatario"]}')
        print(f'endereco:{dados["endereco"]}\n')
        print(f'cidade:{dados["cidade"]}\n')
        print(f'estado:{dados["estado"]}\n')
        print(f'CEP:{dados["CEP"]}\n')
        print(f'telefone:{dados["telefone"]}\n')
        print(f'email:{dados["email"]}\n')
        return dados
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}

def post_cadastro_cartao(id_cartao,usuario_id,nome_titular,numero_cartao,data_validade,CVV):
    url = f'http://127.0.0.1:5003/cadastro/cartao/{id}'
    input_cartao = {
        "id_cartao":id_cartao,
        "nome_titular":nome_titular,
        "numero_cartao":numero_cartao,
        "data_validade":data_validade,
        "CVV":CVV
    }
    response = requests.post(url, json=input_cartao)
    if response.status_code == 200:
        dados = response.json()
        print(f'id_cartao:{dados["id_cartao"]}\n')
        print(f'nome_titular:{dados["nome_titular"]}\n')
        print(f'numero_cartao:{dados["numero_cartao"]}\n')
        print(f'data_validade:{dados["data_validade"]}\n')
        print(f'CVV:{dados["CVV"]}\n')
        dados = response.json()
    else:
        print(f"erro:{response.status_code}")
        return {"erro": response.json()}

def put_atualizar_envio(nome_destinatario,endereco,cidade,estado,CEP,telefone,email):
    url = f'http://10.135.235.31:5002/atualizar/envio/{id}'
    envio = {
        'nome_destinatario':nome_destinatario,
        'endereco':endereco,
        'cidade':cidade,
        'estado':estado,
        'CEP':CEP,
        'telefone':telefone,
        'email':email
    }
    response = requests.put(url, json=envio)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}


def put_atualizar_cartao(nome_titular,numero_cartao,data_validade,CVV):
    url = f'http://10.135.235.31:5002/atualizar/cartao/{id}'
    cartao = {
        'nome_titular':nome_titular,
        'numero_cartao':numero_cartao,
        'data_validade':data_validade,
        'CVV':CVV
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
    url = f'http://10.135.235.31:5002/consulta/envio/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print(dados)
        return dados['Envio']
    else:
        print(f'erro:{response.status_code}')
        return {'erro': response.json()}





