## 🚀 Steps to Run in Google Colab

### 📦 1) Clone the Repository
```bash
!git clone https://github.com/SKULLMAXX/ecommerce.git
%cd ecommerce
````

---

### ⚙️ 2) Install Required Dependency

```bash
!pip install scikit-learn
```

---

### 🧾 3) Run `generate_data.py` (Creates multilingual dataset)

```bash
!python generate_data.py
```

---

### 🧠 4) Run `train_model.py` (Trains the model and saves `.pkl` files)

```bash
!python train_model.py
```

---

### 🔍 5) Use Trained Model for Predictions

Paste this code in a new cell to make predictions:

```python
import joblib, pickle

# Load the model and encoders
model = joblib.load('ecommerce_classifier.pkl')
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

# Example input
text = "I want to cancel my order"

# Predict
vector = vectorizer.transform([text])
pred = model.predict(vector)[0]
intent = label_encoder.inverse_transform([pred])[0]
confidence = model.predict_proba(vector)[0].max()

print("Intent:", intent)
print("Confidence:", round(confidence * 100, 2), "%")
