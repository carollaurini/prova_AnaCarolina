import requests
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

for item in data['results']['bindings']: #Loop para iterar pelos resultados.
    print(value, item['sujeito']['value'], item['instancia']['value'], item['instanciaLabel']['value']) #Resultados




















