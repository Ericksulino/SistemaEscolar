import abc

class Materia(abc.ABC):
    def __init__(self,cod,nome,qt_notas):
        self._cod = cod
        self._nome = nome
        self._qt_notas = qt_notas
        self._notas = []
        self._professor = {}
        self._curso = {}
        self._alunos = {}
        self._media = 0.0
    
    @property
    def cod(self):
        return self._cod 


    def atribui_notas(self):
        for i in range(self._qt_notas):
            n = float(input(f"Digite a nota: "))
            self._notas.append(n);
    
    def atribui_curso(self,curs):
        if self._curso == {}:
            self._curso[0] = curs
        else:
            print("Já possui um curso atribuido a disciplina!")
    
    def remov_curso(self):
        del self._curso[0]

    def atribui_professor(self,prof):
        if self._professor == {}:
            self._professor[0] = prof
        else:
            print("Já possui um professor atribuido a disciplina!")
    
    def remov_prof(self):
        del self._professor[0]
        print("Removido com sucesso!")

    def add_alunos(self,aluno):
        self._alunos[aluno.matricula] = aluno
    
    def remov_aluno(self,matri):
        if matri in self._alunos:
            del self._alunos[matri]
            print("Removido com sucesso!")
        else:
            print("Aluno não encontrado!")
    
    def media(self):
        self._media = sum(self._notas)/self._qt_notas
    
    def imprimeNotas(self):
        for i in self._notas:
            print(i)

    def imprimeMedia(self):
        print(f"Média: {self._media}")
    
    def imprimeMateria(self):
        print("...................")
        print(f"Materia: {self._nome}")
        print(f"Código: {self._cod}")
        self.imprime_curso
        print("...................")
    
    def imprime_alunos(self):
        print("-----------------")
        self.imprimeMateria()
        print("Lista de alunos:")
        for key, alu in self._alunos.items():
            alu.imprimir_aluno()
        print("-----------------")
    
    def imprime_prof(self):
        if self._professor == {}:
            print("Professor: ")
            self._professor[0].imprimir_professor()
        else:
            print("Nenhum professor!")
    
    def imprime_curso(self):
        if self._curso == {}:
            print("Curso: ")
            self._curso[0].imprime_curso()
        else:
            print("Nenhum Curso!")
    
        