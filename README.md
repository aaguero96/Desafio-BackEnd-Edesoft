# Desafio-BackEnd-Edesoft

## Iniciar a aplicação (local)

1. Clone o repositório

- Use o comando ```git clone https://github.com/tryber/sd-015-b-restaurant-orders.git``` para chaves HTTPS
- Use o comando ```git clone git@github.com:tryber/sd-015-b-restaurant-orders.git``` para chaves SSH

2. Entre na pasta do reposiótio clonado

- Use o comando ```cd Desafio-BackEnd-Edesoft/```

OBS. Caso não tenha o mongoDB rodando na porta <strong>27017</strong> rode o seguinte comando (garanta que nada rode nessa porta):

- ```docker run -d --name=mongo -p 27017:27017 bitnami/mongodb```

3. Crie o ambiente virtual para o projeto

- Use o comando ```python3 -m venv .venv && source .venv/bin/activate```

4. Instale as dependências

- Use o comando ```python3 -m pip install -r requirements.txt```

5. Inicie o programa

- Use o comando ```uvicorn index:app --reload```

6. Abra o navegar e utilize a API

- O navegador deve ser aberto em ```http://localhost:8000/docs```