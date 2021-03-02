def bubbleSort(vettore):
    temp = 0

    for j in range(len(vettore)-1):
        for i in range(len(vettore)-j-1):
            if vettore[i] > vettore[i+1] :
                temp = vettore[i]
                vettore[i] = vettore[i+1]
                vettore[i+1] = temp

    return vettore



vettore = [1,3,5,7,9,2,4,6,8,0]

vettore = bubbleSort(vettore)

print(vettore)