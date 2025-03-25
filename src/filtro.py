import pandas as pd

columns = [
    'data_inversa', 'dia_semana', 'horario', 'br', 'km', 'municipio', 
    'causa_acidente', 'tipo_acidente', 'classificacao_acidente', 
    'condicao_metereologica', 'ilesos', 'feridos_leves', 'feridos_graves', 
    'mortos', 'uf'
]

map = {
    1:'janeiro',
    2:'fevereiro',
    3:'março',
    4:'abril',
    5:'maio',
    6:'junho',
    7:'julho',
    8:'agosto',
    9:'setembro',
    10:'outubro',
    11:'novembro',
    12:'dezembro'
}

for i in range(19, 25):
    df = pd.read_csv(f'data/acidentes20{i}.csv', sep=';', encoding='Windows-1252')
    
    df = df.filter(items= columns)
    
    df = df[df['uf'] == 'PI']
    df.drop(columns=['uf'], inplace=True)

    df['data_inversa'] = pd.to_datetime(df['data_inversa'])
    df['ano'] = df['data_inversa'].dt.year
    df['mes'] = df['data_inversa'].dt.month
    df['mes'] = df['mes'].apply(lambda x: map.get(x))
    
    df.to_csv(f'filtered_data/acidentes20{i}_filtrado.csv', sep=';', encoding='utf-8', index=False)


df_2019 = pd.read_csv(f'filtered_data/acidentes2019_filtrado.csv', sep=';')
df_2020 = pd.read_csv(f'filtered_data/acidentes2020_filtrado.csv', sep=';')
df_2021 = pd.read_csv(f'filtered_data/acidentes2021_filtrado.csv', sep=';')
df_2022 = pd.read_csv(f'filtered_data/acidentes2022_filtrado.csv', sep=';')
df_2023 = pd.read_csv(f'filtered_data/acidentes2023_filtrado.csv', sep=';')
df_2024 = pd.read_csv(f'filtered_data/acidentes2024_filtrado.csv', sep=';')

df_full = pd.concat([df_2019, df_2020, df_2021, df_2022, df_2023, df_2024], ignore_index = True)
df_full.to_csv('filtered_data/acidentes_filtrado_full.csv', sep=';', encoding='utf-8', index=False)
