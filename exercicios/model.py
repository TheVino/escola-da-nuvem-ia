from sklearn.linear_model import LinearRegression
import numpy as np

#Input de dados
horas_de_estudo = np.array([1,2,3,4,5]).reshape(-1,1)
notas = np.array([40,50,60,70,80])

#Treina o modelo
modelo = LinearRegression()
modelo.fit(horas_de_estudo, notas)

#Pergunta ao usuario
horas = float(input("Digite o numero de horas estudadas: "))

#previsao
nota_prevista = modelo.predict([[horas]]) # [[]] is to change the model to 2 axes

print(f"Com {horas} de estudo, a nota prevista eh {nota_prevista[0]:.2f}")