import pandas as pd 

comentarios = pd.read_csv('./datos/comentarios.txt', sep=r'\|', engine='python', skiprows=[1])
comentarios.columns = comentarios.columns.str.strip()

comentarios["Sentimiento"] = comentarios["Sentimiento"].str.strip()

comentarios_positivos = comentarios[comentarios["Sentimiento"] == "Bueno"]

comentarios_negativos = comentarios[comentarios["Sentimiento"] == "Malo"]


porcentaje_positivo = (comentarios_positivos.shape[0] / comentarios.shape[0]) * 100
porcentaje_negativo = (comentarios_negativos.shape[0] / comentarios.shape[0]) * 100

print("Número de comentarios positivos:", comentarios_positivos.shape[0])
print("Número de comentarios negativos:", comentarios_negativos.shape[0])
print("Porcentaje de comentarios positivos:", porcentaje_positivo,"%")
print("Porcentaje de comentarios negativos:", porcentaje_negativo,"%")