def matrx_get(matrx,pos):
    return matrx[pos[0]][pos[1]]

def matrx_a_lista(matrx):
    list_final=[]
    list_pos=[]
    pos=[]
    i=0
    j=0
    Break1=False
    for row in matrx:
        if(Break1):
            break
        for cell in row:
            if(cell//10==9):
                pos=[i,j]
                Break1=True
                break
            j+=1
        i+=1
        j=0
    print(pos)
    print(matrx_get(matrx,pos))
    list_pos.append(pos)
    print(list_pos)
    Break2=False
    iter=0
    while not(Break2) and iter<20:
        cell=matrx_get(matrx,pos)
        j=0
        next_pos=pos
        if cell//10 == 1:
            print(pos,'= verde, avanza un espacio')
            j=1
        elif cell//10 ==2:
            print(pos,'= rojo, se detiene 5s y continua ruta')
            j=2
        elif cell//10 == 3:
            print(pos,'= gris, dispara')
            j=3
        elif cell//10 == 4:
            print(pos,'= morado, avanza hasta el final')
            j=4
        elif cell//10 == 9:
            print(pos,'= azul, inicio')
            j=5
        if(j!=4 and j!=0):
            ############
            if cell%10 == 0:
                print(pos,' up')
                if(pos[0]!=0):
                    next_pos[0]-=1
            elif cell%10 ==1:
                print(pos,'right')
                if(pos[1]!=4):
                    next_pos[1]+=1
            elif cell%10 == 2:
                print(pos,' left')
                if(pos[1]!=0):
                    next_pos[1]-=1
            elif cell%10 == 3:
                print(pos,' down')
                if(pos[0]!=4):
                    next_pos[0]+=1
        elif(j==0):
            print(pos," casilla blanca")
            Break2=True
        else:
            if cell%10 == 0:
                print(pos,'all up')
                next_pos[0]=0
            elif cell%10 ==1:
                print(pos,'right')
                next_pos[1]=4
            elif cell%10 == 2:
                print(pos,' left')
                next_pos[1]=0
            elif cell%10 == 3:
                print(pos,' down')
                next_pos[0]=4
        pos=next_pos
        list_pos.append(pos)
        print(list_pos)
        iter+=1
    list_pos.append([5,5])
    print(list_pos)
    return list_final