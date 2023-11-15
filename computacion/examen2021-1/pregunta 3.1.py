import sys

def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if int(array[j][1]) < int(array[j + 1][1]):

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break


lineas=[]
for line in sys.stdin:
    if line=="\n":
        break
    lineas+=[line.strip("\n")]

for i in range(0,len(lineas)):
    lineas[i]=lineas[i].split(" ")


n_participantes=int(lineas[0][0])
n_eventos=n_participantes/8
lineas=lineas[1:]


#mandarlo a ordenar 
print(lineas)

bubbleSort(lineas)
print(lineas)

#Ahora ya ordenados

#print("len",len(lineas))
a=[]
b=[]
#orden de las pistas 4-5-3-6-2-7-1-8    
orden=[4,5,3,6,2,7,1,8]
count_orden=0
for i in range(len(lineas)):
    #   esquema A
    a.insert(orden[i%8]-1,lineas[i][0])

    #    esquema B
    b.insert(orden[i%8]+8*count_orden,lineas[i][0])
    if count_orden < n_eventos:
        count_orden+=1
    else:
        count_orden=0
print(" ".join(a))
print(" ".join(b))



"""
16
16 945258
5 974925
6 1025304
1 988751
8 945030
2 999421
14 955708
3 1031388
13 1007447
11 981563
10 969338
15 1029284
4 1055499
12 963144
7 980324
9 941296
"""