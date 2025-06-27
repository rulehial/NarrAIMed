def format_eventos_for_llm(eventos_list):
    """
    Recibe la lista de registros de eventos y genera un texto legible para el LLM.
    """
    if not eventos_list:
        return "No hay eventos para este ingreso."
    

    if eventos_list:
        lines = ["--- Eventos Clínicos Detallados ---"]
        for i, evento in enumerate(eventos_list,start=1):
            fecha = evento.get("FECHA_CONSTANTE_INGRESO")
            fc = evento.get("FC_INGRESO")
            glu = evento.get("GLU_INGRESO")
            sat_o2 = evento.get("SAT_02_INGRESO")
            ta_max = evento.get("TA_MAX_INGRESO")
            ta_min = evento.get("TA_MIN_INGRESO")
            temp = evento.get("TEMPERATURA_INGRESO")
            obs = evento.get("SAT_02_INGRESO_OBSERVACIONES")


            line = f"Evento {i} ({fecha}): "
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

            line += ", ".join(detalles) if detalles else "Datos no especificados."
            
            lines.append(line)
        lines.append("")# Línea en blanco
    return "\n".join(lines)

def format_medicacion_for_llm(medicacion_list):
    """
    Recibe la lista de registros de medicación y genera un texto legible para el LLM.
    """
    if not medicacion_list:
        return "No hay registros de medicación para este ingreso."

    lines = ["--- Medicación Administrada Durante el Ingreso ---"]
    for i, med in enumerate(medicacion_list, start=1):
        nombre = med.get("FARMACO_NOMBRE_COMERCIAL", "Nombre desconocido")
        dosis = med.get("DOSIS_MEDIA_DIARIA", "Dosis no especificada")
        inicio = med.get("INICIO_TRATAMIENTO")
        fin = med.get("FIN_TRATAMIENTO")
        atc5 = med.get("ATC5_NOMBRE", "")
        
        inicio_str = inicio.strftime("%Y-%m-%d") if hasattr(inicio, "strftime") else str(inicio)
        fin_str = fin.strftime("%Y-%m-%d") if hasattr(fin, "strftime") else str(fin)

        line = (
            f"Medicamento {i}: {nombre}, Dosis media diaria: {dosis}, "
            f"Tratamiento desde: {inicio_str} hasta: {fin_str}"
        )
        if atc5:
            line += f", Clasificación ATC: {atc5}"
        lines.append(line)
    return "\n".join(lines)


def format_laboratorio_for_llm(laboratorio_list):
    """
    Recibe la lista de registros de laboratorio y genera un texto legible para el LLM.
    """
    # print(laboratorio_list)
    if not laboratorio_list:
        return "No hay registros de laboratorio para este ingreso."
    lines = ["--- Resultados de Laboratorio ---"]
    for i, lab in enumerate(laboratorio_list, start=1):
        laboratorio = lab.get("LAB_NUMERO", "Laboratorio no especificado")

        fecha_lab = lab.get("LAB_FECHA")
        # inicio_str = inicio.strftime("%Y-%m-%d") if hasattr(inicio, "strftime") else str(inicio)
        item = lab.get("LAB_ITEM")
        valor = lab.get("RESULTADO_VALOR")
        unidad = lab.get("RESULTADO_UNIDAD")
        referencias = lab.get("RESULTADO_VALORES_REFERENCIALES", "Referencias no especificadas")
        line = (
            f"Laboratorio {i}: {laboratorio}, Item: {item}, Valor: {valor}, "
            f"Unidad: {unidad}, Referencias: {referencias}"
        )
        lines.append(line)
    return "\n".join(lines)

def prepare_diagnostico_ppal(cie10_ingreso_data):
    """
    recibe listado de su diagnóstico principal en cie10 y genera un string legible para el LLM
    """
    if not cie10_ingreso_data:
        return "No hay registros de diagnóstico para este ingreso."
    
    cie10_ingreso = cie10_ingreso_data[0]
    diagnostico_ppal = cie10_ingreso.get("diagnostico_ppal", {})


    lines = ["--- Diagnostico Principal segun CIE10 ---"]
    
    ddpal = diagnostico_ppal
    codigo = ddpal.get("CODIGO", "Código no especificado")
    desc_corta = ddpal.get("DESCRIPCION_CORTA")
    desc_larga = ddpal.get("DESCRIPCION_LARGA")
    
    line = (
        f"Diagnostico Principal: {codigo}, Descripción Corta: {desc_corta}, Descripción Larga: {desc_larga}, "
    )
    lines.append(line)
    return "\n".join(lines)


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

    return "\n".join(historial_text)