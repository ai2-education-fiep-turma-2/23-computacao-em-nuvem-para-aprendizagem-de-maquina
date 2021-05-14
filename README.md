# computacao-em-nuvem-para-aprendizagem-de-maquina

## Heroku

* Instalacao https://devcenter.heroku.com/articles/heroku-cli

```
sudo snap install --classic heroku
```

* Login no Heroku (Sem abrir o browser -i)

```
heroku login -i
```

* Criando uma aplicação no Heroku

```
heroku create dsview2 --buildpack heroku/python
```

* Obtendo ponto de montagem da aplicação (git clone)

```
git clone https://git.heroku.com/dsview2.git
```

* A partir desse ponto estará trabalhando em outro servidor git

* Montando uma aplicação
  * Configurar arquivos: Procfile, requirements.txt e runtime.txt

* requirements.txt 
    * Especifica os pacotes necessários para excutar a aplicação  
```
alembic==1.4.2
appdirs==1.4.4
attrs==19.3.0
cached-property==1.5.1
certifi==2020.4.5.2
chardet==3.0.4
click==7.1.2
defusedxml==0.6.0
Deprecated==1.2.10
dominate==2.5.1
Flask==1.1.2
Flask-Bootstrap==3.3.7.1
Flask-Migrate==2.5.3
Flask-Script==2.0.6
Flask-SQLAlchemy==2.4.3
Flask-WTF==0.14.3
gunicorn==20.0.4
idna==2.9
isodate==0.6.0
itsdangerous==1.1.0
Jinja2==2.11.2
lxml==4.5.1
Mako==1.1.3
MarkupSafe==1.1.1
pycep-correios==4.0.3
python-dateutil==2.8.1
python-editor==1.0.4
pytz==2020.1
requests==2.24.0
requests-toolbelt==0.9.1
six==1.15.0
SQLAlchemy==1.3.18
urllib3==1.25.9
visitor==0.1.3
Werkzeug==1.0.1
wrapt==1.12.1
WTForms==2.3.1
zeep==3.4.0
streamlit==0.75.0
```

* runtime.txt 
    * Especifica o ambiente no qual o fonte deve ser executado (python, java, node.js, etc) 	 
```
python-3.9.2
```

* Procfile  
    * Especifica como a aplicação entra em execução
    * Formato: process type: command
	* Process type
	    * web: aplicação para a qual será enviado pacotes HTTP
	    * worker: define que a aplicação atende múltiplas solicitações 
	    * clock: define que a aplicação entra em execução em intervalos regulares

* Exemplo:
``` 
web: sh setup.sh && streamlit run streamlit-teste.py
```

* Os arquivos setup.sh e stramlit.py fazem para da aplicação que vai ser montada

* setup.sh  
    * Esse script reconhece alguns aspectos do ambiente para colocar a aplicação no ar 
```
	mkdir -p ~/.streamlit
	echo "[server]
	headless = true
	port = $PORT
	enableCORS = false
	" > ~/.streamlit/config.toml
```

Seu Arquivo streamlit.py (deve chamar streamlit-teste.py)

```

import streamlit as st

def run():
    st.write("# Welcome to Streamlit!!!! ")
    st.write("# Welcome to Streamlit!!!! ")

if __name__ == "__main__":
    run()

```

* Suba os arquivos para a plataforma Heroku:

```
git add .
git commit -m "message"
git push origin master
```

* acessa em: https://dsview2.herokuapp.com

* Acessando logs

```
heroku logs 
```

* Inspecionando execução
```
heroku ps
```

* Exemplos:

```
heroku logs -a dsview2
heroku ps -a dsview2
```

## Docker


## Testando instalação do docker

```
docker run hello-world
```

Retorno:

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## Listando conteineres presentes no computador

```
docker image ls
```

## Mostrando conteineres que foram iniciadas nesse computador

```
docker ps --all
```

## apagar imagens docker

```
sudo docker rm nome-da-imagem
```
## limpar área do docker

```
docker system prune -a
```

## Montando um conteiner docker 

