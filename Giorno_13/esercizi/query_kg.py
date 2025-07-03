from py2neo import Graph
import openai
import os

# Configurazione Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "Password123"))

# Domanda di business
domanda = "Quali clienti hanno almeno un contratto attivo nel 2024?"

# Query Cypher
cypher = '''
MATCH (p:Persona)-[:HA_FIRMATO]->(d:Documento {tipo: "Contratto", stato: "Attivo"})
WHERE d.data STARTS WITH "2024"
RETURN p.nome AS Nome, p.cognome AS Cognome, d.id AS ContrattoID, d.importo AS Importo, d.data AS Data
'''

# Esecuzione query
risultato = graph.run(cypher).to_table()

# Formattazione tabellare
if risultato:
    header = " | ".join(risultato[0].keys())
    rows = [" | ".join(str(cell) for cell in row.values()) for row in risultato]
    risposta_tabella = header + "\n" + "\n".join(rows)
else:
    risposta_tabella = "Nessun risultato trovato."

# Prompt per LLM
prompt = f"""
Rispondi in linguaggio naturale business alla seguente domanda, usando i dati forniti:
Domanda: {domanda}
Dati:
{risposta_tabella}
"""

# Configurazione OpenAI (inserisci la tua API key)
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...sostituisci...")

# Chiamata a GPT (usa gpt-3.5-turbo o superiore)
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=200,
    temperature=0.2
)

print("Risposta tabellare dalla query:")
print(risposta_tabella)
print("\nRisposta riformulata dal LLM:")
print(response.choices[0].message.content)
