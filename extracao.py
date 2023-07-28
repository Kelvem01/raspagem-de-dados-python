import sqlite3 # importando banco de dados para salvar itens

from requests_html import HTMLSession

secacao = HTMLSession ()

sapatos = []

url = ""  # adicionar url desejada para realizar extração dos dados desejados 
resposta = secacao.get()

links = resposta.html.find() #adicionar as divs dentra dos parenteses que deseja extrair 


for link in links:
    print ()
    url_sapatos = link.attrs['href'] #antes retirar os exemplos attrs e href e colocar um de seu desejo 
    print (url_sapatos)

    resosta_sapato = secacao.get(url_sapatos)
    titulo = resosta_sapato.html.find('h1', first = True). text # mudar onde esta a div h1 para uma de sua escolha 
    preco = resosta_sapato.html.find('h2')[2] # mudar o h1 e o numero 2 e colocar o da sua escolha 
    sapatos.append({
        'tipo_sapatos'
        'preco'
        'estoque'
    })

conexao = sqlite3.connect('nome do banco criado') # criar um banco de dados e adicionar ele aqui 
cursor = conexao.cursor()

sql =   'INSERT INTO sapatos (tipo_sapatos , preco , estoque) values (? ,? ,?)' # passa as tabelas que deseja inserir os dados e salvar no banco de dados

for sapato in sapatos:
    valores = [sapato ['tipo_sapatos'], preco ['preco'], estoque ['estoque']] # trocar os nomes de exemplo pelos de sua tabela 

conexao.commit() # commitando 
conexao.close()# fechando conexão com o banco de dados 

