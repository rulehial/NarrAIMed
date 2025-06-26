from langgraph.graph import StateGraph
from graph.state import NarrativeState # <-- Importa el estado compartido
from agents.event_extractor import extract_events_node
from agents.timeline_analyzer import analyze_timeline_node
from agents.prompt_builder import build_prompt_node
from agents.narrator import generate_narrative_node
from agents.medication_node import medication_node


def build_narrative_graph():
    builder = StateGraph(NarrativeState)
    # Agregar nodos
    # builder.add_node("extract_events", extract_events_node())

    # builder.add_node("medication_node", medication_node())

    builder.add_node("analyze_timeline", analyze_timeline_node())

    builder.add_node("build_prompt", build_prompt_node())
    builder.add_node("generate_narrative", generate_narrative_node())




    # Definir flujo
    # builder.set_entry_point("extract_events")
    # builder.add_edge("extract_events", "analyze_timeline")
    # builder.add_edge("analyze_timeline", "build_prompt")
    # builder.add_edge("build_prompt", "generate_narrative")
    # builder.set_finish_point("generate_narrative")


#FUNCIONAAAAA
    # builder.set_entry_point("extract_events")
    # builder.add_edge("extract_events", "medication_node")
    # builder.add_edge("medication_node", "analyze_timeline")
    # builder.add_edge("analyze_timeline", "build_prompt")
    # builder.add_edge("build_prompt", "generate_narrative")
    # builder.set_finish_point("generate_narrative")

    builder.set_entry_point("analyze_timeline")
    builder.add_edge("analyze_timeline", "build_prompt")
    builder.add_edge("build_prompt", "generate_narrative")
    builder.set_finish_point("generate_narrative")





    # builder.set_entry_point("extract_events")

    # builder.add_edge("extract_events", "analyze_timeline")
    # builder.add_edge("analyze_timeline", "lab_results_summarizer")
    # builder.add_edge("lab_results_summarizer", "medication_summarizer")
    # builder.add_edge("medication_summarizer", "cie10_ingreso_extractor")
    # builder.add_edge("cie10_ingreso_extractor", "cie10_urgencia_extractor")
    # builder.add_edge("cie10_urgencia_extractor", "build_prompt")
    # builder.add_edge("build_prompt", "generate_narrative")

    # builder.set_finish_point("generate_narrative")

    return builder.compile()