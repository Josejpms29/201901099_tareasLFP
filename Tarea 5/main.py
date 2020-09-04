cadena_uno = "__servidor1"
cadena_dos = "3servidor"

def ADF(entrada):
    estado = 0
    for i in range(len(entrada)):
        if estado == 0:
            if entrada[i] == "_":
                estado = 1
            elif entrada[i] == str:
                estado = 2
            else:
                print("ERROR, la cadena no es válida")
                return
        elif estado == 1:
            if entrada[i] =="_":
                estado = 1
            elif entrada[i] == int:
                estado = 3
            else:
                print("ERROR, la cadena no es válida")
                return
        elif estado == 2:
            if entrada[i] == str:
                estado == 2
            elif entrada == int:
                estado == 4
            else:
                print("ERROR, la cadena no es válida")
                return
        elif estado == 3:
            if entrada[i] == int:
                estado = 4
            else:
                print("ERROR, la cadena no es válida")
                return
    print("FELICIDADES, la cadena es válida C:")

ADF(cadena_uno)
ADF(cadena_dos)
