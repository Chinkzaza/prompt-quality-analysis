import json

with open("example_prompts.json") as f:
    data = json.load(f)

def score_prompts(data):
    return {item["id"]: len(item["response"].split()) for item in data}

print("Prompt Scores:", score_prompts(data))
