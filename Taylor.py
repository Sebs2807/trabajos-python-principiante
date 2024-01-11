#---------------------------Importaciones-------------------------
import sympy
import math
#-----------------------Entradas de datos-------------------------
print("--------Bienvenido al programa que calcula polinomios de taylor-------------")
entrada = (input("Ingrese la función que quiere determinar el polinomio de taylor en terminos de x ")).replace("e","E")
n = abs(int(input("Digite cuantas aproximaciones desea hacer a la función (n) ")))
a = sympy.simplify(input("¿Alrededor de que valor desea el polinomio? "))
#--------------------Función decimal o fracción---------------------
def redondeador(numero):
    """Función que elige si dejar la evaluación de la derivada en fracción o decimal
    (float) -> rational/float
    """
    try:
        numero = sympy.Rational(numero).limit_denominator()
        if numero.denominator > 100000:
            return float(numero.evalf())
        else:
            return numero
    except:
        return numero
#---------------------------Proceso--------------------------------
cont = 0
x = sympy.symbols("x")
f = sympy.sympify(entrada)
derivadas = [redondeador(f.subs(x,a).evalf())]
derivadasi = [f]
factoriales = []
elevados = []
#----------------------Ciclo calcula derivadas y factoriales---------------------
while cont <= n:
    x = sympy.symbols("x")
    derivada = sympy.diff(f,x)
    f = derivada
    derivadas.append(redondeador(f.subs(x,a)))
    derivadasi.append(f)
    factoriales.append(math.factorial(cont))
    elevados.append((x-a))
    cont += 1
final = 0
pregunta = input("¿Desea reemplazar algún valor en específico? (Si/No) ")
#--------------------Impresión al querer reemplazar un valor--------------------
if pregunta.lower() == "si":
    valor = sympy.simplify((input("Valor a reemplazar ").replace(",",".")))
    print("-----------El polinomio de Taylor respectivo es: -----------------")
    for i in range(len(factoriales)):
        print(derivadasi[i],"(",elevados[i],")", "**", i,"/",factoriales[i],end="       ----------->      ")
        print(derivadas[i],"(",elevados[i],")", "**", i,"/",factoriales[i])
        final += ((derivadas[i]*(elevados[i].subs(x,valor)**i)) / factoriales[i])
    print("--------------El valor aproximado de la función es:",final.evalf(),"-----------------------")
    print("El programa ha terminado de ejecutarse. Gracias por utilizar el programa para calcular el polinomio de Taylor. ¡Hasta la próxima!")
#-----------------Impresión al no querer reemplazar un valor------------------ 
else:  
    print("-----------El polinomio de Taylor respectivo es: -----------------")
    for i in range(len(factoriales)):
        print(derivadasi[i],"(",elevados[i],")", "**", i,"/",factoriales[i],end="       ----------->      ")
        print(derivadas[i],"(",elevados[i],")", "**", i,"/",factoriales[i])
    print("El programa ha terminado de ejecutarse. Gracias por utilizar el programa para calcular el polinomio de Taylor. ¡Hasta la próxima!")