# Projeto Aprendizagem de Máquina - Airbnb

## Descrição
Projeto referente a solução do desafio 'Airbnb New User Bookings' no Kaggle. Link: https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings

## Integrantes
- Alexandre Vianna (asgv@cin.ufpe.br)
- Everaldo Neto (ecsn@cin.ufpe.br)
- Igor Simões (isol2@cin.ufpe.br)
- Natacha Targino (ntrsb@cin.ufpe.br)

## Instalação
- python >= 3.x
```
$ git clone https://github.com/AlexandreSGV/cin_am_airbnb
$ cd cin_am_airbnb && sudo pip3 install -rrequirements.txt
```
## Datasets
 - Devido ao tamanho dos dados do airbnb, é necessário baixar manualmente através da página do desafio: [airbnb-recruiting-new-user-bookings/data](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/data) e adicioná-los na pasta `input`
 - Nesta solução utilizamos os arquivos: train_users_2.csv, test_users.csv e sessions.csv

## Como executar
 As etapas de limpeza de dados e treino podem ser bastante demoradas, pois os datasets são grandes, por isso incluimos os artefatos resultantes dessas atividades (dados limpos e modelos treinados) no arquivo [OUTPUT.ZIP](https://drive.google.com/drive/u/1/folders/1IdV1JT4pqESEJJ_7DcpAeN4MbqDlLIKl).  Basta descompactar os arquivos na pasta 'output', se fizer esta opção não será necessário executar as etapas 1,2 ou 3.
### 1 Limpeza do dataset de treino e teste. 
- Entradas: `input/test_users.csv`, `input/train_users_2.csv`. 
- Saída: `output/users_clean.csv`
```
$ python3 src/clean_dataset.py
```

### 2 Limpeza dos dados de session:
- Entradas: `input/sessions.csv`
- Saída: `output/sessions_clean.csv`
```
$ python3 src/clean_session.py
```

### 3 Treino:
- Entradas: `output/users_clean.csv`, `output/sessions_clean.csv`;
- Saída: `output/users_sessions_clean.csv`, `output/model.p`, `output/labelencoder.p`;
- Configure a variável session=True/False para usar ou não os dados de session;
```
$ python3 src/train.py
```
### 4 Predição:
- Entradas: `output/users_sessions_clean.csv`, `output/model.p`, `output/labelencoder.p`;
- Saída: `output/submission_users.csv` ou `output/submission_users_sessions.csv`;
- Configure a variável session=True/False para usar ou não os dados de session;
```
$ python3 src/predict.py
```
## Resultados:
Geramos dois arquivos de submissão, um utilizando apenas dados de usuários e outro utilizando dados de usuários e sessão.
- Users Only: [submission_users.csv](https://drive.google.com/open?id=1XQbRJOXZklfIyD6e9h4bswNno54BQCSg);
- Users + Sessions: [submission_users_sessions.csv](https://drive.google.com/open?id=1jcdwRISnIFrcbyQeQmPZdsLn4yyqpocJ);

![resultados](https://github.com/AlexandreSGV/cin_am_airbnb/blob/master/docs/resultado_kaggle.png?raw=true)


## Dependências
- pandas
- scikit-learn
- numpy
- xgboost
- pickle
