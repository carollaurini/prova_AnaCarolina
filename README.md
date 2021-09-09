# Desafio de seleção

## Configuração inicial:

Para executar o ambiente do desafio, você precisa ter instalado em sua máquina o docker e o docker-compose:

1 - Para instalar o docker: https://docs.docker.com/get-docker/

2 - Para instalar o docker-compose: https://docs.docker.com/compose/install/

### Estrutura de diretórios:

A estrutura de diretório do ambiente é descrita a seguir:

```
  volumes/html -> pasta com os arquivos da instalação do wordpress

  volumes/data -> diretório que armazena o banco de dados do wordpress.

  volumes/init.d -> script de inicialização da base.

  docker-compose.yml -> arquivo yml com a configuração do ambiente

  README.md -> arquivo com instruções

  run.sh -> script para auxiliar a subir e derrubar o ambiente (apenas ambiente linux)
```

Durante o desafio, você provavelmente irá trabalhar mais com a pasta do tema `/volumes/html/wp-content/themes/twentyseventeen`.

### Iniciando o ambiente:

Para inicializar o ambiente de desenvolvimento, você pode na raiz do diretório, executar o seguinte comando:

- `./run.sh --start`: Vai inicializar os serviços, na primeira execução ele deve demorar um pouco pois irá baixar as imagens do repositório do docker.

- `./run.sh --start-bg`: Mesmo comportamento do `--start` porém roda o processo em segundo plano

> _observação_: o script `run.sh` foi testado somente em ambientes Linux, caso você utilize outro sistema operacional você pode utilizar os comandos padrões do docker-compose: [ `docker-compose up` ou `docker-compose up -d` ]

Após inicializar o ambiente você pode acessar atraves de um navegado o endereço: [http://localhost:8012/](http://localhost:8012/) que uma instalação padrão do wordpress deve ser exibida.

Para acessar a painel administrativo, você deve utilizar o endereço:
[http://localhost:8012/wp-admin](http://localhost:8012/wp-admin) com as credenciais:

```
user: dev
password: dev123
```

### Desativando o ambiente:

- `./run.sh --stop`: Finaliza os serviços.

> _observação_: o script `run.sh` foi testado somente em ambientes Linux, caso você utilize outro sistema operacional você pode utilizar os comandos padrões do docker-compose: [ `docker-compose down` ]

#### problemas comuns:

```
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?
```

verifique se o docker foi inicializado corretamente, `docker ps` deve mostrar a lista de containers que está rodando. Pode ser um problema com permissão também, tente usar o **sudo**

---

```
Error starting userland proxy: listen tcp 0.0.0.0:8012: bind: address already in use
```

Algum outro serviço está sendo executado na porta 8012, você deve finalizar esse serviço para que o servidor possa inicializar corretamente.
