class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def obter_detalhes(self):
        return f"Curso: {self.nome}\nDuração: {self.duracao} anos"


class Presencial(Curso):
    def __init__(self, nome, duracao, numero_de_salas):
        super().__init__(nome, duracao)
        self.numero_de_salas = numero_de_salas

    def obter_detalhes(self):
        return f"{super().obter_detalhes()}\nNúmero de Salas Presenciais: {self.numero_de_salas}"


class Online(Curso):
    def __init__(self, nome, duracao, plataforma_online):
        super().__init__(nome, duracao)
        self.plataforma_online = plataforma_online

    def obter_detalhes(self):
        return f"{super().obter_detalhes()}\nPlataforma Online: {self.plataforma_online}"


# Criando instâncias
curso_presencial = Presencial("Arquitetura Presencial", 4, 50)
curso_online = Online("Desenvolvimento Web Online", 1, "Plataforma ABC")

# Imprimindo informações
print(curso_presencial.obter_detalhes())
print("\n")
print(curso_online.obter_detalhes())