Um container é montado com base em um arquivo chamado dockerfile. A seguir replicamos uma fragmento do tutorial docker (https://docs.docker.com/get-started/part2/) passo a passo.

* Um conteiner é definido com base em uma imagem vazia, ou a partir de uma imagem existente
* A forma mais eficiente de manter um dockerfile é versionando no github
* O primeiro passo para criar um novo conteiner docker é obtendo a descrição e os arquivos necessários para criar o conteiner

```
git clone https://github.com/dockersamples/node-bulletin-board
cd node-bulletin-board/bulletin-board-app
```

* Conteúdo do dockerfile descritor da imagem

    * FROM utilize uma imagem pré-existente (criada pelo grupo que mantém o node.js)

    * WORKDIR especifica que todas as ações subseqüentes devem ser executadas no diretório /usr/src/ app no sistema de arquivos do conteiner (nunca no sistema de arquivos do host).

    * COPY copia o arquivo package.json do host para o local atual (.) Na sua imagem (neste caso, para /usr/src/app/package.json)

    * RUN Execute o comando npm install dentro do seu sistema de arquivos de imagem (utiliza o package.json instalar dependências)

    * COPY o restante do código-fonte do host para o sistema de arquivos de imagem.

```
FROM node:current-slim

WORKDIR /usr/src/app
COPY package.json .
RUN npm install

EXPOSE 8080
CMD [ "npm", "start" ]

COPY . .
```

* Montando um conteiner a partir da descrição
```
docker build --tag bulletinboard:1.0 .
```

* Iniciando o conteiner
```
docker run --publish 8000:8080 --detach --name bb bulletinboard:1.0
```

* O conteiner é iniciado de modo asíncrono liberado o terminal
* A porta 8080 são exportadas para serem acessíveis a partir do host do conteiner, porém essa porta é desviada para a porta 8000 do host

* Terminando a execução do conteiner
```
docker rm --force bb
```

* Criando uma versão nova de imagem com tag (troque silviostanzani pelo seu repo docker hub)

``` 
docker image tag bulletinboard:1.0 silviostanzani/bulletinboard:2.0
```
* armazenando imagem docker no espaço público do usuário (docker-hub)

```  
docker image push silviostanzani/bulletinboard:2.0
```

### Carregando container tensorflow

* Container com tensorflow para CPU

    * -it : inicia um terminal para acessar o Container
    * --rm : remove o container após sair do Container

```    
docker run -it --rm tensorflow/tensorflow bash
```

* Container com tensorflow para GPU

    * --runtime=nvidia : utilizar o runtime nvidia para mapear o driver nvidia para o container
```
sudo docker run -it --rm --runtime=nvidia tensorflow/tensorflow:latest-gpu bash
```

* Código para verificar presença da GPU

```
print(tf.config.list_physical_devices('GPU'))

print(('Is your GPU available for use?\n{0}').format(
    'Yes, your GPU is available: True' if tf.test.is_gpu_available() == True else 'No, your GPU is NOT available: False'
))

print(('\nYour devices that are available:\n{0}').format(
    [device.name for device in tf.config.experimental.list_physical_devices()]
))
```

* Container com tensorflow e Jupyter

```
docker run --gpus all -v /home/silvio/git:/tf -p 8888:8888 --user $(id -u):$(id -g) tensorflow/tensorflow:nightly-gpu-py3-jupyter
```

   * -v /notebooks:/tf/notebooks : mapeia o diretório local (~/notebooks) para o diretório do container (/tf/notebooks)  
   * -p 8889:8888 : mapeia porta do container (8889) para porta do host (8888)
   * Mapeando usuário do host para Container --user $(id -u):$(id -g)

### Configurando conteiner para executar um comando e terminar a execução

* Executando imagem com scikit
* 
```
sudo docker run -it devashishupadhyay/scikit-learn-docker
```

* Montando Container para realizar inferencias

```
sudo docker run -ti -v /home/silvio/git/23-computacao-em-nuvem-para-aprendizagem-de-maquina/modelo/:/tf devashishupadhyay/scikit-learn-docker bash /tf/exec.sh
```

* Montando Container para obter soliticação de inferencias por micro serviço

Dockerfile:
```
FROM devashishupadhyay/scikit-learn-docker
COPY exec2.sh /tmp
COPY exec3.sh /tmp
COPY scaler.pkl /tmp
COPY model.sav /tmp
COPY predicao.py /tmp
COPY predict-server.py /tmp
CMD /tmp/exec3.sh
```

* montando e executando
```
sudo docker image build -t scikit:pred .
sudo docker run scikit:pred
```
 
## AWS


* criar conta

* criar instancia EC2
  * console de controle de EC2 https://console.aws.amazon.com/ec2
  * Passos mínimos importantes
    * Criar chave ssh de acesso
    * liberar acesso a porta 22
   
* instalar aws-cli (https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)

* Associar acesso de ssh
  * criar access key e secret key: https://console.aws.amazon.com/iam/

* Download da chave pem

* configurando terminal para acessar ambientes de nuvem
   *  Informe o access key e secret key
   *  
```
aws configure
```

* listando instancias

	* aws ec2 describe-instances

* Filtrando informações das instâncias

```
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value|[0],State.Name,PrivateIpAddress,PublicIpAddress]' --output text | column -t
```

* start na instancia pela linha de comando

	* aws ec2 start-instances --instance-ids i-086c823ec7054b54e

* stop na instancia pela linha de comando

	* aws ec2 stop-instances --instance-ids i-086c823ec7054b54e

* fazer ssh
