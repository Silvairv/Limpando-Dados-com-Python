import pandas as pd
import numpy as np

df_salarios =  pd.DataFrame({
      'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
      'salario' : [4000, np.nan, 5000, np.nan, 100000]

})
#Calcula a mediana e substitui os nulos pela mediana
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

df_salarios

df_Temperaturas = pd.DataFrame({
    'Dia' : ['Segunda', "Terca", 'Quarta', "Quinta", 'Sexta'],
     'Temperatura': [30, np.nan, np.nan , 28, 27]

})

df_Temperaturas['preenchido_ffill'] = df_Temperaturas['Temperatura'].bfill()
df_Temperaturas

df_cidades = pd.DataFrame({
      'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
       'cidade': ['SP', np.nan, 'Curitiba', np.nan, 'Belem'],
})


df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Nao Informado')
df_cidades
