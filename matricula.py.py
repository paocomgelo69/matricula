import mysql.connector
	
def getConexao():
	conexao = mysql.connector.connect(user='admin', password ='admin123', database='matricula')

	return conexao


def cadastrarAluno():
	aluno = input('Digite o aluno: ')
	senha = input('Digite a senha: ')
	email = input('Digite o email: ')
	sql = "INSERT INTO matricula (aluno, senha, email) VALUES (%s, %s, %s)"
	val = (aluno, senha, email)
	mycursor.execute(sql, val)
	conexao.commit()
	conexao = getConexao()
	cursor = conexao.cursor()

	while True:
		novoaluno = input('Novo aluno? (S/n)')
		if novoaluno == 'n':
			break
		listaralunos()
		id_aluno = int(input('Informe o ID do aluno ou 0 para novo: '))
		if id_aluno == 0:
			alunos.append(input('aluno: '))
		else:		
			id_alunos.append(id_aluno)

def cadastrarCurso():
	nome = input('Digite o nome: ')
	sql = "INSERT INTO curso (nome) VALUES (%s)"
	val = (nome)
	mycursor.execute(sql, val)
	conexao.commit()

def listarAluno():
	mycursor.execute("SELECT * FROM Alunos")

	myresult = mycursor.fetchall()

	for x in myresult:
  		print(x)

def listarCurso():
	mycursor.execute("SELECT * FROM curso")

	myresult = mycursor.fetchall()

	for x in myresult:
  		print(x)
			
def atualizarAluno():
	mycursor = conexao.cursor()

	id = input('Digite o id: ')
	novo_aluno = input('Digite um novo valor: ')
	nova_senha = input('Digite uma nova senha: ')
	novo_preco = input('Digite um novo email: ')

	sql = 'UPDATE aluno SET nome, senha, email = %s, %s, %s WHERE id = %s'
	values = (novo_aluno, nova_senha, novo_preco)

	mycursor.execute(sql, values)

	mydb.commit()

	print(mycursor.rowcount, "record(s) affected")

def atualizarCurso():

	id = input('Digite o id: ')
	novo_nome = input('Digite um novo nome: ')
	sql = 'UPDATE curso SET nome = %s WHERE id = %s'
	values = (novo_nome)

	mycursor.execute(sql, values)

	mydb.commit()

	print(mycursor.rowcount, "registro(s) afetado")

def apagarAluno():
	
	sql = 'DELETE FROM aluno WHERE id = %s'

	mycursor.execute(sql)

	conexao.commit()

	print(mycursor.rowcount, "registro(s) apagado")

def apagarCurso():

	sql = 'DELETE FROM aluno WHERE id = %s '
	mycursor.execute(sql)

	conexao.commit()

	print(mycursor.rowcount, "registro(s) apagado")

def juntarTabelas():

	sql = "SELECT \
		aluno.nome AS aluno, \
		curso.nome AS curso \
		FROM alunos  \
		INNER JOIN alunos ON aluno.id_curso = curso.id"

	mycursor.execute(sql)

	myresult = mycursor.fetchall()

	for x in myresult:
  		print(x)
		
while True:
	print('1. Cadastrar alunos')
	print('2. Cadastrar curso')
	print('3. Listar alunos')
	print('4. Listar curso')
	print('5. Atualizar alunos')
	print('6. Atualizar curso')
	print('7. Apagar aluno')
	print('8. Apagar curso')
	print('9. Juntar tabelas')
	print('10. break')
	
	opcao = int(input())
	if opcao == 1:
		cadastrarAluno()
	elif opcao == 2:
		cadastrarCurso()
	elif opcao == 3:
		listarAluno()
	elif opcao == 4:
		listarCurso()
	elif opcao == 5:
		atualizarAluno()
	elif opcao == 6:
		atualizarCurso()
	elif opcao == 7:
		apagarAluno()
	elif opcao == 8:
		apagarCurso()
	elif opcao == 9:
		juntarTabelas()
	else:
		print('sair')
		break