import pandas as pd
import matplotlib.pyplot as plt 

tabela = pd.read_csv("data/acidentes2024.csv", sep=";", encoding="Windows-1252")

estadoDesejado = "PI"
tabelaFiltrada = tabela[tabela["uf"] == estadoDesejado]
print(tabelaFiltrada)

plt.hist(tabelaFiltrada["idade"], bins=20)
plt.title("Distribuição de idades em acidentes no PI")
plt.xlabel("idade")
plt.ylabel("Frequência")
plt.show()
