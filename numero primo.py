def selecionar_numero():
    global numero 
    numero = int(input('digite um numero e veremos se ele é primo'))
    #return numero



def eh_primo(f):
    
    listar_restos =[]
    for i in range(f-1,1,-1):
        resto =(f%i)
        listar_restos.append(resto)

    if 0 in listar_restos:
        print("o numero não é primo")
        return False
    else:
        print("o numero é primo")
        return True
#eh_primo()

def eh_primo2(f):
    
    listar_restos =[]
    for i in range(f-1,1,-1):
        resto =(f%i)
        listar_restos.append(resto)

    if 0 in listar_restos:
        #print("o numero não é primo")
        return False
    else:
        #print("o numero é primo")
        return True

def listar_primos(j):
    for j in range(j,0,-1):
        if eh_primo2(j):
            print(j)

selecionar_numero()
eh_primo(numero)
listar_primos(numero)
