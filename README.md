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

* Criando uma aplicação no HEroku

```
heroku create dsview2 --buildpack heroku/python
```

* Obtendo ponto de montagem da aplicação (git clone)

```
git clone https://git.heroku.com/dsview2.git
```

* A partir desse ponto estará trabalhando em outro servidor git

* Montando uma aplicação
  * Configurar arquivos: Procfile, requirements.txt, runtime.txt, setup.sh   

* Procfile  
	web: sh setup.sh && streamlit run streamlit-teste.py

* requirements.txt  
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

* runtime.txt  
	python-3.9.2

* setup.sh  

	mkdir -p ~/.streamlit

	echo "[server]
	
	headless = true
	
	port = $PORT
	
	enableCORS = false
	
	" > ~/.streamlit/config.toml

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
