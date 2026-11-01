# INF-8239 · Unidad 04 · Gobernanza y Auditoría de Equidad en DSS Territorial

Sistema de soporte a la decisión (DSS) con supervisión humana obligatoria (*Human-in-the-Loop*) orientado a la priorización preventiva de inspecciones territoriales ante riesgos estructurales y ambientales. El proyecto implementa el marco **NIST AI RMF 1.0**, auditoría algorítmica de equidad desagregada e interseccional con **Fairlearn**, mitigación de sesgos mediante optimización de umbrales (*ThresholdOptimizer*) y compuertas de calidad técnica y sostenibilidad (*Green AI*).

---

## 1. Instrucciones de Ejecución

### Preparación del entorno
```bash
uv sync --frozen
uv run pytest -q
uv run python scripts/check_environment.py
```

### Flujo de auditoría y gobernanza
```bash
# 1. Evaluación de impacto y registro de riesgos (LAB11)
uv run python scripts/lab11_impact.py

# 2. Auditoría algorítmica desagregada e interseccional (LAB12)
uv run python scripts/lab12_audit.py --model logistic
uv run python scripts/lab12_audit.py --model tree

# 3. Mitigación de sesgo y análisis de trade-offs de equidad
uv run python scripts/mitigate_bias.py

# 4. Pipeline de gobernanza y compuertas de despliegue (LAB13)
uv run python scripts/lab13_governance.py

# 5. Interfaz interactiva de supervisión
uv run streamlit run app.py
```

---

## 2. Resumen de Resultados y Dictamen de Gobernanza

### Comparativa de Métricas (Modelo Base vs. Mitigado)

| Métrica / Dimensión | Modelo Base (Logistic) | Mitigado (ThresholdOptimizer - EqOdds) | Impacto / Trade-off |
| :--- | :---: | :---: | :--- |
| **Accuracy Global** | 0.719 | **0.731** | +1.2% en exactitud general |
| **Recall Global** | 0.717 | **0.837** | +12.0% en detección global |
| **Recall Subgrupo G1** | 0.653 *(Incumple < 0.68)* | **0.898** | **+24.5%** (Protege a la comunidad vulnerable) |
| **Brecha de Selección** | 0.232 (23.2%) | **0.046** (4.6%) | Reducción de disparidad de selección al mínimo |
| **FPR Subgrupo G1** | 0.250 | **0.462** | Aumento de falsas alarmas en G1 (Costo del trade-off) |
| **Brecha de FPR (`fpr_gap`)** | 0.125 | **0.212** *(Supera compuerta 0.16)* | Requiere supervisión humana obligatoria |

### Dictamen Institucional: **LIMITAR**
* **Justificación:** Aunque la mitigación resuelve la desatención del subgrupo vulnerable G1 (llevando el Recall a 89.8%), incrementa las falsas alarmas (FPR = 46.2%). No es admisible un despliegue totalmente autónomo (`GO`).
* **Condiciones de operación:**
  1. El sistema opera **exclusivamente como herramienta indicativa** para optimizar rutas de visita de inspectores técnicos.
  2. **Prohibición expresa** de sanciones o actos administrativos automáticos sobre personas o comercios.
  3. Validación de campo obligatoria y muestreo aleatorio de control del 20% sobre casos descartados.
  4. Disponibilidad de canal formal de apelación ciudadana con resolución en 10 días hábiles (Ley 107-13).

---

## 3. Estado de Pruebas Unitarias
* **Suite `pytest`:** 10 de 10 pruebas aprobadas (100% de éxito).
* **Validaciones incluidas:** Contrato de esquema de datos, exclusión estricta de identificadores directos (PII), ponderación de riesgos, acotamiento de brechas de equidad y compuertas de despliegue.

---

## 4. Entregables y Documentación
* **Reporte ejecutivo consolidado para entrega:** [`reports/ENTREGA_EJERCICIO_07_EVALUACION_IMPACTO_AUDITORIA_EQUIDAD.html`](reports/ENTREGA_EJERCICIO_07_EVALUACION_IMPACTO_AUDITORIA_EQUIDAD.html)
* **Declaración de uso ético de IA:** [`docs/AI_USE_DECLARATION.md`](docs/AI_USE_DECLARATION.md)
* **Ficha del modelo (Model Card):** [`docs/MODEL_CARD.md`](docs/MODEL_CARD.md)
* **Protocolo de incidentes (Runbook):** [`docs/RUNBOOK.md`](docs/RUNBOOK.md)
