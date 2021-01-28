import abc

class Pessoa(abc.ABC):

    def __init__(self, nome, cpf, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._materias = {}
        self._curso = {}

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def materias(self):
        return self._materias

    def adicionar_Disciplina(self,disc):
        self._materias[disc.cod] = disc
    
    def adicionar_curso(self,curs):
        if self._curso == {}:
            self._curso[0] = curs
        else:
            print("Já possui um curso atribuido a pessoa!")
    
    def remov_curso(self):
        del self._curso[0]
    
    def remov_disc(self,cod):
        del self._materias[cod]

    def imprimir_pessoa(self):
        print('Nome: ',self._nome)
        print('CPF: ', self._cpf)
        print('Data de Nascimento: ',self._data_nascimento)
        if self._curso != {}:
            print('Curso: ')
            self._curso[0].imprime_curso()  
        


class Professor(Pessoa):

    def __init__(self, nome, cpf, data_nascimento,hor_aula,val_hor):
        super().__init__(nome, cpf, data_nascimento)
        self._hor_aula = hor_aula
        self._val_hor = val_hor
        self._salario = self._val_hor*self._hor_aula

    def adicionar_Disciplina(self,disc):
        super().adicionar_Disciplina(disc)
    
    def adicionar_curso(self,curs):
        super().adicionar_curso(curs)
    
    def remov_curso(self):
        super().remov_curso()
    
    def remov_disc(self,cod):
        super().remov_disc(cod)

    def imprimir_professor(self):
        print('---------------------------')
        super().imprimir_pessoa()
        print('---------------------------')
    
    def imprimir_disc_prof(self):
        for key, i in self._materias.items():
            i.imprimeMateria()
    
    def imprimir_sal_prof(self):
        print('-------------------')
        print('Salario: ',self._salario)
        print('-------------------')


class Aluno(Pessoa):

    def __init__(self, nome, cpf, data_nascimento,matricula):
        super().__init__(nome, cpf, data_nascimento)
        self._matricula = matricula

    @property
    def matricula(self):
        return self._matricula 
    
    def adicionar_Disciplina(self,disc):
        super().adicionar_Disciplina(disc)
    
    def adicionar_curso(self,curs):
        super().adicionar_curso(curs)
    
    def remov_curso(self):
        super().remov_curso()
    
    def remov_disc(self,cod):
        super().remov_disc(cod)
    
    def adicionar_notas(self,cod):
        self._materias[cod].atribui_notas()
        self._materias[cod].media()
    
    def boletim(self):
        print('-------------------')
        print(f"Aluno: {self._nome}")
        for key, i in self._materias.items():
            print("_________________")
            print(f"Disciplina: ")
            i.imprimeMateria()
            print("Notas: ")
            i.imprimeNotas()
            i.imprimeMedia()
            print("_________________")
        print('-------------------')

    def imprimir_aluno(self):
        print('---------------------------')
        print('Matricula: ',self._matricula)
        super().imprimir_pessoa()
        print('---------------------------')