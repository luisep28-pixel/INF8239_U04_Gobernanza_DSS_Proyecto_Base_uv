# Incident Simulation Postmortem (LAB13)

- **detected_at:** 2026-10-31T18:53:05.422791+00:00
- **signal:** recall gap exceeded (> 0.16) y desviación en tasa de falsos positivos
- **severity:** P2 - Disparidad en calidad de servicio algorítmico
- **containment:** Transición inmediata de estado a `REVIEW` y activación de línea base segura heurística (FIFO)
- **evidence:** Artefactos preservados en `reports/lab13/` (modelos, métricas Fairlearn y commit de control)
- **communication:** Notificación formal emitida a inspectores de campo y dirección técnica en menos de 2 horas. Canal de atención al ciudadano activado para apelaciones
- **corrective_actions:**
  1. Recalibración de umbrales con `ThresholdOptimizer` (Fairlearn) para restablecer la paridad demográfica (Lead Data Scientist - 3 días).
  2. Implementación de compuertas automatizadas de pre-despliegue en CI/CD con bloqueo de merge ante superación de gaps (ML Engineer - 5 días).
  3. Revisión cruzada de casos etiquetados en zonas de subgrupo G1 para corregir subregistro histórico (Data Team y Analista Territorial - 7 días).
