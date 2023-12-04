import matplotlib.pyplot as plt
import pandas as pd

# Conjunto de dados disponível no repositório -> Arquivo: "chuva (1).xlsx"
chuva = pd.read_excel("")

chuva.columns = ("mes", "chuva_2021", "media", "diferenca")
chuva.index = chuva.mes
chuva.drop("mes", axis=1, inplace=True)

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(chuva.media, color='cornflowerblue')
ax.plot(chuva.chuva_2021, color='orangered')
ax.set(title="Comparison between climatology and observed rainfall - 2021",
       ylabel="Preciptation (mm)",
       xlabel="Month")
ax.legend(["Climatology", "Observed rainfall"])
plt.grid(axis='both', which='major', linestyle='-')
fig.show()
