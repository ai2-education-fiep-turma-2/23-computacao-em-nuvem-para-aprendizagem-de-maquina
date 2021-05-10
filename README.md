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

* runtime.txt  
	python-3.9.2

* setup.sh  
	mkdir -p ~/.streamlit
	echo "[server]
	headless = true
	port = $PORT
	enableCORS = false
	" > ~/.streamlit/config.toml

Seu Arquivo streamlit.py

* Suba os arquivos para a plataforma Heroku:

```
git add .
git commit -m "message"
git push origin master
```

* acessa em: https://dsview2.herokuapp.com
