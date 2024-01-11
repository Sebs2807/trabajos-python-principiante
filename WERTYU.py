def main():
    import sys
    linea = sys.stdin.readline().strip("\n")
    teclas = "‘1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./"
    while linea != "":
        cambiar = ""
        for i in range(len(linea)):
            if linea[i] != " ":
                pos = teclas.index(linea[i])
                cambiar = cambiar + teclas[pos-1]
            else:
                cambiar = cambiar + " "
        print(cambiar)
        linea = sys.stdin.readline().strip("\n")
main()

