def start(modo):
    j=0
    for i in modo: 
        if i//9 == 1:
            break
        else:
            j+=1
    return j