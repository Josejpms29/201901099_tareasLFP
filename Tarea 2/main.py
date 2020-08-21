import Script1
import Script2
import Script3

print('------------------------------------------------------------------------------')
print('IMPRIMIENDO DATOS DE ARCHIVO JSON')
print('')
print(type(Script1.data))
for registros in Script1.data['Registros']:
    print('Nombre: ', registros['Nombre: '])
    print('Edad: ', registros['Edad: '])
    print('Genero: ', registros['Genero: '])
    print('Cumpleaños: ', registros['Cumpleaños: '])
    print('')

print('')
print('------------------------------------------------------------------------------')
print('IMPRIMIENDO DATOS DE ARCHIVO XML')
print('')
print(type(Script3.file))

for elements in Script3.root:
    print(elements.text)
