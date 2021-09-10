import requests
import pandas as pd
url = 'https://query.wikidata.org/sparql' #API Endpoint
value = "museu" #Texto de busca

#SPARQL Query -não é necessário alterações.
query = """ SELECT ?sujeito ?instancia ?instanciaLabel WHERE {
     ?sujeito ?label "%s"@pt .
     ?sujeito wdt:P31 ?instancia
    SERVICE wikibase:label { bd:serviceParam wikibase:language "pt-br", "en". } 
    } """ %(value)

r = requests.get(url, params = {'format': 'json', 'query': query}) #consulta à API
data = r.json() #resposta da consulta à API em JSON

#Cria o array de dados. Foi utilizada uma estrutura de for otimizada em python
rows = [[value,item['sujeito']['value'],item['instancia']['value'],item['instanciaLabel']['value']] for item in data['results']['bindings']]

#Cria o dataframe
df = pd.DataFrame(rows,columns=["palavra","sujeito", "instancia","instanciaLabel"])

#Salva o dataframe em csv com encoding para portugues. Usei separacao por ; para melhor visualizar o arquivo csv no excel
df.to_csv("base_out2.csv",index=False,sep=';',encoding='ISO-8859-1')