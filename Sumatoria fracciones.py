def sumador4p (a,b):
  """Hace la parte de la sumatoria, donde se suman fracciones 
  (float, float) -> float
  """
  contador = 2
  exponente = 3
  sumador = 0
  while contador <= b:
    x = a ** exponente
    exponente = exponente + 4
    medior = x / contador
    contador = contador + 2
    sumador = sumador + medior

  return sumador

def restador4n (a,b):
  """Hace la parte de la sumatoria, donde se restan fracciones 
  (float, float) -> float
  """

  contador = 1
  exponente = 1
  restador = 0
  while contador <= b:
    x = a ** exponente
    exponente = exponente + 4
    medior = x / contador
    contador = contador + 2
    restador = restador - medior

  return restador

def main():
  """Toma 2 números, el primero será el número sobre el que se hace la sumatoria y el otro hasta que denominador irá
  (float, float) -> float
  """
  a = float(input("Ingrese primer valor"))
  b = float(input("Ingrese segundo valor"))

  return sumador4p(a,b) + restador4n(a,b)
    