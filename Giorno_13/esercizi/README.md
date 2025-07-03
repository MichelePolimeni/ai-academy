# NER_Graph_G13

Questo progetto dimostra l'integrazione tra un Knowledge Graph Neo4j e un LLM (GPT) per rispondere a domande di business.

## Struttura
- `carica_grafo.py`: Script per caricare dati di esempio nel Knowledge Graph Neo4j.
- `query_kg.py`: Script per porre una domanda, eseguire una query Cypher e passare la risposta a GPT per la riformulazione.
- `README.md`: Istruzioni e spiegazione del progetto.

## Esempio di domanda
"Quali clienti hanno almeno un contratto attivo nel 2024?"

## Requisiti
- Neo4j in esecuzione su localhost
- py2neo
- openai (o altro LLM compatibile)

## Avvio rapido
1. Esegui `carica_grafo.py` per popolare Neo4j.
2. Esegui `query_kg.py` per porre la domanda e ottenere la risposta riformulata.
