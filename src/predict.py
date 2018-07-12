import pandas as pd
import numpy as np
import pickle

# define se vai considerar ou não os dados de sessão (abordagem 2)
sessions = True

users_path = '../output/users_clean.csv'
model_path = '../output/model_users.p'
le_path = '../output/labelencoder_users.p'

if(sessions == True):
	users_path = '../output/users_sessions_clean.csv'
	model_path = '../output/model_users_sessions.p'
	le_path = '../output/labelencoder_users_sessions.p'

users_df = pd.read_csv(users_path, index_col=False, low_memory=False) # faz a leitura dos dados de usuários "limpos"
test_users = pd.read_csv("../input/test_users.csv")[['id']] # faz a leitura dos dados de usuários de teste

# leitura do arquivo com o modelo gerado e com os labels encoder

model = pickle.load(open(model_path,'rb'))
le = pickle.load(open(le_path, 'rb'))


test_df = pd.merge(test_users, users_df, on='id') # merge para manter apenas os usuários que serão usados para teste
test_df.set_index('id', inplace=True)
test_df.drop('country_destination', axis=1, inplace=True)
id_list = test_df.index.values

y_pred = model.predict_proba(test_df) # faz a predição utilizando o modelo gerado (calcula a prob. para cada classe)

# gerar a predição de acordo com o formato de submissão do kaggle
ids = []  # lista de ids
paises = []  # lista de paises
for i in range(len(id_list)):
    idx = id_list[i]
    ids += [idx] * 5
    paises += le.inverse_transform(np.argsort(y_pred[i])[::-1])[:5].tolist() # ordena os paises com as maiores probabilidades

# gera arquivo de submissão
print("gerando arquivo de sumbmissão...")
sub = pd.DataFrame(np.column_stack((ids, paises)), columns=['id', 'country'])


if(sessions == True):
	sub.to_csv('../output/submission_users_sessions.csv', index=False)

if(sessions == False):
	sub.to_csv('../output/submission_users.csv', index=False)


print("finish...")

