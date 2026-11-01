# Model Card — complete after LAB13

## Intended use
1. Propósito: Asistencia y soporte a la decisión (DSS) técnica para la priorización preliminar de inspecciones territoriales preventivas de riesgo ambiental y estructural.


2. Modo de operación: Human-in-the-Loop obligatorio. El modelo asigna un puntaje de riesgo indicativo; el inspector técnico humano decide y justifica la inspección de campo.


3. Población objetivo: Unidades territoriales y zonas de infraestructura con reporte de incidentes históricos.

## Out-of-scope use
Prohibida la toma de decisiones automatizadas punitivas, sancionatorias o denegatorias de derechos y servicios públicos sin revisión humana directa (conforme al Art. 4 de la Ley 172-13).
Prohibido su uso para perfilamiento demográfico individual, vigilancia masiva o asignación crediticia/financiera.

## Data and split
1. Dataset: data/territorial_risk_synthetic.csv (640 registros sintéticos con fines didácticos, sin PII ni estadísticas reales de RD).


2. Esquema: Variables categóricas (zone, age_band), numéricas estandarizadas (previous_incidents, infrastructure_score, exposure) y atributos protegidos (protected_group).


3. Partición: Temporal causal estricta (temporal_split con 75% entrenamiento [480 casos] y 25% prueba [160 casos]), garantizando que los datos futuros no contaminen el entrenamiento pasado.

## Global and subgroup evaluation
### Modelo Base (Regresión Logística balanceada):
1. Global: Accuracy = 71.9%, Recall = 71.7%, Precision = 77.6%, FPR = 27.9%.


2. Subgrupo G1: Recall = 65.3% (no cumplía compuerta mínima institucional de 0.68), Selection Rate = 44.6%, FPR = 25.0%.


3. Subgrupo G2: Recall = 79.1%, Selection Rate = 67.8%, FPR = 37.5%.


4. Brechas: Recall Gap = 0.138, FPR Gap = 0.125, Selection Rate Gap = 0.232.


5. Evaluación Interseccional (protected_group 
×
 age_band): Disparidad severa oculta en G1 | 30-44 (Recall = 56.2%) y G2 | 60+ (FPR = 55.6%).
### Modelo Mitigado (ThresholdOptimizer con Fairlearn - Equalized Odds):
1. Recall G1 elevado al 89.8% (protegiendo a la comunidad vulnerable).


2. Brecha de selección reducida drásticamente del 23.2% al 4.6%.


3. Trade-off identificado: Incremento del FPR en G1 al 46.2% (FPR gap = 0.212).

## Green AI evidence
1. Tiempo de entrenamiento: ~0.046 segundos (consumo energético despreciable).


2. Tamaño del modelo: 3.56 KB (ampliamente inferior a la compuerta de 1024 KB).


3. Latencia de inferencia: < 0.15 ms por registro (ampliamente inferior a la compuerta de 500 ms).


4. Arquitectura: Pipeline ligero lineal (Scikit-Learn ColumnTransformer + LogisticRegression), evitando redes neuronales profundas para minimizar la huella de carbono computacional.

## Limitations, human oversight and appeal
1. El optimizador de umbrales genera un trade-off que incrementa las falsas alarmas en G1, requiriendo validación documental previa por parte del analista técnico.


2. Se establece una compuerta de supervisión obligatoria y un muestreo aleatorio del 20% sobre casos descartados para auditar falsos negativos.


3. Mecanismo de apelación ciudadana formal con respuesta en 10 días hábiles bajo la Ley 107-13.
## Owner and review date
#### Dueño Institucional:  Dirección de Gestión de Riesgo Territorial y Comité de Gobernanza de IA.

##### Lead Data Scientist: Lic. Luis Eduardo Puello Ureña.

##### Fecha de auditoría: 01 de noviembre de 2026.

#### Próxima revisión obligatoria: 31 de mayo de 2027 (o semestral).
