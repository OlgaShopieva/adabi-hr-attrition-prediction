# IBM HR Analytics: Previsione del tasso di abbandono dei dipendenti (Attrition)

## Panoramica del progetto

Questo progetto analizza il dataset IBM HR Analytics sul tasso di abbandono dei dipendenti per risolvere un problema di apprendimento automatico: prevedere se un dipendente lascerà l'azienda. Questo è un problema di Classificazione ML perché prevediamo un'appartenenza a una categoria.

## Dataset

Il dataset contiene record HR anonimizzati, inclusi dati demografici, ruolo lavorativo, punteggi di soddisfazione e dati retributivi.

Variabile target:
- `Attrition` (Sì/No) — target di classificazione

Un campione dei dati è disponibile in `data/WA_Fn-UseC_-HR-Employee-Attrition.csv`.

## Sommario

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
- Logistic Regression (threshold: 0.6)
- Random Forest Classifier (threshold: 0.2)

*Nota: le soglie di decisione sono state ottimizzate indipendentemente per ciascun modello usando cross-validation (5-fold) sul training set, per massimizzare l'F1-score e rendere il confronto equo.*

## Risultati

### 1. Regressione Logistica (threshold = 0.6)

| Metric       | Score |
|:-------------|------:|
| Accuracy     | 0.827 |
| Precision    | 0.467 |
| Recall       | 0.596 |
| F1-score     | **0.523** |
| ROC-AUC      | 0.817 |

---

### 2. Random Forest (threshold = 0.2)

| Metric       | Score |
|:-------------|------:|
| Accuracy     | 0.776 |
| Precision    | 0.383 |
| Recall       | 0.660 |
| F1-score     | **0.484** |
| ROC-AUC      | 0.782 |

---

![Confusion Matrix](images/confusion_matrix.png)

![Feature Importance](images/feature_importance.png)

## Conclusioni e idee per il miglioramento

### Confronto tra i modelli

Quando entrambi i modelli vengono confrontati in modo equo (con soglie di decisione ottimizzate indipendentemente via cross-validation):

- **Random Forest ottiene un recall superiore** (0.660 vs 0.596): identifica il 66% dei dipendenti che effettivamente lasciano l'azienda, rispetto al 59% della Regressione Logistica. In un contesto HR, dove mancare un dipendente a rischio è costoso, questo è un vantaggio significativo.

- **Logistic Regression mantiene una ROC-AUC superiore** (0.817 vs 0.782): mostra una migliore capacità discriminativa generale, indipendente dalla soglia.

- **I punteggi F1 sono comparabili** (0.484 vs 0.523): entrambi i modelli raggiungono un simile equilibrio tra precision e recall.

### Scelta del modello

**Per questo caso d'uso, Random Forest è preferibile** perché il suo recall superiore (0.66 vs 0.596) significa che intercetta più dipendenti a rischio. In un contesto HR, i falsi positivi (segnalare un dipendente che non lascerà) sono meno costosi rispetto ai falsi negativi (perdere l'occasione di intervenire su un dipendente che sta per andarsene).

Tuttavia, Logistic Regression rimane una scelta valida se la priorità è la stabilità complessiva del modello (ROC-AUC superiore).

### Possibili miglioramenti futuri

1. **Tuning degli iperparametri**: usare `GridSearchCV` o `RandomizedSearchCV` per ottimizzare parametri come il numero di alberi del Random Forest, max_depth, ecc.

2. **Provare altri modelli**: ad esempio Gradient Boosting, XGBoost, SVM.

3. **Feature engineering**: creare nuove variabili derivate (es. rapporto tra anni nel ruolo attuale e anni totali di lavoro) che potrebbero catturare meglio il fenomeno.

---
