import abc

class Curso(abc.ABC):
    def __init__(self,nome,cod):
        self._nome = nome
        self._cod = cod
        self._lista_disc = {}
        self._lista_alu = {}
        self._lista_prof = {}

    @property
    def cod(self):
        return self._cod
    
    def adicionar_aluno(self, aluno):
        self._lista_alu[aluno.matricula] = aluno

    def adicionar_professor(self, professor):
        self._lista_prof[professor.cpf] = professor

    def adicionar_materia(self, mate):
        self._lista_disc[mate.cod] = mate

    def imprime_curso(self):
        print("...................")
        print(f"Nome: {self._nome}")
        print(f"Código: {self._cod}")
        print("...................")
        

    def imprime_disc(self):
        if self._lista_disc != {}:
            for key, disc in self._lista_disc.items():
                disc.imprimeMateria()
        else:
            print("Nada cadastrado!")

    def imprime_alunos(self):
        if self._lista_alu !={}:
            for key, alu in self._lista_alu.items():
                alu.imprimir_aluno()
        else:
            print("Nada cadastrado!")
    
    def imprime_prof(self):
        if self._lista_prof != {}:
            for key, prof in self._lista_prof.items():
                prof.imprimir_professor()
        else:
            print("Nada cadastrado!")
    
    def remover_aluno(self,matri):
        if matri in self._lista_alu:
            del self._lista_alu[matri]
            print("Removido com sucesso!")
            return 1
        else:
            print("Aluno não encontrado!")
            return 0
    
    def remover_professor(self,cpf):
        if cpf in self._lista_prof:
            del self._lista_prof[cpf]
            print("Removido com sucesso!")
            return 1
        else:
            print("Professor não encontrado!")
            return 0
    
    def remover_disci(self,cod):
        if cod in self._lista_disc:
            del self._lista_disc[cod]
            print("Removido com sucesso!")
            return 1
        else:
            print("Disciplina não encontrada!")
            return 0
    