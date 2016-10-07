import csv
import sys

print "----------------OPCIONES---------------"
print "1. LEER"
print "2. INSERTAR REGISTRO"
print "3. SALIR"

opcion=int(input("QUE ACCION QUIERES REALIZAR? "))

if opcion == 1:
    with open ('registros.csv', 'r') as file:
        data = csv.reader(file, delimiter=',')
        for line in data:
            print line
if opcion == 2:
    nombre = raw_input("INGRESA EL NOMBRE: ")
    telefono = raw_input("INGRESA EL NUMERO TELEFONICO: ")
    email = raw_input("INGRESA EL EMAIL: ")
    with open ('registros.csv','a') as file:
        dat = csv.writer(file, delimiter=",")
        dat.writerow([''+str(nombre), ''+(telefono), ''+(email)])
if opcion == 3:
    sys.exit(0)        