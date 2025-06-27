from langgraph.graph import StateGraph
from graph.state import NarrativeState
from nodes.timeline_analyzer_node import get_analyze_timeline_node
from nodes.prompt_builder_node import get_prompt_build_node
from nodes.narrator_node import get_narrative_node


def build_narrative_graph():
    # Crear el grafo
    builder = StateGraph(NarrativeState)

    # Agregar nodos
    builder.add_node("analyze_timeline", get_analyze_timeline_node())
    builder.add_node("build_prompt", get_prompt_build_node())
    builder.add_node("generate_narrative", get_narrative_node())


    # Definir flujo
    builder.set_entry_point("analyze_timeline")
    builder.add_edge("analyze_timeline", "build_prompt")
    builder.add_edge("build_prompt", "generate_narrative")
    builder.set_finish_point("generate_narrative")

    # retornar el grafo
    return builder.compile()