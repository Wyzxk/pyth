import pandas as pd
df = pd.read_csv ("C:\\xampp\\htdocs\\py\\csv\\archi.csv", names=["Name","LastNames","Age"])
ordenado = df.sort_values("Age")
ordenadod = df.sort_values("Age",ascending=False)
# print(ordenado)
# print(ordenadod)
concatenando = df.shape
print(concatenando)