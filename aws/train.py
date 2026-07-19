"""
train.py — entry point script for Amazon SageMaker Training Job
Progetto: IBM HR Attrition — Olga Shopieva (ADABI 2025-2026)

Supporta due modelli, scelti tramite l'iperparametro --model-type:
    - logreg : Pipeline(StandardScaler + LogisticRegression)
    - rf     : RandomForestClassifier
"""

import argparse
import os
import joblib
import pandas as pd
import json

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
)


def parse_args():
    parser = argparse.ArgumentParser()

    # Tipo di modello
    parser.add_argument("--model-type", type=str, default="logreg",
                         choices=["logreg", "rf"])

    # Iperparametri Logistic Regression
    parser.add_argument("--max-iter", type=int, default=1000)

    # Iperparametri Random Forest
    parser.add_argument("--n-estimators", type=int, default=300)

    # Soglia di classificazione (threshold), come nel notebook originale
    parser.add_argument("--threshold", type=float, default=0.5)

    # Canali dati e directory SageMaker (SageMaker imposta questi env vars
    # automaticamente; i default qui servono solo per test locali)
    parser.add_argument("--train", type=str,
                         default=os.environ.get("SM_CHANNEL_TRAIN"))
    parser.add_argument("--test", type=str,
                         default=os.environ.get("SM_CHANNEL_TEST"))
    parser.add_argument("--model-dir", type=str,
                         default=os.environ.get("SM_MODEL_DIR"))

    return parser.parse_args()


def load_dataset(channel_dir, filename):
    path = os.path.join(channel_dir, filename)
    df = pd.read_csv(path)
    y = df.iloc[:, 0]
    X = df.iloc[:, 1:]
    return X, y


def build_model(args):
    if args.model_type == "rf":
        return RandomForestClassifier(
            n_estimators=args.n_estimators,
            class_weight="balanced",
            random_state=42,
        )
    # default: logreg
    return Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(
            max_iter=args.max_iter,
            class_weight="balanced",
            random_state=42,
        )),
    ])


def evaluate(model, X_test, y_test, threshold, label):
    y_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_proba >= threshold).astype(int)

    metrics = {
        "model_type": label,
        "threshold": threshold,
        "accuracy": round(accuracy_score(y_test, y_pred), 3),
        "precision": round(precision_score(y_test, y_pred), 3),
        "recall": round(recall_score(y_test, y_pred), 3),
        "f1_score": round(f1_score(y_test, y_pred), 3),
        "roc_auc": round(roc_auc_score(y_test, y_proba), 3),
    }

    print(f"--- {label} (threshold={threshold}) ---")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    return metrics


if __name__ == "__main__":
    args = parse_args()

    X_train, y_train = load_dataset(args.train, "train.csv")

    model = build_model(args)
    model.fit(X_train, y_train)
    print(f"Modello '{args.model_type}' addestrato su {len(X_train)} righe.")

 
    if args.test:
        X_test, y_test = load_dataset(args.test, "test.csv")
        metrics = evaluate(model, X_test, y_test, args.threshold, args.model_type)

        with open(os.path.join(args.model_dir, "metrics.json"), "w") as f:
            json.dump(metrics, f, indent=2)

    # SageMaker si aspetta il modello salvato dentro SM_MODEL_DIR:
    # da li' verra' automaticamente compresso in model.tar.gz e caricato su S3
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))
    print("Modello salvato in:", args.model_dir)
