import streamlit as st

# Sample quizzes dictionary
quizzes = {
 "Grundlagen": {
  "questions": [
   {
    "question": "Welches der folgenden Formate ist der Standard für den elektronischen Datenaustausch im Bereich Verwaltung, Handel und Transport?",
    "options": ["ANSI X12", "EDIFACT", "IDOC"],
    "answer": "EDIFACT"
   },
   {
    "question": "Wofür steht die Abkürzung EDI?",
    "options": ["Electronic Device Interface", "Electronic Data Interchange", "Electronic Data Integration"],
    "answer": "Electronic Data Interchange"
   },
   {
    "question": "Welches Datenformat wird hauptsächlich in den USA für den Datenaustausch verwendet?",
    "options": ["VDA", "EDIFACT", "ANSI X12"],
    "answer": "ANSI X12"
   },
   {
    "question": "Welcher Standard wird häufig für den elektronischen Datenaustausch in der deutschen Automobilindustrie verwendet?",
    "options": ["ANSI X12", "VDA", "JSON"],
    "answer": "VDA"
   },
   {
    "question": "Welche Datei-Erweiterung wird typischerweise für CSV-Dateien verwendet?",
    "options": [".csv", ".xml", ".json"],
    "answer": ".csv"
   },
   {
    "question": "Welches Symbol wird in CSV-Dateien häufig als Feldtrenner verwendet?",
    "options": ["Komma", "Semikolon", "Tabulator"],
    "answer": "Komma"
   },
   {
    "question": "Was ist ein Merkmal von XML-Daten?",
    "options": ["Sie sind kommagetrennt", "Sie sind binär codiert", "Sie sind durch Tags strukturiert"],
    "answer": "Sie sind durch Tags strukturiert"
   },
   {
    "question": "Welches Datenformat verwendet geschachtelte Strukturen, um Hierarchien in den Daten darzustellen?",
    "options": ["CSV", "JSON", "Fix-Record"],
    "answer": "JSON"
   },
   {
    "question": "Welches Datenformat wird typischerweise von SAP für den Datenaustausch verwendet?",
    "options": ["XML", "IDOC", "CSV"],
    "answer": "IDOC"
   },
   {
    "question": "Was bedeutet die Kennung „AK“ in einem CSV-Beispiel für EDI?",
    "options": ["Ausdruckskennzeichen", "Auftragskopf", "Ankunftskennzeichen"],
    "answer": "Auftragskopf"
   },
   {
    "question": "Welche Satzart beginnt in einem EDIFACT-Datensatz mit „UNA“?",
    "options": ["Segment-Ende-Zeichen", "Vereinbarung der Sonderzeichen", "Endsatz"],
    "answer": "Vereinbarung der Sonderzeichen"
   },
   {
    "question": "Was zeichnet ein Fix-Record-Format aus?",
    "options": ["Werte sind durch Trennzeichen getrennt", "Werte haben feste Positionen und Längen", "Es verwendet JSON-Strukturen"],
    "answer": "Werte haben feste Positionen und Längen"
   },
   {
    "question": "Was müssen XML-Tags sein?",
    "options": ["Nur Kleinbuchstaben", "Case-sensitive", "Mindestens 5 Zeichen lang"],
    "answer": "Case-sensitive"
   },
   {
    "question": "Für welche Art von Datenaustausch wird das openTRANS-Format verwendet?",
    "options": ["Finanztransaktionen", "Geschäftsdokumente", "Gesundheitsinformationen"],
    "answer": "Geschäftsdokumente"
   },
   {
    "question": "Welcher der folgenden Gründe ist ein Vorteil der Nutzung von JSON?",
    "options": ["Gute Lesbarkeit und einfache Syntax", "Speicherung von Binärdaten", "Verwendung von festen Feldlängen"],
    "answer": "Gute Lesbarkeit und einfache Syntax"
   },
   {
    "question": "Welches Datenformat verwendet das Konzept von \"Objects\" und \"Arrays\" ähnlich wie in Programmiersprachen?",
    "options": ["XML", "JSON", "EDIFACT"],
    "answer": "JSON"
   },
   {
    "question": "Was ist ein „Composite Element“ in EDIFACT?",
    "options": ["Mehrere Felder innerhalb eines Segments", "Ein einzelnes Feld", "Eine Zeilenumbruchsmarkierung"],
    "answer": "Mehrere Felder innerhalb eines Segments"
   },
   {
    "question": "Welches der folgenden Formate ist bekannt für die Nutzung in VDA-Dokumenten?",
    "options": ["EDIFACT", "Fix-Record", "JSON"],
    "answer": "Fix-Record"
   },
   {
    "question": "Welche Kennung beschreibt eine Suppressionsadresse in einer EDIFACT-Nachricht?",
    "options": ["UNA", "NAD+SU", "DTM"],
    "answer": "NAD+SU"
   },
   {
    "question": "Welcher von diesen ist ein gängiger Segmenttyp in einer EDIFACT-Nachricht?",
    "options": ["BEG", "UNH", "EDI"],
    "answer": "UNH"
   }
  ]
 },
  "EDI Know-How": {
    "questions": [
      {
        "question": "Was bedeutet die Abkürzung EDIFACT?",
        "options": [
          "Electronic Data Interchange for Factories",
          "Electronic Data Interchange for Administration, Commerce and Transport",
          "Electronic Data Interchange for Agriculture"
        ],
        "answer": "Electronic Data Interchange for Administration, Commerce and Transport"
      },
      {
        "question": "Welches Segment wird in einer EDI-Nachricht für Währungsinformationen verwendet?",
        "options": [
          "PRI",
          "CUX",
          "NAD"
        ],
        "answer": "CUX"
      },
      {
        "question": "Welche Organisation pflegt das EANCOM-Subset?",
        "options": [
          "ISDN",
          "GS1",
          "ISO"
        ],
        "answer": "GS1"
      },
      {
        "question": "Was ist eine Global Location Number (GLN)?",
        "options": [
          "Eine fortlaufende Nummer für Packstücke",
          "Eine 13-stellige Nummer zur Identifikation von Lokationen",
          "Eine Spezifikation für Nachrichtenformate"
        ],
        "answer": "Eine 13-stellige Nummer zur Identifikation von Lokationen"
      },
      {
        "question": "Welche Nachrichtentyp wird für Bestellungen verwendet?",
        "options": [
          "INVOIC",
          "ORDERS",
          "DESADV"
        ],
        "answer": "ORDERS"
      },
      {
        "question": "Was bedeutet AS2 im Zusammenhang mit EDI?",
        "options": [
          "Applicability Statement 2",
          "Application Server 2",
          "Automated System 2"
        ],
        "answer": "Applicability Statement 2"
      },
      {
        "question": "Welche Information enthält das Segment „BGM” in einer EDI-Nachricht?",
        "options": [
          "Belegnummer und Belegart",
          "Währungsangaben",
          "Lieferantendetails"
        ],
        "answer": "Belegnummer und Belegart"
      },
      {
        "question": "Wie viele Zeichen hat eine GTIN-Nummer?",
        "options": [
          "13",
          "15",
          "18"
        ],
        "answer": "13"
      },
      {
        "question": "Welche Protokolle können für AS2-Kommunikation verwendet werden?",
        "options": [
          "FTP und SFTP",
          "HTTP und HTTPS",
          "SSH und Telnet"
        ],
        "answer": "HTTP und HTTPS"
      },
      {
        "question": "Was ist der Zweck des MIC in der AS2-Kommunikation?",
        "options": [
          "Zertifizierung des Senders",
          "Sicherstellung der Nachrichtenintegrität",
          "Verschlüsselung der Nachricht"
        ],
        "answer": "Sicherstellung der Nachrichtenintegrität"
      },
      {
        "question": "Welches Segment beinhaltet die Empfängeradresse in einer EDI-Nachricht?",
        "options": [
          "IMD",
          "NAD",
          "LIN"
        ],
        "answer": "NAD"
      },
      {
        "question": "Welche Nachricht wird durch das Segment „UNH” in einer EDI-Datei geöffnet?",
        "options": [
          "UNT",
          "ORDERS",
          "NAD"
        ],
        "answer": "ORDERS"
      },
      {
        "question": "Was bedeutet EAN in Bezug auf EDI?",
        "options": [
          "European Article Number",
          "Electronic Address Number",
          "Electronic Allocation Number"
        ],
        "answer": "European Article Number"
      },
      {
        "question": "Was ist ein Hauptmerkmal von X.400 im Zusammenhang mit EDI-Kommunikation?",
        "options": [
          "Eindeutige Adressen und verschlüsselte Verbindung",
          "Schnelle Datenübertragung",
          "Verwendung von SQL-Datenbanken"
        ],
        "answer": "Eindeutige Adressen und verschlüsselte Verbindung"
      },
      {
        "question": "Was beinhaltet eine Nachricht vom Typ „INVOIC”?",
        "options": [
          "Rechnungsinformationen",
          "Versandbenachrichtigungen",
          "Auftragsbestätigungen"
        ],
        "answer": "Rechnungsinformationen"
      }
    ]
  }
}


