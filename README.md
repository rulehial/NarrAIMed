# NarrAIMed

NarrAIMed es una herramienta que genera informes clínicos narrativos a partir de datos estructurados de pacientes hospitalizados. Utiliza modelos de lenguaje (LLM) para transformar eventos médicos, medicación, resultados de laboratorio y diagnósticos en textos comprensibles y útiles para el personal clínico.

## 🩺 Objetivo

Proveer informes clínicos automatizados, claros y detallados, que ayuden al equipo médico a comprender rápidamente la evolución y estado del paciente.

## 🚀 Características

- Extracción de datos desde MongoDB (eventos clínicos, laboratorio, medicación, CIE10).
- Orquestación con LangGraph y agentes modulares (extracción, análisis, generación).
- Generación de narrativa clínica estructurada usando LLMs.
- Exportación y guardado en formato `.txt`.
- Interfaz gráfica con Streamlit para generación bajo demanda.
- Compatibilidad con GPT-4o vía OpenAI API.

## 🧱 Estructura del Proyecto

```
NarrAIMed/
│
├── config/ # Configuración de la aplicación
├── models/ # Módulos LangGraph (nodos de extracción, análisis, narrativa)
├── db/ # Utilidades de conexión y agregación MongoDB
├── graph/ # Grafo de LLMs
├── llm/ # configuraciones de LLMs
├── narrativas/ # Resultados de las narrativas generadas
├── nodes/ # Módulos LangGraph (nodos de extracción, análisis, narrativa)
├── prompts/ # Prompts para generar lsa narrativas
├── tools/ # Funciones auxiliares (formato, PDF, fechas, etc.)
├── agents/ # Módulos LangGraph (nodos de extracción, análisis, narrativa)
├── .env # Variables de entorno (API Keys, etc.)
├── main.py # Ejecución principal
├── requirements.txt # Dependencias del proyecto
└── README.md
```

## ⚙️ Requisitos

- Python 3.10+
- MongoDB (local o remoto)
- `.env` configurado con: OPENAI_API_KEY=your_key

## 🛠️ Instalación

```bash
# Clona el repositorio
git clone https://github.com/tuusuario/NarrAIMed.git
cd NarrAIMed

# Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

```
## 🧪 Uso
Ejecutar generación directa:
```
python main.py
```

Ejecutar interfaz web:
```
streamlit run main.py
```


## 📁 Ejemplo de salida


#### Se genera un informe clínico como:
---

📄 **Informe Clínico Narrativo**

🧾 **Información del Paciente**
- **Paciente ID:** 3
- **Fecha de Informe:** 27 de junio de 2025
- **Edad:** Neonato
- **Sexo:** Femenino
- **Diagnóstico de Ingreso:** COVID-19 sospecha
- **Fecha de Ingreso:** 09 de abril de 2020
- **Fecha de Alta:** 10 de abril de 2020
- **Motivo de Alta:** Domicilio
- **Respirador:** No

🩺 **Resumen de Ingreso**
El paciente fue ingresado con sospecha de COVID-19. Al momento de ingreso, no se reportaron signos vitales alterados ni síntomas agudos evidentes. La evaluación inicial no mostró la necesidad de soporte respiratorio.

📈 **Eventos Clínicos y Signos Vitales**
- **Eventos Clínicos Registrados:** No se registraron eventos clínicos durante la hospitalización.
- **Signos Vitales:** No se documentaron signos vitales específicos en el historial, lo que sugiere estabilidad durante la estancia hospitalaria.

💊 **Medicación Administrada**
- **Registros de Medicación:** No se registraron medicamentos administrados durante el ingreso.

🧪 **Resultados de Laboratorio**
- **Registros de Laboratorio:** No se realizaron exámenes de laboratorio durante la hospitalización.

📉 **Progresión Clínica**
Durante la hospitalización, el paciente no presentó eventos clínicos significativos, ni se administraron medicamentos, lo que sugiere una evolución estable. La falta de datos clínicos impide establecer una tendencia en el estado del paciente.

✅ **Conclusión y Recomendaciones**
- **Estado General:** El paciente fue ingresado con sospecha de COVID-19, pero no se registraron eventos clínicos, medicación o exámenes de laboratorio, lo que indica que no hubo complicaciones durante su breve estancia hospitalaria.
- **Recomendaciones:** Para futuros ingresos, es crucial registrar cualquier evento clínico, administración de medicamentos y resultados de laboratorio, incluso en pacientes que parecen estables, para proporcionar un seguimiento más completo y facilitar la toma de decisiones clínicas.
---

#### Guardado automáticamente como:

```
narrativas/3_F_24_04_2020_2025_06_26_12_30.txt
```

### 🧠 Créditos

- Desarrollado por [Rubén Hidalgo] para el Trabajo de Fin de Máster - UNIR (Visual Analytics & Big Data).
- Supervisado por el equipo de TFM de la UNIR [María Corina Rodriguez] - [María Paula Jaramillo].
