import json
from pathlib import Path
import pandas as pd
from fairlearn.postprocessing import ThresholdOptimizer

from inf8239_u04.data import load_data, features, temporal_split
from inf8239_u04.fairness import audit, gap
from inf8239_u04.governance import load_config
from inf8239_u04.model import build_model, fit_measure

def main():
    out = Path("reports/lab12")
    out.mkdir(parents=True, exist_ok=True)
    cfg = load_config()
    gates = cfg["gates"]

    df = load_data()
    train, test = temporal_split(df)
    X_train, y_train = features(train), train.target
    X_test, y_test = features(test), test.target
    sens_train = train.protected_group
    sens_test = test.protected_group

    # 1. Modelo Base (Regresión Logística)
    base_model = build_model("logistic")
    resources_base = fit_measure(base_model, X_train, y_train, "models/logistic.joblib")
    pred_base = base_model.predict(X_test)
    overall_base, groups_base, diff_base = audit(y_test, pred_base, sens_test)

    # 2. Mitigación con Fairlearn ThresholdOptimizer
    # Evaluamos Equalized Odds y TPR Parity (Igualdad de Oportunidades)
    optimizer = ThresholdOptimizer(
        estimator=base_model,
        constraints="equalized_odds",
        prefit=True,
        predict_method="predict_proba",
    )
    optimizer.fit(X_train, y_train, sensitive_features=sens_train)
    pred_mitigated = optimizer.predict(X_test, sensitive_features=sens_test)
    overall_mit, groups_mit, diff_mit = audit(y_test, pred_mitigated, sens_test)

    # Comparativa de métricas
    comparison = pd.DataFrame([
        {
            "version": "Baseline (Logistic)",
            "accuracy": round(float(overall_base["accuracy"]), 3),
            "recall_overall": round(float(overall_base["recall"]), 3),
            "precision_overall": round(float(overall_base["precision"]), 3),
            "recall_G1": round(float(groups_base.loc["G1", "recall"]), 3),
            "recall_G2": round(float(groups_base.loc["G2", "recall"]), 3),
            "recall_gap": round(float(gap(groups_base, "recall")), 3),
            "fpr_gap": round(float(gap(groups_base, "fpr")), 3),
            "selection_rate_gap": round(float(gap(groups_base, "selection_rate")), 3),
            "gate_min_recall": bool(overall_base["recall"] >= gates["min_recall"]),
            "gate_recall_gap": bool(gap(groups_base, "recall") <= gates["max_recall_gap"]),
            "gate_fpr_gap": bool(gap(groups_base, "fpr") <= gates["max_fpr_gap"]),
        },
        {
            "version": "Mitigated (ThresholdOptimizer - EqOdds)",
            "accuracy": round(float(overall_mit["accuracy"]), 3),
            "recall_overall": round(float(overall_mit["recall"]), 3),
            "precision_overall": round(float(overall_mit["precision"]), 3),
            "recall_G1": round(float(groups_mit.loc["G1", "recall"]), 3),
            "recall_G2": round(float(groups_mit.loc["G2", "recall"]), 3),
            "recall_gap": round(float(gap(groups_mit, "recall")), 3),
            "fpr_gap": round(float(gap(groups_mit, "fpr")), 3),
            "selection_rate_gap": round(float(gap(groups_mit, "selection_rate")), 3),
            "gate_min_recall": bool(overall_mit["recall"] >= gates["min_recall"]),
            "gate_recall_gap": bool(gap(groups_mit, "recall") <= gates["max_recall_gap"]),
            "gate_fpr_gap": bool(gap(groups_mit, "fpr") <= gates["max_fpr_gap"]),
        }
    ])

    comparison_path = out / "mitigation_comparison.csv"
    comparison.to_csv(comparison_path, index=False)
    groups_mit.to_csv(out / "mitigated_by_group.csv")

    tradeoff_summary = {
        "analysis": "Trade-off entre Rendimiento Global y Equidad Subgrupal",
        "accuracy_delta": float(overall_mit["accuracy"] - overall_base["accuracy"]),
        "recall_G1_delta": float(groups_mit.loc["G1", "recall"] - groups_base.loc["G1", "recall"]),
        "recall_gap_delta": float(gap(groups_mit, "recall") - gap(groups_base, "recall")),
        "fpr_gap_delta": float(gap(groups_mit, "fpr") - gap(groups_base, "fpr")),
        "baseline": comparison.iloc[0].to_dict(),
        "mitigated": comparison.iloc[1].to_dict(),
    }
    (out / "mitigation_tradeoff.json").write_text(json.dumps(tradeoff_summary, indent=2), encoding="utf-8")

    print("\n=== RESUMEN COMPARATIVO DE MITIGACIÓN (LAB12) ===")
    print(comparison.to_string(index=False))
    print("\nDesglose por grupo mitigado:")
    print(groups_mit[["count", "selection_rate", "recall", "fpr", "accuracy"]].round(3))
    print(f"\nReportes generados en {out}")

if __name__ == "__main__":
    main()
