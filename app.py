import streamlit as st

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Sistema Experto Cardiovascular",
    page_icon="🫀",
    layout="centered"
)

# ==========================================
# BASE DE REGLAS
# ==========================================
reglas = [
    {"id": "Regla 1", "descripcion": "Edad>60 + Colesterol Alto + Presión Muy elevada",
     "condicion": lambda h, r_e: r_e==">60" and h['colesterol']=="Alto" and h['presion']=="Muy elevada",
     "nivel": "Alto"},
    {"id": "Regla 2", "descripcion": "Edad 45-60 + Colesterol Medio/Alto + Glucosa Elevada",
     "condicion": lambda h, r_e: r_e=="45-60" and h['colesterol'] in ["Medio","Alto"] and h['glucosa']=="Elevada",
     "nivel": "Medio"},
    {"id": "Regla 3", "descripcion": "Dolor intenso + ECG Anormal",
     "condicion": lambda h, _: h['dolor_pecho']=="Intenso" and h['ecg']=="Anormal",
     "nivel": "Alto"},
    {"id": "Regla 4", "descripcion": "Angina inducida + Frecuencia Máxima Alta",
     "condicion": lambda h, _: h['angina']=="Sí" and h['frecuencia_max']=="Alta",
     "nivel": "Alto"},
    {"id": "Regla 5", "descripcion": "ST inducida por ejercicio significativa",
     "condicion": lambda h, _: h['st_ejercicio']=="Significativa",
     "nivel": "Alto"},
    {"id": "Regla 6", "descripcion": "Dolor moderado + Colesterol Medio",
     "condicion": lambda h, _: h['dolor_pecho']=="Moderado" and h['colesterol']=="Medio",
     "nivel": "Medio"},
    {"id": "Regla 7", "descripcion": "Edad<45 + Presión Normal + Colesterol Bajo",
     "condicion": lambda h, r_e: r_e=="<45" and h['presion']=="Normal" and h['colesterol']=="Bajo",
     "nivel": "Bajo"},
    {"id": "Regla 8", "descripcion": "ECG Normal + ST 'No lo sé'",
     "condicion": lambda h, _: h['ecg']=="Normal" and h['st_ejercicio']=="No lo sé",
     "nivel": "Medio"},
    {"id": "Regla 9", "descripcion": "Sin angina + Dolor Ausente",
     "condicion": lambda h, _: h['angina']=="No" and h['dolor_pecho']=="Ausente",
     "nivel": "Bajo"},
    {"id": "Regla 10", "descripcion": "Frecuencia Media + Presión Ligeramente elevada",
     "condicion": lambda h, _: h['frecuencia_max']=="Media" and h['presion']=="Ligeramente elevada",
     "nivel": "Medio"},
    {"id": "Regla 11", "descripcion": "Dolor Leve + Edad 45-60",
     "condicion": lambda h, r_e: h['dolor_pecho']=="Leve" and r_e=="45-60",
     "nivel": "Medio"},
    {"id": "Regla 12", "descripcion": "Dolor Intenso + ST Significativa",
     "condicion": lambda h, _: h['dolor_pecho']=="Intenso" and h['st_ejercicio']=="Significativa",
     "nivel": "Alto"},
    {"id": "Regla 13", "descripcion": "Colesterol Alto + Glucosa Elevada",
     "condicion": lambda h, _: h['colesterol']=="Alto" and h['glucosa']=="Elevada",
     "nivel": "Alto"},
    {"id": "Regla 14", "descripcion": "Edad>60 + Presión Ligeramente elevada",
     "condicion": lambda h, r_e: r_e==">60" and h['presion']=="Ligeramente elevada",
     "nivel": "Medio"},
    {"id": "Regla 15", "descripcion": "ECG Anormal + Dolor Moderado",
     "condicion": lambda h, _: h['ecg']=="Anormal" and h['dolor_pecho']=="Moderado",
     "nivel": "Medio"},
    {"id": "Regla 16", "descripcion": "Angina Sí + Edad 45-60",
     "condicion": lambda h, r_e: h['angina']=="Sí" and r_e=="45-60",
     "nivel": "Medio"},
    {"id": "Regla 17", "descripcion": "ST Leve + Frecuencia Alta",
     "condicion": lambda h, _: h['st_ejercicio']=="Leve" and h['frecuencia_max']=="Alta",
     "nivel": "Medio"},
    {"id": "Regla 18", "descripcion": "Dolor Ausente + Presión Normal",
     "condicion": lambda h, _: h['dolor_pecho']=="Ausente" and h['presion']=="Normal",
     "nivel": "Bajo"},
    {"id": "Regla 19", "descripcion": "Glucosa Elevada + Colesterol Medio",
     "condicion": lambda h, _: h['glucosa']=="Elevada" and h['colesterol']=="Medio",
     "nivel": "Medio"},
    {"id": "Regla 20", "descripcion": "Edad<45 + ECG Normal + ST No",
     "condicion": lambda h, r_e: r_e=="<45" and h['ecg']=="Normal" and h['st_ejercicio']=="No",
     "nivel": "Bajo"}
]

# ==========================================
# INTERFAZ DE USUARIO
# ==========================================

