# Movie Recommendation System

## Overview
This is a **Movie Recommendation System** that suggests similar movies based on content similarity. It uses **Natural Language Processing (NLP)** and **cosine similarity** to find movies similar to the one selected by the user.

## Features
- Recommends **top 5 similar movies** based on content analysis.
- Uses **cosine similarity** to measure movie similarity.
- Fetches movie posters using the **OMDb API**.
- Provides an interactive user interface using **Streamlit**.

## Technologies Used
- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **NLTK** (Natural Language Toolkit)
- **Streamlit** (for UI)
- **OMDb API** (for fetching posters)

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/purva-8/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Install all dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Model Preprocessing
Execute `main.py` to generate the necessary files (`movies.pkl` and `similarity.pkl`).
```bash
python main.py
```

### 4. Run the Streamlit App
Once the preprocessing is done, start the recommendation system:
```bash
streamlit run app.py
```
---

## How It Works
### **1. Data Preprocessing (main.py)**
- **Merges** the movies and credits datasets.
- **Extracts important features** (genres, keywords, cast, crew, overview).
- **Cleans and processes text** (removes spaces, lowercase, and stems words).
- **Converts text data into numerical vectors** using **CountVectorizer**.
- **Computes cosine similarity** between movie vectors.
- Saves processed data into `movies.pkl` and `similarity.pkl`.

### **2. Recommendation System (app.py)**
- Loads the **movies and similarity matrix**.
- Provides a **dropdown to select a movie**.
- Computes **top 5 similar movies**.
- Fetches and displays **movie posters** using the **OMDb API**.

---

## Example Output
When a user selects **"Iron Man"**, the system may recommend:
1. The Avengers
2. Iron Man 2
3. Captain America: Civil War
4. Avengers: Age of Ultron
5. Thor

Each recommended movie is displayed along with its **poster**.

---
