from datetime import datetime, date

class Cliente: 
    def __init__(self, nome, rg, cpf, data_nasc, salario):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.salario = salario

    def setNome (self, nome):
        self.nome = nome

    def setRg (self, rg):
        self.rg = rg

    def setCpf (self, cpf):
        self.cpf = cpf

    def setData_nasc (self, data_nasc):
        self.data_nasc = data_nasc

    def setSalario (self, salario):
        self.salario = salario


    def getNome (self):
        return self.nome
    
    def getRg (self):
        return self.rg

    def getCpf (self):
        return self.cpf

    def getData_nasc (self):
        return self.data_nasc

    def getSalario (self):
        return self.salario

        
    def AvaliaCredito(self):
        idade = datetime.strptime(self.data_nasc, "%d %m %Y")

        def calculate_age(nasc):
            today = date.today()
            return today.year - nasc.year - ((today.month, today.day) < (nasc.month, nasc.day))

        age = calculate_age(idade)

        
        form1 = age * 0.1
        #print(form1)

        form2 = self.salario * 0.3
        #print(form2)

        limite_credito = form1 * form2
        print(limite_credito)


        
Daniel = Cliente('Daniel',123456,963852,'20 6 1995',2000)

print(Daniel.AvaliaCredito())



