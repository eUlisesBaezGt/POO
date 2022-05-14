import pandas as pd
nombres= pd.read_csv("ej1repaso.csv")
print(nombres)
prom=nombres["Edad"].mean()
print(prom)