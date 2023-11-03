import psycopg2

# Função com finalidade de executar consultas no Banco de dados postgres através de um parâmetro "consultadb"
def executa_insert(consultadb):
  con= conecta_db('localhost','teste', "postgres", "postgres", 5432)
  cursor = con.cursor()
  cursor.execute(consultadb)
  con.commit() # Envia as variáveis para o db
  con.close() 
  
def executa_fetch(consultadb):

  con = conecta_db('localhost','teste', "postgres", "postgres", 5432)
  cursor = con.cursor()
  cursor.execute(consultadb)
  result = cursor.fetchmany(4)
  con.close() 
  
  print (result)

# Conectar ao database no postgres utilizando o DBeaver
def conecta_db(host, database, user, password, port):
  con = psycopg2.connect(host = host, database = database, user = user,  password=password, port = port)
  return con

# Variáveis para preencher tabela
nome = str(input("Digite o nome: "))
telefone = str(input("Digite o número do telefone: "))
cidade = str(input("Digite a sua cidade: "))
# 'executa_consulta(consulta) para enviar as variáveis para o banco de dados.' 
consulta = str("insert into public.contato(nome, telefone) values('"+nome+"','"+telefone+"')")
executa_insert(consulta)

consulta = str("select * from public.contato")
executa_fetch(consulta)
