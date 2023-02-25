#Assembler
#Edwin Ortega Kou 22305
#Esteban Zambrano 22119

hexx = input("Ingresar un numero en hexadecimal de 3 digitos: ")
dec = int(hexx, 16)
bin = bin(dec)[2:].zfill(12)

print("La representación de binario de este numero hexadecimal", hexx, "es:", bin)

binn = input("Ingresar un numero en binario de 12 digitos: ")


while len(binn) % 4 != 0:
    binn = '0' + binn

decc = int(binn, 2)

hex = hex(decc)

hex = hex[2:]

print("La conversion de binario de", binn, "a hexadecimal es:", hex)