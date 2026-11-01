# Registro de Decisión de Impacto (LAB11)

- **Sistema:** Territorial Review DSS - Synthetic
- **Fecha:** 2026-11-01
- **Responsables (Owners):** Dirección Institucional, Product Owner y Comité de Gobernanza de IA
- **Estado preliminar:** **REVIEW** (Aprobación condicionada a compuertas de equidad y desempeño)

## 1. Evidencia de Impacto
- **Partes interesadas:** Matriz completada en `student_inputs/stakeholders.csv` identificando afectados, operadores técnicos, dueños y equipo de datos.
- **Diferenciación de marcos:**
  - *Obligación Legal:* Cumplimiento de la Ley 172-13 (prohibición de decisiones exclusivamente automáticas; derechos ARCO) y debido proceso administrativo.
  - *Marco Voluntario:* Adopción integral de las funciones *Govern*, *Map*, *Measure* y *Manage* del NIST AI RMF 1.0.
  - *Recomendación Ética:* Principios de justicia distributiva y explicabilidad de la UNESCO (2021) y principios de Green AI.
- **Riesgos priorizados:** 8 escenarios evaluados en `reports/lab11/risk_register_scored.csv`. Los riesgos críticos son:
  - **R02 (Prioridad 9):** [NIST-MAP] Subregistro de incidentes críticos en subgrupos vulnerables (G1).
  - **R01 (Prioridad 8):** [NIST-GOVERN] Automatización punitiva indebida sin Human-in-the-Loop.
  - **R07 (Prioridad 8):** [NIST-MEASURE] Latencia excesiva o huella de carbono computacional.

## 2. Incertidumbre y Mitigación
- Persiste incertidumbre respecto a la disparidad de tasas de falsos positivos y recall entre subgrupos demográficos y edad (`protected_group` y `age_band`).
- Se condiciona el avance a la auditoría algorítmica desagregada con Fairlearn en el LAB12.

## 3. Dictamen y Condiciones de Paso
- **Dictamen:** **REVIEW** (Paso a fase de medición y auditoría algorítmica).
- **Condición resolutoria:** El sistema solo podrá ser desplegado o pilotado si cumple estrictamente las compuertas de calidad (*gates*):
  - `min_recall >= 0.68`
  - `max_recall_gap <= 0.16`
  - `max_fpr_gap <= 0.16`
  - `max_latency_ms <= 500`
  - `max_model_kb <= 1024`
