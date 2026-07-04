# IBM HR Analytics: Previsione del tasso di abbandono dei dipendenti (Attrition)

## Panoramica del progetto
Questo progetto analizza il dataset IBM HR Analytics sul tasso di abbandono dei dipendenti per risolvere un problema di apprendimento automatico:   
prevedere se un dipendente lascerà l'azienda (classificazione).

## Dataset
Il dataset contiene record HR anonimizzati, inclusi dati demografici, ruolo lavorativo, punteggi di soddisfazione e dati retributivi.  
Variabile target:  
- `Attrition` (Sì/No) — target di classificazione

Un campione dei dati è disponibile in `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`.  

## Workflow
1. Intro
2. Importazione di librerie e caricamento dei dati
3. Una occhiata alla struttura dei dati
4. Feature pulizia
5. Costruiamo Training e Test set
6. Exploratory Data Analysis - EDA
7. Preprocessing
8. Classificazione - predire Attrition (Sì/No)
9. Conclusioni e idee per il miglioramento



## Modelli usati
**Classification (Attrition):**
- Logistic Regression
- Random Forest Classifier


## Risultati

### Classification — Attrition Prediction
| Metric | Score |
|---|---:|
| Accuracy | X.XX |
| Precision | X.XX |
| Recall | X.XX |
| F1-score | X.XX |

![Confusion Matrix](images/confusion_matrix.png)
![Feature Importance](images/feature_importance.png)
