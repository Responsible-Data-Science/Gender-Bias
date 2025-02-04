# Mitigating Gender Bias in Search Engines

This project investigates and mitigates gender bias in automated image labeling systems across multiple search engines (Google, Baidu, Naver, and Yandex). It implements a modified ResNet-10 model for gender detection and employs novel re-ranking algorithms to ensure fairer representation in image search results.

## Table of Contents

- [Motivation](#motivation)
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Methodology](#methodology)
- [Re-Ranking Algorithms](#re-ranking-algorithms)
- [Execution Steps](#execution-steps)

## Motivation

Search engines significantly influence societal perceptions by shaping access to information. However, AI-driven image search results often exhibit gender bias, particularly in professional occupations. This project aims to:

- Analyze gender bias in image search results.
- Implement bias detection using a modified ResNet-10 model.
- Develop re-ranking algorithms to mitigate bias while maintaining search relevance.

## Project Overview

The project follows a structured approach:

1. **Data Collection**: Image search results are retrieved for gender-neutral queries.
2. **Bias Detection**: A ResNet-10-based model detects gender distribution in images.
3. **Bias Mitigation**: Re-ranking algorithms adjust search results to improve gender balance.
4. **Evaluation**: The impact of bias mitigation is measured using statistical analysis.

## Technologies Used

- **Frontend**: React.js (User Interface)
- **Backend**: Flask (Web Server)
- **Machine Learning**: ResNet-10 (Gender Classification)
- **Search APIs**: Google, Baidu, Naver, Yandex
- **Programming Languages**: Python, JavaScript

## Methodology

### 1. **Frontend (React.js)**

- Users enter search queries in a web interface.
- The query is sent to the Flask backend for processing.
- The UI dynamically updates with re-ranked image search results.

### 2. **Backend (Flask)**

- Handles requests from the frontend.
- Calls search engine APIs to retrieve image search results.
- Processes retrieved images using the gender detection model.
- Applies re-ranking algorithms to mitigate gender bias.
- Returns adjusted results to the frontend.

### 3. **Bias Detection**

- A modified ResNet-10 neural network is used for gender classification.
- The model analyzes search engine image results for gender representation.

<a id="re-ranking-algorithms"></a>

### 4. **Re-Ranking Algorithms**

To counteract gender bias, three re-ranking algorithms are implemented:

### **1. Epsilon-Greedy Algorithm**

- Introduces randomness to disrupt biased clusters.
- Randomly swaps images to achieve more balanced representation.

### **2. Relevance-Aware Swapping Algorithm**

- Balances fairness with relevance.
- Retains high-relevance images while ensuring gender diversity.

### **3. Fairness-Greedy Algorithm**

- Adjusts rankings based on real-world gender distribution in professions.
- Ensures that top search results reflect balanced gender representation.

## Execution Steps

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository

```

### **2. Set Up the Frontend (React.js)**

```bash
cd Client
npm install
npm start

```

This will launch the React web application.

### **3. Set Up the Backend (Flask)**

```bash
cd Server
pip install -r requirements.txt
python app.py

```
