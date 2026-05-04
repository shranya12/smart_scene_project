from typing import List


class SceneDescriber:
    def __init__(self):
        pass

    def analyze_scene(self, objects: List[str]):
        if not objects:
            return "No objects detected.", "No risk", "LOW"

        objects = list(set(objects))

        # ---------------- DESCRIPTION ----------------
        if "person" in objects and "car" in objects:
            desc = "A person is near a car in a traffic environment."
        elif "person" in objects and "bus" in objects:
            desc = "A person is close to a bus in a public area."
        elif "person" in objects and "cell phone" in objects:
            desc = "A person is using a mobile phone."
        elif "person" in objects and "laptop" in objects:
            desc = "A person is working on a laptop."
        elif "person" in objects:
            desc = "A person is present in the scene."
        else:
            desc = f"A scene with {', '.join(objects)}"

        # ---------------- RISK ----------------
        if "person" in objects and "car" in objects:
            risk = "High risk due to proximity to vehicles"
            level = "HIGH"

        elif "person" in objects and "bus" in objects:
            risk = "High risk due to large vehicle nearby"
            level = "HIGH"

        elif "person" in objects and "skateboard" in objects:
            risk = "Moderate risk due to movement activity"
            level = "MEDIUM"

        else:
            risk = "No immediate danger detected"
            level = "LOW"

        return desc, risk, level
