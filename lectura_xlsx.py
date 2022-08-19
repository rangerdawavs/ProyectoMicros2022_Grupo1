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

#from types import NoneType
import openpyxl , modo_1 , modo_2
from matrx_a_lista_instrucciones import matrx_a_lista
openfile = openpyxl.load_workbook('ejemplos_rutas.xlsx')

list1 , list2 = [],[]
matrx1=[]
test_list=[]
sheet = openfile.get_sheet_by_name('Modo 1')
data = sheet['A1':'E5']
for row in data:
    for cell in row:
        if cell.value == None:
            test_list.append(0)
            list1.append(0)
        else:
            test_list.append(cell.value)
            list1.append(cell.value)
    matrx1.append(test_list)
    test_list=[]
print(matrx1)
print(matrx_a_lista(matrx1))

sheet = openfile.get_sheet_by_name('Modo 2')
data = sheet['A1':'E5']
for row in data:
    for cell in row:
        if cell.value == None:
            list2.append(2)
        else:
            list2.append(cell.value)


print('Datos modo 1 \n\n ',list1,'\n')
print('CASILLA INICIO     ',modo_1.start(list1))
modo_1.color(list1)
modo_1.move(list1)

#print('\n\nDatos modo 2 \n\n ',list2, '\n')
#print('Tamaño lista     ',modo_2.start(list2))'''