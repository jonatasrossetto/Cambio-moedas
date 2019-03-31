import os
import requests 
import json
import pandas as pd #cria um acrônimo 'ps' para o nome da biblioteca 'pandas'

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
    day=day[8:10]+"/"+day[5:7]+"/"+day[0:4]
    #print(day)
    #print("%s / %s / %s" % (day[8:10],day[5:7],day[0:4])) 
    dados1=response._content #aparentemente content não estrutura os dados
    #print(dados['rates']['EUR'])
    #print(dados['rates']['BRL'])
    #print(dados['rates']['USD'])
    #print(dados['rates']['BTC'])

    euro=dados['rates']['EUR']
    real=dados['rates']['BRL']
    dolar=dados['rates']['USD']
    bitcoin=dados['rates']['BTC']

    #convertendo para reais

    print("1 euro equivale a %.3f"% (real/euro)," reais")
    print("1 usd equivale a %.3f"% (real/dolar)," reais")
    print("1 bitcoin equivale a %.3f"% (real/bitcoin)," reais")

    euro_brl=round(real/euro,2)         #Conversão de euro para real
    dolar_brl=round(real/dolar,2)       #Conversão de dolar para real
    bitcoin_brl=round(real/bitcoin,2)   #Conversão de Bitcoin para real

    #Cria um frame, tabela/dicionário, com valores da conversão para exportar
    #como arquivo .csv para abrir em outros softwares, com o excel por exemplo
    
    #df=pd.DataFrame({'Moedas': ['Euro', 'Dollar','Bitcoin'],'Valores':[euro_brl,dolar_brl,bitcoin_brl]})
    df=pd.DataFrame({'Data':[day,day,day], 'Moedas': ['Euro', 'Dollar','Bitcoin'],'Valores':[euro_brl,dolar_brl,bitcoin_brl]})
    df.to_csv("valores.csv", index=False, sep=";", decimal=",")
    print(df)
    

    print("que legal!!! funcionou!!!")


