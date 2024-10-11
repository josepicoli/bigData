import pandas as pd

columns = {
            'id', 'pesid', 'sentido_via', 'tracado_via', 'tipo_pista', 'uso_solo',
            'id_veiculo', 'ano_fabricacao_veiculo', 'tipo_envolvido', 'latitude',
            'longitude', 'regional', 'delegacia', 'uop', 'marca', 'fase_dia'
        }

exception = {'pesid', 'id_veiculo', 'ano_fabricacao_veiculo', 'tipo_envolvido', 'marca'}


for i in range(19, 25):
    df = pd.read_csv(f'data/acidentes20{i}.csv', sep=';', encoding='Windows-1252')
    
    if i == 23:
        df.drop(columns= columns.difference(exception), inplace=True)
    else:
        df.drop(columns= columns, inplace=True)
    
    df = df[df['uf'] == 'PI']
    
    df.to_csv(f'filtered_data/acidentes20{i}_filtrado.csv', sep=';', encoding='utf-8', index=False)
