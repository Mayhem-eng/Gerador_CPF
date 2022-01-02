from random import randint

valores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

class Gerador_Cpf():
    
    cpf = randint(111111111, 999999999)
    cpf = str(cpf)

    def gerar(self):
        global valores
        
        while True:
            resultado = 0

            for index, cpf in enumerate(self.cpf):
                resultado += int(cpf) * valores[1:][index]
          
            digito = 11 - (resultado % 11)

            if digito > 9:
                self.cpf += "0"
            else:
                self.cpf += str(digito)

            valores.insert(0, 11)

            if len(self.cpf) == 11:
                break

        print(f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}")
        
cpf = Gerador_Cpf()
cpf.gerar()

