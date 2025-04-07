class Cuadrado:
  def __init__ (self,lado):
    self.lado=lado

def Area (self,lado):
  return self.lado*self.lado

lado= int(input("ingrese un lado: "))
figura=Cuadrado(lado)
r=figura.area()
print(f"el area del cuadrado es: {r}")
