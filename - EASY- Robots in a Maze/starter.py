import pandas as pd
import random

# Citeste fisierele furnizate in problema drept set de date
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

rows = [
    {"robot_id": "GLOBAL", "subtaskID": 1, "answer": random.randint(1, 20)},
    {"robot_id": "GLOBAL", "subtaskID": 2, "answer": round(random.uniform(0.5, 10.0), 2)},
    {"robot_id": "GLOBAL", "subtaskID": 3, "answer": "rezultat"},
    {"robot_id": "GLOBAL", "subtaskID": 4, "answer": 100},
]

for robot_id in test["robot_id"]:
    rows.append({
        "robot_id": robot_id,
        "subtaskID": 5,
        "answer": random.choice("explorer")
    })

submission = pd.DataFrame(rows)
submission.to_csv("submission.csv", index=False)

print("submission.csv generat complet aleator.")