"""
Recursive AI Loop – Illuminator Protocol Core

Combines helix processing, ethical checks, and reset triggers.
"""

from core.helix_model import HelixModel
from core.reset import reset_to_z0

def illuminator_ai_loop(data_stream):
    model = HelixModel()

    for data in data_stream:
        if "violation" in data:
            return reset_to_z0(reason="ethics violation")
        elif "feedback" in data:
            model.feed_reactive(data)
        else:
            model.feed_proactive(data)

    result = model.evaluate()
    print("✅ Evaluation complete:", result)
    return result
