base = float (input("digite a base do triangulo: "))
altura = float (input("digite a altura do triangulo: "))
area = (base*altura)/2
print ("area:", area)

salarioatual=float(input("digite seu salário atual: "))
percentualdereajuste=float(input("digite percentual de reajuste: "))
reajuste=(salarioatual*percentualdereajuste)/100
novosalario=salarioatual+reajuste
print("novo salário: ", novosalario)

altura=float(input("digite a altura do cubo: "))
volume=altura**3
print("volume:", volume)


km=float(input("digite a distância percorrida em km: "))
combustivel=float(input("digite quantos litros foram gastos: "))
consumo=km/combustivel
print("consumo: ",consumo)


comprimento=float(input("digite o comprimento da sala em metros: "))
largura=float(input("digite a largura da sala em metros: "))
preco=float(input("digite o preco do metro quadrado: "))
area=comprimento*largura
custo=area*preco
print("custo: ",custo)


