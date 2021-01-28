import pessoa
import materia
import escola
import curso

#Menus
def menu():
    op = 0
    while(op!=-1):
        print("\tMENU")
        print(" 1 - Menu Aluno")
        print(" 2 - Menu Professor")
        print(" 3 - Menu Disciplina")
        print(" 4 - Menu Curso")
        print("-1 - Sair")
        try:
            op = int(input("Digite a opção desejada: "))
        except:
            print("Opção invalida!")
        if op == 1:
            menuAlu()
        elif op == 2:
            menuProf()
        elif op == 3:
            menuDisc()
        elif op == 4:
            menuCurs()
        elif(op!=-1): 
            print("Opção invalida!")
        elif(op == -1):
            break

def menuAlu():
    op = 0
    while(op!=-1):
        print("\tMENU ALUNO")
        print(" 1 - Cadastrar Aluno")
        print(" 2 - Adicionar aluno a Disciplina")
        print(" 3 - Ver todos os Alunos")
        print(" 4 - Buscar Aluno")
        print(" 5 - Cadastrar notas")
        print(" 6 - Ver boletim")
        print(" 7 - Remover Aluno")
        print(" 8 - Remover aluno do curso")
        print(" 9 - Adicionar aluno ao Curso")
        print("-1 - Sair")
        try:
            op = int(input("Digite a opção desejada: "))
        except:
            op = 0
            print("Opção invalida!")
        if op == 1:
            cadastrarAluno()
        elif op == 2:
            addAluDisc()
        elif op == 3:
            impriAlunos()
        elif op == 4:
            buscaAluno()
        elif op == 5:
            cadastarNot()
        elif op == 6:
            impriBoletim()
        elif op == 7:
            removAl()
        elif op == 8:
            removAlCurs()
        elif op == 9:
            addAluCurs()
        elif(op!=-1): print("Opção invalida!")

def menuProf():
    op = 0
    while(op!=-1):
        print("\tMENU PROFESSOR")
        print(" 1 - Cadastrar Professor")
        print(" 2 - Adicionar professor a Disciplina")
        print(" 3 - Ver todos os Pofessores")
        print(" 4 - Buscar Professor")
        print(" 5 - Ver Disciplinas do professor")
        print(" 6 - Ver Salario do professor")
        print(" 7 - Remover Professor")
        print(" 8 - Remover professor do Curso")
        print(" 9 - Adicionar professor ao Curso")
        print("-1 - Sair")
        try:
            op = int(input("Digite a opção desejada: "))
        except:
            op = 0
            print("Opção invalida!")
        if op == 1:
            cadastrarProfe()
        elif op == 2:
            addProfDisc()
        elif op == 3:
            impriProfes()
        elif op == 4:
            buscaProfe()
        elif op == 5:
            impriProfDisc()
        elif op == 6:
            impriProfSal()
        elif op == 7:
            removProf()
        elif op == 8:
            removProfCurs()
        elif op == 9:
            addProfCurs()
        elif(op!=-1): print("Opção invalida!")

def menuDisc():
    op = 0
    while(op!=-1):
        print("\tMENU DISCIPLINA")
        print(" 1 - Cadastrar Disciplina")
        print(" 2 - Ver professor da Disciplina")
        print(" 3 - Ver alunos da Disciplina")
        print(" 4 - Ver todas as Disciplinas")
        print(" 5 - Buscar Disciplina")
        print(" 6 - Remover Disciplina")
        print(" 7 - Remover Disciplina do Curso")
        print(" 8 - Adicionar disciplina ao Curso")
        print(" 9 - Remover professor da Disciplina")
        print(" 10 - Remover Aluno da Disciplina")
        print("-1 - Sair")
        try:
            op = int(input("Digite a opção desejada: "))
        except:
            op = 0
            print("Opção invalida!")
        if op == 1:
            cadastarDisc()
        elif op == 2:
            profDisc()
        elif op == 3:
            alunosDisc()
        elif op == 4:
            impriDisc()
        elif op == 5:
            buscDisc()
        elif op == 6:
            removDis()
        elif op == 7:
            removDisCurs()
        elif op == 8:
            addDiscCurs()
        elif op == 9:
            removProfDis()
        elif op == 10:
            removAlDis()
        elif(op!=-1): print("Opção invalida!")

def menuCurs():
    op = 0
    while(op!=-1):
        print("\tMENU CURSO")
        print(" 1 - Cadastrar Curso")
        print(" 2 - Ver professores do Curso")
        print(" 3 - Ver alunos do Curso")
        print(" 4 - Ver disciplinas do Curso")
        print(" 5 - Ver todos os Cursos")
        print(" 6 - Buscar Curso")
        print(" 7 - Remover Curso")
        print("-1 - Sair")
        try:
            op = int(input("Digite a opção desejada: "))
        except:
            op = 0
            print("Opção invalida!")
        if op == 1:
            cadastrarCurs()
        elif op == 2:
            impriProfCurs()
        elif op == 3:
            impriAluCurs()
        elif op == 4:
            impriDiscCurs()
        elif op == 5:
            impriCurs()
        elif op == 6:
            buscaCurs()
        elif op == 7:
            removCurs()
        elif(op!=-1): print("Opção invalida!")

