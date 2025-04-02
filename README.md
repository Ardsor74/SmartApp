# SmartApp

SmartApp è un'applicazione Python che include un calendario, gestione delle spese, automazione per il cellulare e aggiornamento automatico delle notizie sportive.

## Funzionalità

1. **Calendario**: Visualizza il calendario del mese corrente e gestisce eventi.
2. **Gestione delle Spese**: Aggiunge, stampa e salva le spese in un file JSON.
3. **Automazione per il Cellulare**: Invia notifiche al cellulare.
4. **Aggiornamento delle Notizie Sportive**: Esegue il web scraping delle notizie sportive e aggiorna un file HTML.

## Requisiti

Assicurati di avere Python installato sul tuo computer. Puoi scaricarlo da [python.org](https://www.python.org/).

## Installazione

1. Clona il repository:
   ```sh
   git clone https://github.com/Ardsor74/SmartApp.git
   cd SmartApp
   ```

2. Installa le dipendenze richieste:
   ```sh
   pip install requests beautifulsoup4 twilio
   ```

## Utilizzo

1. Esegui il file principale:
   ```sh
   python main.py
   ```

2. **Calendario**:
   - Visualizza il calendario del mese corrente.
   - Aggiungi eventi al calendario modificando il codice in `calendar_app.py`.

3. **Gestione delle Spese**:
   - Aggiungi spese eseguendo `python expenses_app.py`.
   - Le spese verranno salvate automaticamente in `expenses.json`.

4. **Automazione per il Cellulare**:
   - Invia una notifica eseguendo `python automation_app.py`.

5. **Aggiornamento delle Notizie Sportive**:
   - Esegui il web scraping delle notizie sportive e aggiorna il file HTML eseguendo `python ai_news_updater.py`.

## Contribuire

Se desideri contribuire a questo progetto, sentiti libero di fare un fork del repository, creare una nuova branch, apportare le modifiche e inviare una pull request.

## Licenza

Questo progetto è sotto la licenza MIT.