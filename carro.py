class Carro ():

    def __init__ (self,consumo,capacidade):
        self.consumo = consumo
        self.capacidade = capacidade
        self.combustivel = 0
        self.km_rodado = 0

    def get_consumo (self,consumo):
        self.consumo = consumo

    def set_consumo (self):
        return self.consumo

    def get_capacidade (self,capacidade):
        self.capacidade = capacidade

    def set_capacidade (self):
        return self.capacidade

    def abastecer (self,litros):
        if (litros + self.combustivel) > self.capacidade:
            print ("Apenas "+str(self.capacidade-self.combustivel)+" Litros foram abastecidos")
            self.combustivel = self.capacidade
        else:
            self.combustivel = litros + self.combustivel

    def gasolina (self):
        return self.combustivel

    def mover (self,km):
        if km > (self.combustivel*self.consumo):
            self.km_rodado = self.km_rodado + (self.combustivel*self.consumo)
            print ("O carro andou apenas "+str(self.consumo*self.combustivel)+" e parou por falta de combustivel")
            self.combustivel = 0
        else:
            self.combustivel = self.combustivel - (km/self.consumo)
            self.km_rodado = self.km_rodado + km

    def get_km_rodado (self):
        return self.km_rodado

consumo = float(input("Entre com o consumo do carro(km/l): "))
capacidade = float(input("Entre com a capacidade do tanque do carro(l): "))

carro = Carro (consumo,capacidade)

opcao = 1

while opcao != 0:
    opcao = int(input("\nEscolha sua opção:\n1 - Checar o nível de combustivel\n2 - Abastecer\n3 - Andar com o carro\n4 - Kilometros rodados\nOutro - Sair:\n"))

    if opcao == 1:
        print (str(carro.gasolina())+" Litros de combustivel")
    elif opcao == 2:
        litros = float(input("Quantos litros serão adicionados:"))
        carro.abastecer(litros)
    elif opcao == 3:
        km = float(input("Quantos km serão percoridos:"))
        carro.mover(km)
    elif opcao == 4:
        print (str(carro.get_km_rodado())+"km rodados")
    else:
        opcao = 0


