import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin123",
  database="matricula"
)

mycursor = mydb.cursor()

print(mydb)

matricula = []


def cadastrarAluno():
    print("cadastrando")
    dados = {"nome": input('Digite o nome')}
    valores = (dados["nome"], )
    sql = "insert into alunos(nome) values (%s, %s, %s)"
    mycursor.execute(sql, valores) 
    mydb.commit()

def cadastrarCurso():
    print("cadastrando")
    dados = {"nome": input('Digite o nome')}
    valores = (dados["nome"], )
    sql = "insert into cursos (nome) values (%s, %s, %s)"
    mycursor.execute(sql, valores) 
    mydb.commit()

def listarAluno():
    print("listar")
    mycursor.execute("SELECT * FROM alunos")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def listarCurso():
    print("listar")
    mycursor.execute("SELECT * FROM cursos")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def deletarAluno():
    id = input("Digite o id")
    valores = (id, )
    sql = "DELETE FROM alunos WHERE id = %s, %s, %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def deletarCurso():
    id = input("Digite o id")
    valores = (id, )
    sql = "DELETE FROM cursos WHERE id = %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def atualizarAluno():
    id = input("Digite o id")
    nome = input("Digite o nome")
    valores = (id, nome, )

    sql = "UPDATE alunos SET nome = %s WHERE id = %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "registro(s) afetado(s)")
    print('cadastrando')
    nome = input('Digite o nome do aluno')
    senha = input('Digite o senha')
    email = input('Digite o email')
    valores = (nome, senha, email, )
    sql = "insert into aluno(nome, senha, email) values (%s, %s, %s)"
    mycursor.execute(sql, valores) 
    mydb.commit()

def atualizarCurso():
    id = input("Digite o id")
    nome = input("Digite o nome")
    valores = (id, nome, )

    sql = "UPDATE curso SET nome = %s WHERE id = %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "registro(s) afetado(s)")
    print('cadastrando')
    nome = input('Digite o nome')
    materia = input('Digite a materia')
    hora = input('Digite a hora do seu curso')
    valores = (nome, materia, hora, )
    sql = "insert into curso(nome, materia, hora) values (%s, %s, %s)"
    mycursor.execute(sql, valores) 
    mydb.commit()

def listarAluno():
    print("listar")
    mycursor.execute("SELECT * FROM aluno")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def listarCurso():
    print("listar")
    mycursor.execute("SELECT * FROM curso")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def deletarAluno():
    id = input("numero do id")
    valores = (id, )
    sql = "DELETE FROM aluno WHERE id = %s, %s, %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def deletarCurso():
    id = input("numero do id")
    valores = (id, )
    sql = "DELETE FROM curso WHERE id = %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def atualizarAluno():
    id = input("Digite o id")
    nome = input("Digite o nome")
    valores = (id, nome, )

    sql = "UPDATE aluno SET nome = %s WHERE id = %s, %s, %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

def atualizarCurso():
    id = input("Digite o id")
    nome = input("Digite o nome")
    valores = (id, nome, )

    sql = "UPDATE aluno SET nome = %s WHERE id = %s"

    mycursor.execute(sql, valores)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

def juntar_tabelas():
    sql= "SELECT \
        aluno.nome AS aluno, \
        curso.nome AS aluno \
        FROM aluno \
        INNER JOIN alunos ON aluno.id_aluno = alunos.nome"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

while True:
    print('1.cadastrar aluno')
    print('2.cadastrar curso')
    print('3.listar aluno')
    print('4.listar curso')
    print('6.deletar aluno')
    print('7.deletar curso')
    print('8.atualizar aluno')
    print('9.atualizar curso')
    print('10.juntar tabelas')
    print('11.break')
    
    if opcao == 1:
        cadastrarAluno()
    elif opcao == 2:
        cadastrarCurso()
    elif opcao == 3:
        listarAluno()
    elif opcao == 4:
        listarCurso()
    elif opcao == 6:
        deletarAluno()
    elif opcao == 7:
        deletarCurso()
    elif opcao == 8:
        atualizarAluno()
    elif opcao == 9:
        atualizarCurso()
    elif opcao == 9:
        apagarAluno()
    elif opcao == 9:
        apagarCurso()
    elif opcao == 10:
        juntarTabelas()
    else: 
        print('exit')
        break 
    
    