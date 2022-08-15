# azul 9 inicio de ruta
# verde 1 caminar un espacio direcci'on indicada
# rojo 2 detener 5s antes de continuar con la ruta
# gris 3 pared, activar disparo
# morado 4 seguir hasta el extremo ignorando el resto de intrucciones
# naranja 5 retroceso de ruta

# 0 up
# 1 right
# 2 left
# 3 down

import openpyxl
openfile = openpyxl.load_workbook('ejemplos_rutas.xlsx')

modo1,modo2 = [],[]

sheet = openfile.get_sheet_by_name('Modo 1')
datos = sheet['A1':'E5']
for row in datos:
    for cell in row:
        modo1.append(cell.value)

sheet = openfile.get_sheet_by_name('Modo 2')
datos = sheet['A1':'E5']
for row in datos:
    for cell in row:
        modo2.append(cell.value)


print('Datos modo 1 \n\n ',modo1,'\n')
print('Tamaño lista     ',len(modo1))
print('\n\nDatos modo 2 \n\n ',modo2, '\n')
print('Tamaño lista     ',len(modo2))