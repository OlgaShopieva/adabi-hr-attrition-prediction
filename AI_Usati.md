# Dichiarazione sull'utilizzo di strumenti di Intelligenza Artificiale

Questo documento elenca gli strumenti di intelligenza artificiale generativa utilizzati durante lo sviluppo del progetto **"IBM HR Analytics: Previsione del tasso di abbandono dei dipendenti (Attrition)"**, insieme ai prompt principali utilizzati per ciascuno strumento.

---

## 1. Google Gemini 3.5 Flash

**Utilizzo:** generazione di un'immagine illustrativa per la presentazione.

**Prompt:**
```
Generate an image showing employee attrition. One employee is walking away from
the team, representing a worker who is going to leave the company.
```

---

## 2. Claude Sonnet 5

**Utilizzo:** revisione del codice, verifica metodologica, correzione di errori, supporto nella scrittura di funzioni di visualizzazione e nella stesura della documentazione.

### 2.1 Code review e verifica metodologica

**Prompt:**
```
Analyze this Jupyter notebook (classification project) and identify any errors,
inconsistencies, or issues that could be raised. Explain each issue and how to fix it.
```

### 2.2 Correzione di un problema metodologico specifico

**Prompt:**
```
Suggest a correct implementation for threshold selection using cross-validation
on the training set only, ensuring the test set is used exactly once for final
evaluation.
```

### 2.3 Verifica della correttezza del confronto tra modelli

**Prompt:**
```
Is it methodologically valid to compare two classification models when each uses
a different decision threshold? What are the trade-offs?
```

### 2.4 Supporto nella formulazione delle interpretazioni testuali dei risultati

**Prompt:**
```
Given these cross-validation results [list of different thresholds], help me
write a clear analytical paragraph explaining the threshold trade-off in Italian,
consistent with the rest of my notebook's writing style.
```

### 2.5 Aggiornamento della documentazione del progetto (README)

**Prompt:**
```
Update my project README to reflect the corrected results after fixing the
threshold-tuning methodology, and summarize what was changed and why.
```

### 2.6 Visualizzazione e formattazione dell'output dei risultati

**Prompt:**
```
Write a code in Python that plots a confusion matrix and ROC curve side by side
for a classification model, with clean labels and a consistent style.
```

---

## 3. Replit.com

**Utilizzo:** generazione di una presentazione PowerPoint basata sul notebook del progetto.

**Prompt:**
```
This project hr_attrition_income_analysis.ipynb analyzes the IBM HR Analytics
Employee Attrition dataset. The goal is to predict if an employee will leave the
company using machine learning. Create a PowerPoint presentation (.pptx) based on
this notebook. The presentation should have 5 to 10 slides and be written in
Italian. Explain the project in order: objective, dataset, data cleaning, data
analysis, machine learning model, results, and conclusion. Use the charts from
the notebook if possible. Keep the slides simple, with short text and a clean
academic style. Do not invent information. Use only the content available in
the notebook.
```

---

## Nota finale

Gli strumenti di intelligenza artificiale sono stati utilizzati come supporto per il code review, il debug, la scrittura di funzioni ausiliarie (visualizzazione, formattazione dell'output), la consulenza metodologica e la generazione di materiali di supporto (immagine, presentazione). Tutte le decisioni relative alla scelta dei modelli, all'interpretazione dei risultati e alla struttura del progetto sono state prese autonomamente sulla base delle analisi condotte.
