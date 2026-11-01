# Incident Runbook — Protocolo de Gestión de Incidentes Algorítmicos

## 1. Detección y Clasificación (Detection and Classification)
- **Monitoreo continuo:** Ejecución semanal de compuertas en CI/CD y bitácora de inspecciones en producción.
- **Señales de alarma:**
  - Brecha de Recall (`recall_gap`) > 0.16 entre subgrupos demográficos.
  - Brecha de falsos positivos (`fpr_gap`) > 0.16.
  - Caída de Recall global < 0.68 o tasa de anulación manual por inspectores > 30%.
- **Severidad:** P1 (Crítica: sesgo discriminatorio o falla en contención de PII); P2 (Moderada: aumento de falsos positivos o latencia superior a 500 ms).

## 2. Autoridad de Contención (Containment Authority)
- El **Product Owner** y el **Oficial de Gobernanza de IA** poseen autoridad delegada inmediata para cambiar el estado de producción de `GO` a `REVIEW` o `STOP` sin requerir aprobación de comités directivos.
- En caso de indisponibilidad, el **Lead Data Scientist** puede pausar el servicio de inferencia.

## 3. Preservación de Evidencias (Evidence Preservation)
- Congelar el snapshot del modelo serializado (`models/model.joblib`) y la versión exacta del commit de Git.
- Exportar los registros de predicción, matriz de métricas desagregadas (`fairness_by_group.csv`) y logs de inferencia a un almacenamiento inmutable (`reports/incident_snapshots/`).

## 4. Comunicación Interna y a Partes Afectadas (Communication)
- Notificación interna al equipo técnico y dirección institucional en un plazo < 2 horas.
- Notificación transparente a operadores de campo instruyéndolos a operar bajo el protocolo de contingencia no predictivo.
- En caso de impacto en derechos ciudadanos, publicación de nota aclaratoria conforme a la Ley 107-13 y canalización expedita de apelaciones.

## 5. Reversión a Línea Base Segura (Rollback or Safe Baseline)
- Desactivación inmediata del servicio de predicción algorítmica.
- Activación automática de la **línea base determinista segura**: asignación cronológica de inspecciones (FIFO) combinada con muestreo territorial estratificado por historial de denuncias.

## 6. Postmortem, Responsable y Plazo (Postmortem, Owner and Due Date)
- Responsable de redacción: ML Engineer y Lead Data Scientist.
- Aprobador: Dirección de Gobernanza Institucional.
- Plazo de entrega: Máximo 5 días hábiles tras el incidente.
- Formato: Documentación de causa raíz (RCA), análisis de datos anómalos, acciones preventivas y fecha límite de remediación.
