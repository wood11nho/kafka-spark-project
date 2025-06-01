# Real-Time Transaction Monitoring with Kafka & Spark

Acest proiect demonstrează cum putem construi un pipeline Big Data complet pentru detectarea tranzacțiilor financiare mari în timp real, folosind **Apache Kafka** și **Apache Spark (Structured Streaming + SQL)**.

Scenariul simulat: un sistem bancar care monitorizează în timp real tranzacțiile clienților pentru a semnala activitatea suspectă.

---

## ⚙️ Tehnologii utilizate

- **Apache Kafka** – ingestia datelor (streaming)
- **Apache Spark** – procesare și analiză în timp real
- **Spark SQL** – filtrare și interogare a datelor
- **Python** – dezvoltarea aplicațiilor
- **Docker Compose** – orchestrare locală
- **Jupyter Notebook + Matplotlib** – vizualizare output

---

## 🧩 Componente principale

- `producer.py` – trimite mesaje JSON în Kafka (simulează tranzacții aleatorii)
- `spark_app.py` – consumă datele, filtrează tranzacțiile mari (>500) și alertează cele >900
- `docker-compose.yml` – pornește Kafka, Zookeeper și Spark în containere
- `visualize.ipynb` – încarcă fișiere Parquet și generează o histogramă a tranzacțiilor

---

## 🚀 Cum rulezi proiectul

1. **Pornește mediul de lucru**
   ```bash
   docker-compose up -d
   ```

2. **Rulează generatorul de tranzacții**
   ```bash
   python producer.py
   ```

3. **Conectează-te la containerul Spark și rulează aplicația**
   ```bash
   docker exec -it <nume_container_spark> bash
   spark-submit spark_app.py
   ```

4. **(Opțional) Activează scrierea în Parquet în `spark_app.py` pentru a salva datele**
   > În fișierul `spark_app.py`, decomentează secțiunea `df_fraude.writeStream...`

5. **Vizualizează rezultatele în Jupyter**
   ```bash
   jupyter notebook
   ```
   Rulează `visualize.ipynb` pentru a genera o histogramă a tranzacțiilor mari.

---

## 📌 Logica de business

- Tranzacțiile sunt generate cu sume între 1 și 1000.
- Cele >500 RON sunt considerate "mari".
- Cele >900 RON declanșează **alertă în consolă**.
- Datele pot fi salvate în format Parquet pentru analiză ulterioară.

---

## 📈 Exemplu de vizualizare

Graficul generat evidențiază distribuția valorilor tranzacționate peste 500 RON — util pentru analiza anomaliilor sau pragurilor critice.

---

## 🧠 Observații finale

- Proiectul arată cum Kafka și Spark pot colabora pentru un sistem de streaming scalabil.
- Extensii posibile: alertare pe email, stocare în baze de date, integrare cu dashboard-uri live (Grafana).
- Codul este modular și poate fi adaptat ușor la orice alt domeniu unde e nevoie de procesare în timp real.

---

🎓 *Proiect realizat în cadrul cursului Big Data – Master NLP, Universitatea din București, 2025.*

