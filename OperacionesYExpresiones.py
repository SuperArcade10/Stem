#hola
print("|----------------------------------|")
print("|Bienvenid@ a la calculadora de IMC|")
print("|----------------------------------|")
print("**********")
print("*ATENCIÓN*")
print("**********")
print("|-----------------------------------------------|")
print("|Ingrese los datos sin comas (,) solo puntos (.)|")
print("|-----------------------------------------------|")

#VARIABLES
DatEsta = float(input("Ingrese la estatura en metros: "))
DatPeso = float(input("Ingrese el peso en kilogramos: "))
PBajo = 18.5
PNorm = 24.99
SobrP = 25.00

IMC = DatPeso/(DatEsta**2)

print("Tu IMC es: ", IMC)

if IMC < PBajo:
    print("Peso Bajo: True")
    print("Peso Normal: False")
    print("Sobre Peso: False")
elif IMC < PNorm and IMC > PBajo:
    print("Peso Bajo: False")
    print("Peso Normal: True")
    print("Sobre Peso: False")
elif IMC >= SobrP:
    print("Peso Bajo: False")
    print("Peso Normal: False")
    print("Sobre Peso: True")

print("|-----------------------|")
print("|Gracias por preferirnos|")
print("|-----------------------|")