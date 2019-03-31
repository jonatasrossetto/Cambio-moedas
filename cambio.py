import os
import requests 

#limpando a tela no dos
os.system('cls' if os.name == 'nt' else 'clear')


url="http://data.fixer.io/api/latest?access_key=3ea8603d68b09980f633c36c92977fd2"

print("acessando base de dados ...")
response=requests.get(url)
#print(response)

if response.status_code==200: #código de resposta dizendo que o site está de pé!!!
    print("Hei, consegui acessar a base de dados!!!")
    print("agora estou buscando informações das moedas ...")
    dados=response.json() #desempacotar os dados em json na resposta da API
    day=dados['date']
    print(day)
    print("%s / %s / %s" % (day[8:10],day[5:7],day[0:4])) 
    dados1=response._content #aparentemente content não estrutura os dados
    print(dados['rates']['EUR'])
    print(dados['rates']['BRL'])
    print(dados['rates']['USD'])
    print(dados['rates']['BTC'])

    euro=dados['rates']['EUR']
    real=dados['rates']['BRL']
    dolar=dados['rates']['USD']
    bitcoin=dados['rates']['BTC']

    #convertendo para reais

    print("1 euro equivale a %.3f"% (real/euro)," reais")
    print("1 usd equivale a %.3f"% (real/dolar)," reais")
    print("1 bitcoin equivale a %.3f"% (real/bitcoin)," reais")

    print("que legal!!! funcionou!!!")


