import psycopg2

# Conexão
conn = psycopg2.connect(
    dbname="meu_banco",
    user="meu_usuario",
    password="minha_senha",
    host="localhost",
    port="5432"
)

# Cursor
cur = conn.cursor()

# Nome da tabela ou view
tabela = "minha_tabela"  # ou "minha_view"

# Exportar para CSV
with open("saida.csv", "w", encoding="utf-8") as f:
    cur.copy_expert(f"COPY {tabela} TO STDOUT WITH CSV HEADER DELIMITER ','", f)

# Fechar conexões
cur.close()
conn.close()