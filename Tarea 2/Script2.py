import csv

print('IMPRIMIENDO DATOS DE ARCHIVO CSV')
print('')
with open('archivo2.csv') as file:
    data = csv.reader(file)
    print(type(file))
    for row in data:
        print(row)
print('')