from langgraph.graph import StateGraph
from graph.state import NarrativeState # <-- Importa el estado compartido
from agents.event_extractor import extract_events_node
from agents.timeline_analyzer import analyze_timeline_node
from agents.prompt_builder import build_prompt_node
from agents.narrator import generate_narrative_node

def build_narrative_graph():
    builder = StateGraph(NarrativeState)
    # Agregar nodos
    builder.add_node("extract_events", extract_events_node())
    builder.add_node("analyze_timeline", analyze_timeline_node())
    builder.add_node("build_prompt", build_prompt_node())
    builder.add_node("generate_narrative", generate_narrative_node())

    # Definir flujo
    builder.set_entry_point("extract_events")
    builder.add_edge("extract_events", "analyze_timeline")
    builder.add_edge("analyze_timeline", "build_prompt")
    builder.add_edge("build_prompt", "generate_narrative")
    builder.set_finish_point("generate_narrative")

    return builder.compile()