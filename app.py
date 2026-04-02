import streamlit as st
import joblib
import numpy as np

st.title("📣 AduanKu")
st.write("Ulasan Pengguna pada AduanKu")

model = joblib.load("model.joblib")
tfidf = model.named_steps['tfidf']

def get_keywords(text):
    vec = tfidf.transform([text])
    feature_names = tfidf.get_feature_names_out()
    indices = np.argsort(vec.toarray()[0])[-5:]
    return [feature_names[i] for i in indices]

text = st.text_area("Masukkan komentar:")

if st.button("Analisis"):
    if text.strip() == "":
        st.warning("Tidak boleh kosong!")
    else:
        pred = model.predict([text])[0]
        st.success(f"Sentimen: {pred}")

        if hasattr(model, "predict_proba"):
            proba = model.predict_proba([text])[0]
            st.write(f"Confidence: {np.max(proba)*100:.2f}%")

        keywords = get_keywords(text)

        st.write("### Keyword:")
        for k in keywords:
            st.markdown(f"**{k}**")
