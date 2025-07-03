from py2neo import Graph, Node, Relationship
from datetime import datetime

# Connessione a Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "Password123"))
graph.delete_all()  # Pulisce il grafo

# Nodi Persona
p1 = Node("Persona", id="P001", nome="Mario", cognome="Rossi", ruolo="CEO", partitaIVA="MRRSSM80A01F205X")
p2 = Node("Persona", id="P002", nome="Luca", cognome="Bianchi", ruolo="CFO", partitaIVA="BNCLCU85B01F205Y")

# Nodi Azienda
az1 = Node("Azienda", id="A001", nome="ACME Srl", settore="Manifattura", partitaIVA="12345678901", indirizzo="Via Roma 1, Milano")

# Nodi Documento (Contratti)
d1 = Node("Documento", id="D001", tipo="Contratto", stato="Attivo", importo=15000, data="2024-05-01")
d2 = Node("Documento", id="D002", tipo="Contratto", stato="Scaduto", importo=8000, data="2023-03-15")
d3 = Node("Documento", id="D003", tipo="Contratto", stato="Attivo", importo=12000, data="2024-02-10")

# Nodi Fattura
f1 = Node("Fattura", id="F001", data="2024-01-20", importo=12000, stato="Pagata")
f2 = Node("Fattura", id="F002", data="2024-03-10", importo=9000, stato="Emessa")

# Nodi IBAN
iban1 = Node("IBAN", id="IB001", iban="IT60X0542811101000000123456")

# Nodi Progetto
prj1 = Node("Progetto", id="PRJ001", nome="Digitalizzazione", descrizione="Progetto di digitalizzazione processi")

# Nodi Email
email1 = Node("Email", id="E001", oggetto="Richiesta supporto", data="2024-04-01", testo="Gentile ACME, ...")

# Nodi Data
data1 = Node("Data", id="DT001", valore="2024-05-01")

# Nodi Indirizzo
ind1 = Node("Indirizzo", id="IND001", via="Via Roma 1", citta="Milano", cap="20100", provincia="MI", nazione="Italia")

# Relazioni principali
r1 = Relationship(p1, "HA_FIRMATO", d1, timestamp=str(datetime.now()), stato="Valido", motivazione="Firma digitale")
r2 = Relationship(p2, "HA_FIRMATO", d2, timestamp=str(datetime.now()), stato="Scaduto", motivazione="Firma cartacea")
r3 = Relationship(p1, "HA_FIRMATO", d3, timestamp=str(datetime.now()), stato="Valido", motivazione="Firma digitale")
r4 = Relationship(d1, "RIFERITO_A", az1)
r5 = Relationship(d2, "RIFERITO_A", az1)
r6 = Relationship(d3, "RIFERITO_A", az1)
r7 = Relationship(f1, "EMESSA_DA", az1)
r8 = Relationship(f2, "EMESSA_DA", az1)
r9 = Relationship(p1, "PARTECIPA_A", prj1)
r10 = Relationship(az1, "USA_IBAN", iban1)
r11 = Relationship(d1, "DATA_FIRMA", data1)
r12 = Relationship(az1, "SEDE_LEGALE", ind1)
r13 = Relationship(email1, "INVIATO_A", p1)

# Caricamento nel grafo
graph.create(p1 | p2 | az1 | d1 | d2 | d3 | f1 | f2 | iban1 | prj1 | email1 | data1 | ind1 |
              r1 | r2 | r3 | r4 | r5 | r6 | r7 | r8 | r9 | r10 | r11 | r12 | r13)

print("Caricamento completato.")