def main():
    st.title("🫀 Sistema Experto: Riesgo Cardiovascular")
    st.markdown("""
    Este sistema evalúa su riesgo cardiovascular basándose en reglas médicas predefinidas.
    *Por favor, complete el formulario a continuación.*
    """)
    
    st.info("⚠️ **Aviso:** Esta herramienta es demostrativa y no sustituye el diagnóstico de un médico profesional.")

    st.divider()

    # --- RECOGIDA DE DATOS ---
    # Usamos columnas para mejorar la disposición visual
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Datos Generales")
        edad = st.number_input("Edad (años)", min_value=1, max_value=120, value=45, step=1)
        sexo = st.selectbox("Sexo", ["Hombre", "Mujer"])
        
        st.subheader("Indicadores Metabólicos")
        colesterol = st.selectbox("Nivel de Colesterol", ["Bajo", "Medio", "Alto"])
        glucosa = st.selectbox("Glucosa en ayunas", ["Normal", "Elevada"])
        presion = st.selectbox("Presión Arterial (Reposo)", ["Normal", "Ligeramente elevada", "Muy elevada"])

    with col2:
        st.subheader("Indicadores Cardíacos")
        frecuencia_max = st.selectbox("Frecuencia Cardíaca Máxima", ["Baja", "Media", "Alta"])
        dolor_pecho = st.selectbox("Dolor en el pecho", ["Ausente", "Leve", "Moderado", "Intenso"])
        angina = st.selectbox("¿Angina inducida por ejercicio?", ["Sí", "No"])
        
        st.subheader("Electrocardiograma (ECG)")
        ecg = st.selectbox("Resultado del ECG en reposo", ["Normal", "Anormal"])
        
        # Lógica Condicional: Pregunta ST solo si ECG es anormal
        st_ejercicio = "No" # Valor por defecto
        if ecg == "Anormal":
            st.markdown("**Detalle del ECG:**")
            st_ejercicio = st.selectbox(
                "¿Depresión del segmento ST inducida por ejercicio?",
                ["Inexistente", "Leve", "Significativa", "No lo sé"]
            )
            # Ayuda visual contextual sobre qué es el segmento ST si el usuario tiene dudas
            with st.expander("¿Qué es el segmento ST?"):
                 st.write("El segmento ST es una parte del ciclo cardíaco en el electrocardiograma. Su depresión puede indicar isquemia.")
                 # Triggering educational image for clarity
                 st.write("") 

    # --- BOTÓN DE ANÁLISIS ---
    st.markdown("---")
    analizar = st.button("🔍 Calcular Riesgo", type="primary", use_container_width=True)

    if analizar:
        # Preparar diccionario de hechos
        hechos = {
            "edad": edad, "sexo": sexo, "colesterol": colesterol,
            "glucosa": glucosa, "presion": presion,
            "frecuencia_max": frecuencia_max, "dolor_pecho": dolor_pecho,
            "ecg": ecg, "st_ejercicio": st_ejercicio, "angina": angina
        }

        # Calcular rango de edad para las reglas
        if edad < 45:
            rango_edad = "<45"
        elif 45 <= edad <= 60:
            rango_edad = "45-60"
        else:
            rango_edad = ">60"

        # --- MOTOR DE INFERENCIA ---
        jerarquia_riesgo = {"Bajo": 1, "Medio": 2, "Alto": 3}
        riesgo = "No determinado"
        reglas_disparadas = []

        for regla in reglas:
            # Ejecutamos la condición lambda
            if regla["condicion"](hechos, rango_edad):
                reglas_disparadas.append(regla)
                # Actualizamos riesgo si es mayor al actual
                if riesgo == "No determinado" or jerarquia_riesgo[regla['nivel']] > jerarquia_riesgo.get(riesgo, 0):
                    riesgo = regla['nivel']

        # --- MOSTRAR RESULTADOS ---
        st.subheader("Resultados del Análisis")

        # Feedback visual según el riesgo
        if riesgo == "Alto":
            st.error(f"🔴 **RIESGO DETECTADO: {riesgo.upper()}**")
            st.markdown("Se recomienda **asistencia médica inmediata** para una evaluación completa.")
        elif riesgo == "Medio":
            st.warning(f"🟠 **RIESGO DETECTADO: {riesgo.upper()}**")
            st.markdown("Se sugiere programar una cita médica para control y seguimiento.")
        elif riesgo == "Bajo":
            st.success(f"🟢 **RIESGO DETECTADO: {riesgo.upper()}**")
            st.markdown("Mantenga sus hábitos saludables y realice chequeos periódicos.")
        else:
            st.info("⚪ **RIESGO NO DETERMINADO**")
            st.markdown("No se activó ninguna regla específica con los datos proporcionados.")

        # Módulo de explicación (White Box)
        with st.expander("📂 Ver detalle técnico (Reglas activadas)"):
            if reglas_disparadas:
                st.write(f"Se activaron **{len(reglas_disparadas)}** reglas de inferencia:")
                for r in reglas_disparadas:
                    st.markdown(f"- **{r['id']}**: {r['descripcion']} → *Riesgo {r['nivel']}*")
            else:
                st.write("Ninguna regla de la base de conocimientos coincidió exactamente con los hechos presentados.")

if __name__ == "__main__":

    main()


