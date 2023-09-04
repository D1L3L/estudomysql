import psycopg2

# Função com finalidade de executar consultas no Banco de dados postgres através de um parâmetro "consultadb"
def executa_consulta(consultadb):
  con= conecta_db()
  cursor = con.cursor()
  cursor.execute(consultadb)
  con.commit() # Envia as variáveis para o db
  con.close() 

# Conectar ao database no postgres utilizando o DBeaver
def conecta_db():
  con = psycopg2.connect(host='localhost', database='teste', user='postgres',  password='postgres', port = 5432)
  return con

# Variáveis para preencher tabela
nome = input("Digite o nome:")
telefone = str(input("Digite o número do telefone:"))

# 'executa_consulta(consulta) para enviar ' 
consulta = str("insert into public.contatos(nome, telefone) values('"+nome+"','"+telefone+"')")
executa_consulta(consulta)
