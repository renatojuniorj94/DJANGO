#Usando celular nokia tijolão como exemplo em POO

class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    def fazer_ligações(self):
        print('Fazendo ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Despertando...')

    def calcular(self, v1, v2):
        return v1 + v2

print(Celular.marca)
celular = Celular()
calculado = celular.calcular(2, 4)
print(calculado)