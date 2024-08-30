class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self):
        print('Acelerando...V2')

    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinando...')


carro = Carro()
carro.acelerar()


class Uno(Carro):  # Uno está herdando as especificações da classe Carro, evitando códigos duplicados.
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992
    """numero_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self):
        print('Acelerando...')

    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinando...')"""


uno = Uno()
uno.acelerar()
print(uno.numero_rodas)