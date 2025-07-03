# Definizione dello schema del grafo e delle proprietà principali
# Questo file serve come documentazione e riferimento per la modellazione

# Tipi di nodi:
# - Persona: {id, nome, cognome, ruolo, partitaIVA}
# - Azienda: {id, nome, settore, partitaIVA, indirizzo}
# - Documento: {id, tipo, data, importo, stato}
# - Progetto: {id, nome, descrizione}
# - Fattura: {id, data, importo, stato}
# - IBAN: {id, iban}
# - Email: {id, oggetto, data, testo}
# - Data: {id, valore}
# - Indirizzo: {id, via, citta, cap, provincia, nazione}

# Relazioni principali:
# - HA_FIRMATO: (Persona)-[timestamp, stato, motivazione]->(Documento)
# - RIFERITO_A: (Documento)->(Azienda)
# - EMESSA_DA: (Fattura)->(Azienda)
# - PARTECIPA_A: (Persona)->(Progetto)
# - INVIATO_A: (Email)->(Persona)
# - USA_IBAN: (Azienda)->(IBAN)
# - DATA_FIRMA: (Documento)->(Data)
# - SEDE_LEGALE: (Azienda)->(Indirizzo)

# Normalizzazione:
# - Tutte le entità hanno un id univoco
# - I nomi sono uniformati e non ambigui
# - Le relazioni usano timestamp e stato ove utile

# Esempio di schema:
# (Persona)-[:HA_FIRMATO]->(Documento)-[:RIFERITO_A]->(Azienda)
# (Fattura)-[:EMESSA_DA]->(Azienda)
# (Persona)-[:PARTECIPA_A]->(Progetto)
# (Azienda)-[:USA_IBAN]->(IBAN)
# (Documento)-[:DATA_FIRMA]->(Data)
# (Azienda)-[:SEDE_LEGALE]->(Indirizzo)
