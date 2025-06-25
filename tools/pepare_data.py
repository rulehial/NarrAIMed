def prepare_historial_for_llm(pacientes: list[dict]) -> str:
    """
    Convierte una lista de diccionarios con información clínica en un string legible
    para el modelo de lenguaje.
    """

    if not pacientes:
        return "No hay historial clínico disponible."

    paciente = pacientes[0]  # Tomamos el primero de la lista

    historial_text = []

    # 1. Información general del paciente y del episodio
    historial_text.append(f"--- Datos Generales del Paciente ---")
    historial_text.append(f"ID Paciente: {paciente.get('ID_PACIENTE')}")
    historial_text.append(f"Edad: {paciente.get('EDAD')}")
    historial_text.append(f"Sexo: {paciente.get('SEXO')}")
    historial_text.append(f"Diagnóstico de Ingreso: {paciente.get('DIAGNOSTICO_INGRESO')}")
    historial_text.append(f"Fecha de Ingreso: {paciente.get('FECHA_INGRESO')}")
    historial_text.append(f"Fecha de Alta: {paciente.get('FECHA_ALTA_INGRESO')}")
    historial_text.append(f"Motivo de Alta: {paciente.get('MOTIVO_ALTA_INGRESO')}")
    historial_text.append(f"Diagnóstico de Urgencia: {paciente.get('DIAGNOSTICO_URGENCIA')}")
    historial_text.append(f"Especialidad Urgencia: {paciente.get('ESPECIALIDAD_URGENCIA')}")
    historial_text.append(f"Destino Urgencia: {paciente.get('DESTINO_URGENCIA')}")
    historial_text.append(f"Respirador: {'Sí' if paciente.get('RESPIRADOR') else 'No'}")
    historial_text.append("")  # Línea en blanco

    # 2. Constantes vitales de urgencia
    if paciente.get('FC_ULTIMA_URGENCIA') is not None:
        historial_text.append(f"--- Constantes Vitales de Última Urgencia ---")
        historial_text.append(f"Hora: {paciente.get('HORA_CONSTANTES_ULTIMA_URGENCIA')}")
        historial_text.append(f"FC: {paciente.get('FC_ULTIMA_URGENCIA')}")
        historial_text.append(f"Temperatura: {paciente.get('TEMPERATURA_ULTIMA_URGENCIA')}")
        historial_text.append(f"Sat O2: {paciente.get('SAT_02_ULTIMA_URGENCIA')}")
        historial_text.append(f"TA Max: {paciente.get('TA_MAX_ULTIMA_URGENCIA')}")
        historial_text.append(f"TA Min: {paciente.get('TA_MIN_ULTIMA_URGENCIA')}")
        historial_text.append("")

    # 3. Eventos clínicos detallados
    eventos_data = paciente.get("eventos", [])
    if isinstance(eventos_data, str):
        try:
            import json
            eventos_data = json.loads(eventos_data)
        except Exception:
            eventos_data = []

    if eventos_data:
        historial_text.append(f"--- Eventos Clínicos Detallados ---")
        for i, evento in enumerate(eventos_data):
            fecha = evento.get("FECHA_CONSTANTE_INGRESO")
            fc = evento.get("FC_INGRESO")
            glu = evento.get("GLU_INGRESO")
            sat_o2 = evento.get("SAT_02_INGRESO")
            ta_max = evento.get("TA_MAX_INGRESO")
            ta_min = evento.get("TA_MIN_INGRESO")
            temp = evento.get("TEMPERATURA_INGRESO")
            obs = evento.get("SAT_02_INGRESO_OBSERVACIONES")

            evento_str = f"Evento {i+1} ({fecha}): "
            detalles = []
            if fc is not None: detalles.append(f"FC: {fc}")
            if glu is not None: detalles.append(f"GLU: {glu}")
            if sat_o2 is not None: detalles.append(f"Sat O2: {sat_o2}")
            if ta_max is not None and ta_min is not None:
                detalles.append(f"TA: {ta_max}/{ta_min}")
            elif ta_max is not None:
                detalles.append(f"TA Max: {ta_max}")
            elif ta_min is not None:
                detalles.append(f"TA Min: {ta_min}")
            if temp is not None: detalles.append(f"Temp: {temp}°C")
            if obs: detalles.append(f"Obs Sat O2: {obs}")

            evento_str += ", ".join(detalles) if detalles else "Datos no especificados."
            historial_text.append(evento_str)

    return "\n".join(historial_text)