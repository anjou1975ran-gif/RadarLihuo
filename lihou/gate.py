from .radar import analyze

def evaluate(prompt):
    data = analyze(prompt)

    if not data["structure_ok"]:
        return "HOLD"
    
    if data["has_unknown"]:
        return "STOP"
    
    return "PASS"
