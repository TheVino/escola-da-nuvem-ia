import math

r = float(input("Insira o raio do circulo: "))
p = math.pi

area = "{:.4f}".format(p * (r**2))


print(f"A area eh {area}")
