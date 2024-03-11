# método que não recebe parâmetro
# e não tem retorno
def imprimirEu():
    print("Nome: Adalto")
    print("Hobby: Vôlei na orla")


# método que não recebe parâmetro
# e tem retorno
def getPi():
    return 3.14

# método que recebe parâmetro
# e não tem retorno
def imprimirAreaCirculo(raio):
    area = calcularAreaCirculo(raio)
    print( "Área do círculo: " , area)

# método que recebe parâmetro
# e tem retorno
def calcularAreaCirculo(raio):
    area = getPi() * ( raio * raio)
    return area

imprimirEu()
imprimirAreaCirculo( 3 )







