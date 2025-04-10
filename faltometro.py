import os
import pickle

class Disciplina:
    def __init__(self, nome, ch, faltas=0):
        """
        Inicializa uma nova Disciplina.

        - nome : (str) nome da disciplina
        - ch : (int) carga horária total, em horas
        - faltas : (int) faltas até o momento, em horas
        """

        self.nome = nome
        self.ch = int(ch)
        self.faltas = int(faltas)
        # calcula o percentual de presença a partir das faltas e da CH total
        self.presenca = 100 - (self.faltas / self.ch) * 100 
     
    def __str__(self):
        return (f'\n- NOME: {self.nome}\n- CARGA HORÁRIA: {self.ch}h\n- FALTAS: {self.faltas}h\n- PRESENÇA: {self.presenca}%')

def save():
    
    with open('save.txt', 'w') as file:
        file.write(str(disciplinas))

if __name__ == "__main__":

    disciplinas = []

    while True:

        command = input('\n- ADD : adiciona uma nova disciplina\n- SHOW : mostra as disciplinas existentes').upper()

        if command == 'ADD':
            
            nova_disciplina = Disciplina(input("nome?"), input("carga horária?"), input("faltas?"))

            disciplinas.append(nova_disciplina)

            save()

            
        elif command == 'SHOW':
            
            for disciplina in disciplinas:
                print("\n" + disciplinas)       

        elif command == 'LOAD':
            pass 

        else:
            break



