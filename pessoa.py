class Pessoa:

    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso =  peso

    def eh_maior(self):
        return self.idade >= 18

    def imc(self):
        return self.peso / (self.altura ** 2)

    def imc_longo(self):
        imc = self.imc()
        if imc < 18.5:
            return 'Abaixo do Peso'
        elif imc < 25.0:
            return 'Peso normal'
        elif imc < 30.0:
            return 'Excesso de peso'
        elif imc < 35.0:
            return 'Obesidade classe I'
        elif imc < 40.0:
            return 'Obesidade classe II'
        else:
            return 'Obesidade classe III'

    def apresentar(self):
        print(f'Muito prazer! Eu me chamo {self.nome} e tenho {self.idade} anos de idade.')
    
    def compara_idade(self, idade):
        if idade < self.idade:
            print(f'{self.nome} é mais velho que esta idade!')
        elif idade > self.idade:
            print(f'{self.nome} é mais novo que esta idade!')
        else:
            print(f'{self.nome} possui esta idade!')

class Atleta(Pessoa):
    def __init__(self, nome, idade, altura, peso, esporte, vitorias):
        super().__init__(nome, idade, altura, peso)
        self.esporte = esporte
        self.vitorias = vitorias
    
    def conquistas(self):
        print(f'{self.nome} já conquistou {self.vitorias} vitórias no(a) {self.esporte}!')

    def apresentar(self):
        print(f'Muito prazer! Eu me chamo {self.nome}, tenho {self.idade} anos de idade e sou um(a) atleta.')
# Testes:

pessoa1=Pessoa('Zezinho', 21 , 1.78, 33.6)
pessoa1.apresentar()
if pessoa1.eh_maior():
    print("É maior de idade!")
else:
    print("É menor de idade!")
print(f"IMC: {pessoa1.imc():.1f}")
print("Classificação:",pessoa1.imc_longo())
pessoa1.compara_idade(21)

print('---')

pessoa2=Pessoa('Luizinho', 17, 1.63, 90.5)
pessoa2.apresentar()
if pessoa2.eh_maior():
    print("É maior de idade!")
else:
    print("É menor de idade!")
print(f"IMC: {pessoa2.imc():.1f}")
print("Classificação:",pessoa2.imc_longo())
pessoa2.compara_idade(16)
print('---')

pessoa1.compara_idade(pessoa2.idade)
print('---')
atleta1 = Atleta("Mariazinha", 25, 1.80, 55.0, "natação", 15)

atleta1.apresentar()
atleta1.conquistas()