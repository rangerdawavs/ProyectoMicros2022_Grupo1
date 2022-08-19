def matrx_get(matrx,pos):
    return matrx[pos[0]][pos[1]]

def matrx_a_lista(matrx):
    list_final=[]
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
            j+=1
        i+=1
        j=0
    print(pos)
    print(matrx_get(matrx,pos))
                
    return list_final