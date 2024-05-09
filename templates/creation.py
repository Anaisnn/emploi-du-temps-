import psycopg2
conn = psycopg2.connect(
   dbname="postgres",
   user="postgres",
   password="12345",
   host="localhost",
   port=5432
)
def connect():
   try:
       conn = psycopg2.connect(**conn_params)
       return conn
   except psycopg2.Error as e:
       print("Erreur lors de la connexion à la base de données:", e)
       return None


def get_emplois_du_temps(conn):
   try:
       cur = conn.cursor()
       cur.execute("SELECT * FROM emploi_du_temps")
       emplois_du_temps = cur.fetchall()
       cur.close()
       return emplois_du_temps
   except psycopg2.Error as e:
       print("Erreur lors de la récupération des emplois du temps:", e)
       return []