#Cadastros
def cadastrarAluno():
    nome = input("Nome: ")
    cpf = input("Cpf: ")
    datNas = input("Data de nascimento: ")
    matricula = input("Matricula: ")
    codCur = input("Digite o código do curso: ")

    alu = pessoa.Aluno(nome,cpf,datNas,matricula)
    esc.adicionar_aluno(alu,codCur)

def cadastrarProfe():
    nome = input("Nome: ")
    cpf = input("Cpf: ")
    datNas = input("Data de nascimento: ")
    horAu = int(input("Horas de aula: "))
    valHo = int(input("Valor da hora aula: "))
    codCur = input("Digite o código do curso: ")

    prof = pessoa.Professor(nome,cpf,datNas,horAu,valHo)
    esc.adicionar_professor(prof,codCur)

def cadastarDisc():
    nome = input("Nome: ")
    cod = input("Código: ")
    qtNot = int(input("Quantidade de notas: "))
    codCur = input("Digite o código do curso: ")

    disc = materia.Materia(cod,nome,qtNot)
    esc.adicionar_materia(disc,codCur)

def cadastrarCurs():
    nome = input("Nome: ")
    cod = input("Código: ")

    curs = curso.Curso(nome,cod)
    esc.adicionar_curso(curs)


def cadastarNot():
    matri = input("Digite a matricula do aluno: ")
    cod = input("Digite o código da disciplina: ")
    esc.adicionar_notas(cod,matri)

#Adicionar a
def addAluDisc():
    matri = input('Digite a matricula do aluno: ')
    cod = input('Digite o código da disciplina: ')

    esc.alu_add_materia(cod,matri)

def addProfDisc():
    cpf = input('Digite o cpf do professor: ')
    cod = input('Digite o código da disciplina: ')

    esc.prof_add_materia(cod,cpf)

def addAluCurs():
    matri = input('Digite a matricula do aluno: ')
    cod = input('Digite o código do curso: ')
    esc.alu_add_curs(cod,matri)

def addProfCurs():
    cpf = input('Digite o cpf do professor: ')
    cod = input('Digite o código do curso: ')
    esc.prof_add_curs(cod,cpf)

def addDiscCurs():
    cod = input('Digite o código da disciplina: ')
    codCur = input('Digite o código do curso: ')
    esc.disc_add_curs(codCur,cod)

#Impressão de dados
def impriAlunos():
    esc.exibir_alunos()

def impriProfes():
    esc.exibir_professores()

def impriDisc():
    esc.exibir_discipinas()

def impriBoletim():
    matri = input("Digite a matricula do aluno: ")
    esc.exibir_boletim(matri)

def impriProfDisc():
    cpf = input("Digite o cpf do professor: ")
    esc.exibir_disc_prof(cpf)

def impriProfSal():
    cpf = input("Digite o cpf do professor: ")
    esc.exibir_sal_prof(cpf)

def impriCurs():
    esc.exibir_cursos()

def impriAluCurs():
    cod = input("Digite o código do curso: ")
    esc.exibir_al_curs(cod)

def impriProfCurs():
    cod = input("Digite o código do curso: ")
    esc.exibir_prof_curs(cod)

def impriDiscCurs():
    cod = input("Digite o código do curso: ")
    esc.exibir_disc_curs(cod)

#Buscas:
def buscaAluno():
    matri = input("Digite a matricula do aluno: ")
    esc.buscar_aluno(matri)

def buscaProfe():
    cpf = input("Digite o cpf do professor: ")
    esc.buscar_professor(cpf)

def buscDisc():
    cod = input("Digite o codigo da disciplina: ")
    esc.buscar_disc(cod)

def alunosDisc():
    cod = input("Digite o codigo da disciplina: ")
    esc.exibir_alunos_disc(cod)

def profDisc():
    cod = input("Digite o codigo da disciplina: ")
    esc.exibir_prof_disc(cod)

def buscaCurs():
    cod = input("Digite o código do curso: ")
    esc.buscar_curso(cod)

#Removendo:
def removAl():
    matri = input("Digite a matricula do aluno: ")
    esc.remover_aluno(matri)

def removProf():
    cpf = input("Digite o cpf do professor: ")
    esc.remover_professor(cpf)

def removDis():
    cod = input("Digite o código da disciplina: ")
    esc.remover_disci(cod)

def removCurs():
    cod = input("Digite o código do curso: ")
    esc.remover_curso(cod)

def removAlCurs():
    matri = input("Digite a matricula do aluno: ")
    cod = input("Digite o código do curso: ")
    esc.remov_alu_curs(matri,cod)

def removProfCurs():
    cpf = input("Digite o cpf do professor: ")
    cod = input("Digite o código do curso: ")
    esc.remov_prof_curs(cpf,cod)

def removDisCurs():
    cod = input("Digite o código da disciplina: ")
    codCur = input("Digite o código do curso: ")
    esc.remov_disc_curs(cod,codCur)

def removAlDis():
    cod = input("Digite o código da disciplina: ")
    matri = input("Digite a matricula do aluno: ")
    esc.remov_alu_disc(cod,matri)

def removProfDis():
    cod = input("Digite o código da disciplina: ")
    cpf = input("Digite o cpf do professor: ")
    esc.remov_prof_disc(cod,cpf)



esc = escola.Escola()
menu()