import time

def validar_int(a):
    if isinstance(a, float) and a.is_integer():
        return True
    elif isinstance(a, float):
        return False

def limit_b(n):
    b = (n ** 0.5)
    if validar_int(b) == False:
        b = ((n + 1) ** 0.5)
        if (validar_int(b) == False):
            a_type = validar_int(b)
            x = 1
            while a_type == False:
                b = ((n + x) ** 0.5)
                a_type = validar_int(b)
                x += 1
                #concatenar = n - 1           
            return b
        else:
            return b
    else:
            return b


def limit_a(n):
    a = (n ** 0.5)
    if validar_int(a) == False:
        a = ((n - 1) ** 0.5)
        if (validar_int(a) == False):
            a_type = validar_int(a)
            x = 1
            while a_type == False:
                a = ((n - x) ** 0.5)
                a_type = validar_int(a)
                x += 1
                #concatenar = n - 1           
            return a
        else:
            return a
    else:
            return a

def bissection_str(x, margem_erro=1e-3):
    a = limit_a(x)
    b = limit_b(x)
    if (x**0.5).is_integer():

        meio = (a + b) / 2
        

        while abs(meio**2 - x) > margem_erro:

            if meio**2 < x:
                a = meio
            else:
                b = meio
            
            meio = (a + b) / 2
            # time.sleep(0.5)
            print(meio)

        if meio.is_integer():
            print(f"A raiz de {x} é: {meio}")
    else:
        print(f"As raizes perfeitas mais próximas da raiz de {x} é: {a} e {b}")
        meio = (a + b) / 2
        

        while abs(meio**2 - x) > margem_erro:

            if meio**2 < x:
                a = meio
            else:
                b = meio
            
            meio = (a + b) / 2
            # time.sleep(0.5)
            # print(meio)

        print(f"A raiz aproximada de {x} é: {meio}")

raiz_desejada = int(input("digite o valor da raiz a ser calculada: "))
bissection_str(raiz_desejada)