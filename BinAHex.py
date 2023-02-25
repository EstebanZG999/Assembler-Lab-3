#Assembler
#Edwin Ortega Kou 22305
#Esteban Zambrano 22119

binn = input("Ingresar un numero en binario de 12 digitos: ")


while len(binn) % 4 != 0:
    binn = '0' + binn

dec = int(binn, 2)

hex = hex(dec)

hex = hex[2:]

print("La conversion de binario de", binn, "a hexadecimal es:", hex)
