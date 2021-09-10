import pandas as pd
import requests
import math

colDict = {} #dicionário para armazenar dados de coleções
install = "https://museudoouro.acervos.museus.gov.br/" #link do museu
col_endpoint  = install+"/wp-json/tainacan/v2/collections/" #endpoint da API para listar as coleções do acervo
col_r  =  requests.get(col_endpoint).json() #resultado da consulta das coleções do acervo

for collection in col_r:  #Cria um dicionário com os dados das coleções encontradas
    colDict[collection['name']] = {'id':collection['id'], 'total_items':collection['total_items']['publish']}

rows = []
for collectionName in colDict.keys():#itera para cada coleção encontrada
    total_pages = int(colDict[collectionName]['total_items'])/25 ##calcula o total de páginas de resultados
    print("Coletado dados para a coleção {}".format(collectionName))
    for page in range(int(math.ceil(total_pages))): #itera pelas páginas de resultados   
        page +=1 #pula a primeira página, a página 0 e 1 são iguais
        items_endpoint = install+"/wp-json/tainacan/v2/collection/{}/items/?perpage=25&paged={}".format(colDict[collectionName]['id'], page) #consulta à API
        item_r = requests.get(items_endpoint).json() #resultado da consulta em JSON
        if item_r["items"] == []:#se não houver mais dados para o script
            print("   * Todos os itens da coleção {} coletados".format(collectionName))
            break
        elif type(item_r) == dict:#se houver dados para coletar
            for item in item_r["items"]:#para cada item
                print("Coletando o item {}".format(item['id']))
                for metadata in item['metadata'].keys():#coleta os metadados e seus respectivos valores
                    metadado = item['metadata'][metadata]['name']#armazena o metadado
                    valor = item['metadata'][metadata]['value_as_string']#armazena os valores do metadado
                    if valor == "": #desconsidera valores nulos
                        continue
                    else: #Salve os valores das variáveis “metadado” em colunas e “valor” em linhas em um CSV.
                        rows.append([metadado,valor])


#Cria o dataframe
df = pd.DataFrame(rows,columns=["metadado","valor"])

#Salva o dataframe em csv . Usei separacao por ; para melhor visualizar o arquivo csv no excel
df.to_csv("base_out3.csv",index=False,sep=';',encoding='utf-16')