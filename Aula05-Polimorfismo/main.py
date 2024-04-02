from Categoria import Categoria
from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto

cat1 = Categoria("SUV")
cat2 = Categoria("Esportiva")
cat3 = Categoria("Sedan")

v1 = Veiculo()
v1.imprimir()
print("-----------------")
c1 = Carro("Jeep", 2021, cat1, 4)
c1.imprimir()
print("-----------------")
m1 = Moto("BMW" , 2020 , cat2, 500)
m1.imprimir()