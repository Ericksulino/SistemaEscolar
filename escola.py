import pessoa
import materia
import curso

class Escola:
    
    def __init__(self):
        self._lista_alunos = {}
        self._lista_professores = {}
        self._lista_materias = {}
        self._lista_cursos = {}

    #Adicionando:

    def adicionar_aluno(self, aluno,codCur):
        if self._lista_cursos != {}:
            if aluno.matricula in self._lista_alunos:
                print("Aluno já cadastrado!")
            else:
                if codCur in self._lista_cursos:
                    self._lista_alunos[aluno.matricula] = aluno
                    self.alu_add_curs(codCur,aluno.matricula)
                    self._lista_alunos[aluno.matricula].adicionar_curso(self._lista_cursos[codCur])
                    print('Aluno cadastrado com sucesso!')
                else:
                    print("Curso não encontrado!")
        else:
            print("Primeiro crie um curso!")

    def adicionar_professor(self, professor,codCur):
        if self._lista_cursos != {}:
            if professor.cpf in self._lista_professores:
                print("Professor já cadastrado!")
            else:
                if codCur in self._lista_cursos:
                    self._lista_professores[professor.cpf] = professor
                    self.prof_add_curs(codCur,professor.cpf)
                    self._lista_professores[professor.cpf].adicionar_curso(self._lista_cursos[codCur])
                    print('Professor cadastrado com sucesso!')
                else:
                    print("Curso não encontrado!")
        else:
            print("Primeiro crie um curso!")

    def adicionar_materia(self, mate,codCur):
        if self._lista_cursos != {}:
            if mate.cod in self._lista_materias:
                print("Disciplina já cadastrada!")
            else:
                if codCur in self._lista_cursos:
                    self._lista_materias[mate.cod] = mate
                    self.disc_add_curs(codCur,mate.cod)
                    self._lista_materias[mate.cod].atribui_curso(self._lista_cursos[codCur])
                    print('Disciplina cadastrada com sucesso!')
                else:
                    print("Curso não encontrado!")
        else:
            print("Primeiro crie um curso!")
    
    def adicionar_curso(self,curso):
        if curso.cod in self._lista_cursos:
            print("Curso já cadastrado!")
        else:
            self._lista_cursos[curso.cod] = curso
            print('Curso criado com sucesso!')

    def alu_add_curs(self,codCur,matri):    
        if codCur in self._lista_cursos:
            if matri in self._lista_alunos:
                self._lista_cursos[codCur].adicionar_aluno(self._lista_alunos[matri])
            else:
                print("Aluno não encontrado!")
        else:
            print("Curso não encontrado!")
    
    def prof_add_curs(self,codCur,cpf):
        if codCur in self._lista_cursos:
            if cpf in self._lista_professores:
                self._lista_cursos[codCur].adicionar_professor(self._lista_professores[cpf])
            else:
                print("Professor não encontrado!")
        else:
            print("Curso não encontrado!")
    
    def disc_add_curs(self,codCur,cod):
        if codCur in self._lista_cursos:
            if cod in self._lista_materias:
               self._lista_cursos[codCur].adicionar_materia(self._lista_materias[cod])
            else:
                print("Disciplina não encontrada!")
        else:
            print("Curso não encontrado!")
    
    def alu_add_materia(self, cod,matri):
        if cod in self._lista_materias:
            if matri in self._lista_alunos:
                self._lista_alunos[matri].adicionar_Disciplina(self._lista_materias[cod])
                self._lista_materias[cod].add_alunos(self._lista_alunos[matri])
                print('Aluno adicionado a Disciplina com sucesso!')
            else:
                print('Aluno não encontrado!')
        else:
            print("Materia não encontrada!")

    def prof_add_materia(self, cod,cpf):
        if cod in self._lista_materias:
            if cpf in self._lista_professores:
                self._lista_professores[cpf].adicionar_Disciplina(self._lista_materias[cod])
                self._lista_materias[cod].atribui_professor(self._lista_professores[cpf])
                print('Professor adicionado a Disciplina com sucesso!')
            else:
                print('Aluno não encontrado!')
        else:
            print("Materia não encontrada!")
    
    def adicionar_notas(self,cod,matri):
        if matri in self._lista_alunos:
                self._lista_alunos[matri].adicionar_notas(cod)
                print('Notas cadastradas com sucesso!')
        else:
            print('Aluno não encontrado!')

    
    #Removendo:

    def remover_aluno(self,matri):
        if matri in self._lista_alunos:
            del self._lista_alunos[matri]
            print("Removido com sucesso!")
        else:
            print("Aluno não encontrado!")
    
    def remover_professor(self,cpf):
        if cpf in self._lista_professores:
            del self._lista_professores[cpf]
            print("Removido com sucesso!")
        else:
            print("Professor não encontrado!")
    
    def remover_disci(self,cod):
        if cod in self._lista_materias:
            del self._lista_materias[cod]
            print("Removido com sucesso!")
        else:
            print("Disciplina não encontrada!")
    
    def remover_curso(self,cod):
        if cod in self._lista_cursos:
            del self._lista_cursos[cod]
            print("Removido com sucesso!")
        else:
            print("Curso não encontrado!")
    
    def remov_alu_curs(self,matri,codCur):
        if codCur in self._lista_cursos:
            if self._lista_cursos[codCur].remover_aluno(matri) == 1:
                self._lista_alunos[matri].remov_curso()
        else:
            print("Curso não encontrado!")
    
    def remov_prof_curs(self,cpf,codCur):
        if codCur in self._lista_cursos:
            if self._lista_cursos[codCur].remover_professor(cpf) == 1:
                self._lista_professores[curso].remov_curso()
        else:
            print("Curso não encontrado!")

    def remov_disc_curs(self,cod,codCur):
        if codCur in self._lista_cursos:
            if self._lista_cursos[codCur].remover_disci(cod) == 1:
                self._lista_materias[cod].remov_curso()
        else:
            print("Curso não encontrado!")
    
    def remov_alu_disc(self,cod,matri):
        if cod in self._lista_materias:
            if matri in self._lista_alunos:
                self._lista_materias[cod].remov_aluno(matri)
                self._lista_alunos[matri].remov_disc(cod)
            else: 
                print("Aluno não encontrado!")
        else:
            print("Disciplina não encontrada!")
    
    def remov_prof_disc(self,cod,cpf):
        if cod in self._lista_materias:
            if cpf in self._lista_professores:
                self._lista_materias[cod].remov_prof()
                self._lista_professores[cpf].remov_disc(cod)
            else:
                 print("Professor não encontrado!")
        else:
            print("Disciplina não encontrada!")

        

    #Buscando:

    def buscar_aluno(self,matri):
        if matri in self._lista_alunos:
            self._lista_alunos[matri].imprimir_aluno()
        else:
            print("Aluno não encontrado!")

    def buscar_professor(self,cpf):
        if cpf in self._lista_professores:
            self._lista_professores[cpf].imprimir_professor()
        else:
            print("Professor não encontrado!")
    
    def buscar_disc(self,cod):
        if cod in self._lista_materias:
            self._lista_materias[cod].imprimeMateria()
        else:
            ("Disciplina não encontrada!")
    
    def buscar_curso(self,cod):
        if cod in self._lista_cursos:
            self._lista_cursos[cod].imprime_curso()
        else:
            print("Curso não encontrado!")
    
    #Exibindo:
    def exibir_boletim(self,matri):
        if matri in self._lista_alunos:
            self._lista_alunos[matri].boletim()
        else:
            print("Aluno não encontrado!")

    def exibir_alunos(self):
        if self._lista_alunos !={}:
            print("\tAlunos:")
            for key, i in self._lista_alunos.items():
                i.imprimir_aluno()
        else:
            print("Nenhum aluno cadastrado!")
    
    def exibir_alunos_disc(self,cod):
        if cod in self._lista_materias:
            self._lista_materias[cod].imprime_alunos()
        else:
            print("Materia não encontrada!")
    
    def exibir_prof_disc(self,cod):
        if cod in self._lista_materias:
            self._lista_materias[cod].imprime_prof()
        else:
            print("Materia não encontrada!")

    def exibir_professores(self):
        if self._lista_professores != {}:
            print("\tProfessores:")
            for key, i in self._lista_professores.items():
                i.imprimir_professor()
        else:
            print("Nenhum professor cadastrado!")
    
    def exibir_disc_prof(self,cpf):
        if self._lista_professores != {}:
            if cpf in self._lista_professores:
                self._lista_professores[cpf].imprimir_disc_prof()
            else:
                print("Professor não encontrado!")
        else:
            print("Nenhum professor cadastrado!")

    def exibir_sal_prof(self,cpf):
        if self._lista_professores != {}:
            if cpf in self._lista_professores:
                self._lista_professores[cpf].imprimir_sal_prof()
            else:
                print("Professor não encontrado!")
        else:
            print("Nenhum professor cadastrado!")   

    def exibir_discipinas(self):
        if self._lista_materias != {}:
            print("\tDisciplinas:")
            for key, i in self._lista_materias.items():
                i.imprimeMateria()
        else:
            print("Nenhuma disciplina cadastrada!")
    
    def exibir_cursos(self):
        if self._lista_cursos != {}:
            print("\tCursos:")
            for key, i in self._lista_cursos.items():
                i.imprime_curso()
        else:
            print("Nenhum curso cadastrado!")
    
    def exibir_al_curs(self,cod):
        if self._lista_cursos != {}:
            if cod in self._lista_cursos:
                self._lista_cursos[cod].imprime_alunos()
            else:
                print("Curso não encontrado!")
        else:
            print("Nenhum curso cadastrado!")
    
    def exibir_prof_curs(self,cod):
        if self._lista_cursos != {}:
            if cod in self._lista_cursos:
                self._lista_cursos[cod].imprime_prof()
            else:
                print("Curso não encontrado!")
        else:
            print("Nenhum curso cadastrado!")
    
    def exibir_disc_curs(self,cod):
        if self._lista_cursos != {}:
            if cod in self._lista_cursos:
                self._lista_cursos[cod].imprime_disc()
            else:
                print("Curso não encontrado!")
        else:
            print("Nenhum curso cadastrado!")

