from .gate import evaluate

def run(prompt):
    decision = evaluate(prompt)

    if decision == "STOP":
        return "[LIHUO] STOP"
    elif decision == "HOLD":
        return "[LIHUO] HOLD"
    elif decision == "DELAY":
        return "[LIHUO] DELAY"
    else:
        return "[LIHUO] PASS"
