from Conta import Conta

c = Conta()
if c.saldo != None:
    print( c.saldo )
c.saldo = 2

c.depositar(0.5)
c.sacar(2)

c.setSaldo(100)
print( c.getSaldo() )