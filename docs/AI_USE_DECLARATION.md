# Declaración de uso de IA
Estudiante / Autor: Lic. Luis Eduardo Puello Ureña  (Maestría en Inteligencia Artificial, UASD)
Asignatura: INF-8239 · Ciencia de Datos II · Unidad 04
Entorno de desarrollo: Pycharm Gemini 3.8 Flash (High)
Fecha: 01 de noviembre de 2026

## Herramienta y finalidad 

Se utilizó el asistente de inteligencia artificial como Geminis técnico para:

Modelado y Gobernanza: 

Estructuración de matrices de gobernanza conforme a los marcos NIST AI RMF 1.0 (Govern, Map, Measure, Manage) y la delimitación conceptual frente a la legislación dominicana (Ley No. 172-13 sobre Protección de Datos Personales y Ley No. 107-13 sobre Derechos de las Personas ante la Administración Pública).

Auditoría Algorítmica con Fairlearn: Interpretación y desglose de métricas de equidad desagregadas (Paridad Demográfica, Equal Opportunity, Equalized Odds) e interseccionales (protected_group 
×
 age_band).

Mitigación y Trade-Offs: Implementación de técnicas de post-procesamiento (ThresholdOptimizer) para evaluar el impacto en la frontera de eficiencia (Accuracy vs. Disparidad de Recall y FPR).

Depuración de Entorno: Identificación y corrección de sintaxis multilínea en los scripts base de Python.

## Fragmentos afectados verificaciones humanas, 
      
### Dimensiones:
1. Finalidad e Impacto       
2. Riesgos NIST AI RMF
3. Fairness y Desagregación
4. Mitigación de Sesgo
5. Integridad del Pipeline

### Interacciones:
1. Redacción de propósitos, delimitación de usos no permitidos y partes interesadas.
2. Formulación de 8 escenarios mapeados a Govern, Map, Measure y Manage.
3. Ejecución de lab12_audit.py y análisis de brechas grupales e interseccionales.
4. Script scripts/mitigate_bias.py usando ThresholdOptimizer con equalized_odds.
5. Ejecución de la suite completa de pruebas (pytest -q).

### Verificaciónes Humanas Rigurosas Realizadas
1. Se revisó que el sistema quede explícitamente acotado a soporte a la decisión (Human-in-the-Loop) y nunca a decisiones autónomas sancionatorias. Se verificó coherencia con la Ley 172-13.


2. Se calcularon y contrastaron manualmente los puntajes de severidad (
P
=
Probabilidad
×
Impacto
), asegurando que los riesgos residuales reflejen los controles reales.


3. Se verificaron los cálculos de MetricFrame contra los datos crudos del split temporal. Se constató la disparidad crítica en el subgrupo G1 | 30-44 (Recall de solo 56.2%).


4. Se comprobó la reducción de la brecha de selección (de 23.2% a 4.6%) y el aumento de Recall en G1 (a 89.8%), validando el trade-off con el incremento de FPR en G1 (46.2%).


5. Se validó la ejecución de las 10 pruebas unitarias con resultado 100% aprobado (0 fallos).

## Errores detectados y correcciones: 

1. Error detectado en código base: Los scripts scripts/lab11_impact.py y scripts/simulate_incident.py del paquete original presentaban un error de sintaxis SyntaxError: unterminated string literal al usar comillas dobles simples " para cadenas con saltos de línea físicos.


2. Corrección efectuada: Se sustituyeron las comillas por bloques de comillas triples """ estándar de Python (PEP 8), restableciendo la ejecución exitosa de los scripts.