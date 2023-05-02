import csv
with open ("C:\\xampp\\htdocs\\py\\csv\\archi.csv") as archivo:
    reader = csv.reader(archivo)
    print(reader)
    for row in reader:
        print(row)