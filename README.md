Candidate Performance Analytics Integration

📌 Overview

This project implements a **Candidate Performance Analytics Pipeline** that integrates academic scores with monitoring signals to generate meaningful behavioral insights and final evaluation metrics.

The system simulates how modern **AI-based proctoring and hiring platforms** evaluate candidates by combining performance data with behavioral indicators.

---

🎯 Objective

* Combine performance scores with monitoring signals
* Generate behavioral performance metrics
* Build a complete analytics pipeline
* Produce final candidate evaluation
* 
⚙️ Features

* Data integration using Pandas
* Behavioral metric generation (focus, integrity, presence)
* Final score calculation combining performance and behavior
* Simple visualization using Matplotlib

🧠 Methodology

 1. Data Collection

Two datasets are used:

* Candidate performance scores
* Monitoring signals (tab switch, idle time, face detection)

2. Data Integration

Datasets are merged using candidate ID.

 3. Feature Engineering

Behavioral metrics are derived:

* **Focus Score** → Based on idle time
* **Integrity Score** → Based on tab switching
* **Presence Score** → Based on face detection

4. Score Calculation

* Academic Score = Average of coding, MCQ, project
* Behavior Score = Average of behavioral metrics
* Final Score =

  * 70% Academic Performance
  * 30% Behavioral Performance

---

🏗️ Project Structure

candidate_analytics
│
├── analytics_pipeline.py
├── requirements.txt

---

## 🚀 How to Run

### Step 1: Clone or Download Project

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Run the Script

```
python analytics_pipeline.py
```

---

## 📊 Output

* Displays candidate performance analytics in tabular form
* Generates a bar chart showing final scores

---

## 📦 Requirements

* Python 3.x
* pandas
* matplotlib

---

## 🔍 Example Metrics

| Candidate | Academic | Behavior | Final |
| --------- | -------- | -------- | ----- |
| A         | 84.3     | 92       | 87    |
| B         | 65       | 60       | 63    |
| C         | 91.6     | 97       | 93    |

---

## 💡 Use Cases

* Online examination systems
* AI-based candidate screening
* Behavioral analytics platforms
* Hiring evaluation systems

---

## 📌 Conclusion

This project demonstrates how **data integration and feature engineering** can be used to build a simple yet effective analytics pipeline for candidate evaluation.

---

## ⚡ Future Improvements

* Add real-time monitoring data
* Integrate machine learning models
* Build a web-based dashboard
* Support multiple candidates via CSV input

---

## 👩‍💻 Author

Developed as part of AI/ML Internship Task
