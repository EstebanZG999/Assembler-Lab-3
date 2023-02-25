#Assembler
#Edwin Ortega Kou 22305
#Esteban Zambrano 22119

hex = input("Ingresar un numero en hexadecimal de 3 digitos: ")
dec = int(hex, 16)
bin = bin(dec)[2:].zfill(12)

print("La representación de binario de este numero hexadecimal", hex, "es:", bin)