def display_quiz(quiz_name):
    quiz = quizzes[quiz_name]
    
    user_answers = []
    
    for i, question in enumerate(quiz['questions']):
        st.subheader(f"Q{i + 1}: {question['question']}")
        options = question['options']
        selected_option = st.radio(f"Select your answer:", options, key=f"q{i}")
        user_answers.append(selected_option)
    
    if st.button("Submit"):
        score = 0
        results = []
        for i, question in enumerate(quiz['questions']):
            correct_answer = question['answer']
            user_answer = user_answers[i]
            if user_answer == correct_answer:
                results.append((question['question'], user_answer, 'correct', 'green'))
                score += 1
            elif user_answer == "":
                results.append((question['question'], user_answer, 'missed', 'yellow'))
            else:
                results.append((question['question'], user_answer, 'wrong', 'red'))
                
        st.subheader("Results:")
        for question, answer, status, color in results:
            st.markdown(f"<span style='color: {color};'>{question} - Your Answer: {answer} - Status: {status}</span>", unsafe_allow_html=True)

        st.write(f"Your score: {score}/{len(quiz['questions'])}")

# Streamlit app structure
st.title("Quiz App")
st.sidebar.title("Select a Quiz Topic")
quiz_topic = st.sidebar.selectbox("Choose your quiz:", list(quizzes.keys()))

display_quiz(quiz_topic)