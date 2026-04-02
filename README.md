# 📣 AduanKu

AduanKu adalah prototype sistem analisis sentimen ulasan masyarakat berbasis Natural Language Processing (NLP).
Proyek ini dikembangkan untuk mengklasifikasikan ulasan ke dalam sentimen **Positif**, **Netral**, dan **Negatif** menggunakan metode **TF-IDF** dan **Logistic Regression**.

## 🚀 Fitur Utama
- Preprocessing teks Bahasa Indonesia
- Analisis sentimen ulasan
- Penanganan data imbalance dengan SMOTE
- Evaluasi model menggunakan Accuracy, Precision, Recall, dan F1-Score
- Keyword extraction untuk menampilkan kata-kata penting dari ulasan
- Prototype aplikasi berbasis Streamlit

## 🛠️ Teknologi yang Digunakan
- Python
- Scikit-learn
- Pandas
- NLTK
- Sastrawi
- Streamlit
- Imbalanced-learn

## 📊 Dataset
Dataset yang digunakan berasal dari Kaggle:

https://www.kaggle.com/datasets/nuricahyono/sp4n-lapor

## 📂 Struktur Project
```bash
AduanKu/
│── app.py
│── model.joblib
│── requirements.txt
│── README.md
```