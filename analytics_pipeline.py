import pandas as pd
import matplotlib.pyplot as plt

# Candidate performance data
scores = pd.DataFrame({
    "candidate": ["A", "B", "C"],
    "coding": [85, 60, 92],
    "mcq": [78, 70, 88],
    "project": [90, 65, 95]
})

# Monitoring signals
signals = pd.DataFrame({
    "candidate": ["A", "B", "C"],
    "tab_switch": [1, 5, 0],
    "face_detected": [True, False, True],
    "idle_time": [5, 20, 3]
})

# Combine both datasets
data = pd.merge(scores, signals, on="candidate")

# Academic score
data["academic_score"] = (data["coding"] + data["mcq"] + data["project"]) / 3

# Behavioral metrics
data["focus_score"] = 100 - (data["idle_time"] * 2)
data["integrity_score"] = 100 - (data["tab_switch"] * 10)
data["presence_score"] = data["face_detected"].apply(lambda x: 100 if x else 50)

# Behavior score
data["behavior_score"] = (
    data["focus_score"] +
    data["integrity_score"] +
    data["presence_score"]
) / 3

# Final candidate score
data["final_score"] = (
    0.7 * data["academic_score"] +
    0.3 * data["behavior_score"]
)

print("\nCandidate Analytics Result\n")
print(data)

# Visualization
plt.bar(data["candidate"], data["final_score"])
plt.title("Candidate Final Performance")
plt.xlabel("Candidate")
plt.ylabel("Score")
plt.show()