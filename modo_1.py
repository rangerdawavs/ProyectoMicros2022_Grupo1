# azul 9 inicio de ruta
# verde 1 caminar un espacio direcci'on indicada
# rojo 2 detener 5s antes de continuar con la ruta
# gris 3 pared, activar disparo
# morado 4 seguir hasta el extremo ignorando el resto de intrucciones
# naranja 5 retroceso de ruta

def start(modo):
    j=0
    for i in modo: 
        if i//10 == 9:
            break
        else:
            j+=1
    return j

def color(modo):
    j=0
    for i in modo: 
        if i !=0:
            if i//10 == 1:
                print(j,'= verde, avanza un espacio')
            elif i//10 ==2:
                print(j,'= rojo, se detiene 5s y continua ruta')
            elif i//10 == 3:
                print(j,'= gris, dispara')
            elif i//10 == 4:
                print(j,'= morado, avanza hasta el final')
            elif i//10 == 9:
                print(j,'= azul, inicio')
        else:
            print(j,)
        j+=1

def move(modo):
    j=0
    for i in modo:
        if i !=0:
            if i%10 == 0:
                print(j,' up')
            elif i%10 ==1:
                print(j,'right')
            elif i%10 == 2:
                print(j,' left')
            elif i%10 == 3:
                print(j,' down')
        else:
            print(j)
        j+=1
