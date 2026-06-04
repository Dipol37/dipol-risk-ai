import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px

st.set_page_config(
    page_title="DiPol Risk AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 DiPol Risk AI")
st.subheader("Makine Öğrenmesi Destekli Risk Analiz Sistemi")

st.write("""
Bu uygulama, kullanıcıdan alınan finansal ve kişisel verileri kullanarak
risk seviyesini tahmin eder. Projede Random Forest algoritması kullanılmıştır.
""")

st.sidebar.header("Kullanıcı Bilgileri")

gelir = st.sidebar.number_input("Aylık Gelir (TL)", min_value=0, value=25000, step=1000)
borc = st.sidebar.number_input("Toplam Borç (TL)", min_value=0, value=50000, step=1000)
odeme_puani = st.sidebar.slider("Ödeme Puanı", 0, 100, 60)
yas = st.sidebar.slider("Yaş", 18, 70, 25)
calisma_suresi = st.sidebar.slider("Çalışma Süresi (Yıl)", 0, 40, 2)
gec_odeme = st.sidebar.slider("Geç Ödeme Sayısı", 0, 20, 1)

np.random.seed(42)

veri_sayisi = 300

X = pd.DataFrame({
    "gelir": np.random.randint(8000, 80000, veri_sayisi),
    "borc": np.random.randint(0, 300000, veri_sayisi),
    "odeme_puani": np.random.randint(0, 101, veri_sayisi),
    "yas": np.random.randint(18, 70, veri_sayisi),
    "calisma_suresi": np.random.randint(0, 40, veri_sayisi),
    "gec_odeme": np.random.randint(0, 20, veri_sayisi)
})

def risk_uret(row):
    risk = 0

    if row["borc"] > row["gelir"] * 6:
        risk += 2
    if row["odeme_puani"] < 40:
        risk += 2
    if row["gec_odeme"] > 5:
        risk += 2
    if row["calisma_suresi"] < 1:
        risk += 1
    if row["gelir"] < 15000:
        risk += 1

    if risk <= 1:
        return 0
    elif risk <= 3:
        return 1
    else:
        return 2

y = X.apply(risk_uret, axis=1)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

kullanici_verisi = pd.DataFrame({
    "gelir": [gelir],
    "borc": [borc],
    "odeme_puani": [odeme_puani],
    "yas": [yas],
    "calisma_suresi": [calisma_suresi],
    "gec_odeme": [gec_odeme]
})

tahmin = model.predict(kullanici_verisi)[0]
olasilik = model.predict_proba(kullanici_verisi)[0]

risk_metinleri = {
    0: "Düşük Risk",
    1: "Orta Risk",
    2: "Yüksek Risk"
}

risk_renkleri = {
    0: "🟢",
    1: "🟡",
    2: "🔴"
}

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tahmin Edilen Risk", f"{risk_renkleri[tahmin]} {risk_metinleri[tahmin]}")

with col2:
    borc_gelir_orani = borc / gelir if gelir > 0 else 0
    st.metric("Borç / Gelir Oranı", f"{borc_gelir_orani:.2f}")

with col3:
    st.metric("Ödeme Puanı", odeme_puani)

st.divider()

st.subheader("📊 Risk Olasılık Grafiği")

grafik_verisi = pd.DataFrame({
    "Risk Seviyesi": ["Düşük Risk", "Orta Risk", "Yüksek Risk"],
    "Olasılık": olasilik
})

fig = px.bar(
    grafik_verisi,
    x="Risk Seviyesi",
    y="Olasılık",
    title="Modelin Risk Tahmin Olasılıkları"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🧠 AI Yorumu")

if tahmin == 0:
    st.success("Bu kullanıcı düşük risk grubundadır. Gelir, ödeme puanı ve borç durumu genel olarak olumlu görünmektedir.")
elif tahmin == 1:
    st.warning("Bu kullanıcı orta risk grubundadır. Borç ve ödeme alışkanlıkları dikkatle değerlendirilmelidir.")
else:
    st.error("Bu kullanıcı yüksek risk grubundadır. Borç oranı, ödeme puanı veya geç ödeme sayısı risk oluşturabilir.")

st.divider()

st.subheader("📌 Kullanılan Algoritma")
st.write("""
Bu projede denetimli öğrenme yöntemlerinden biri olan Random Forest algoritması kullanılmıştır.
Random Forest, birden fazla karar ağacının birlikte çalışmasıyla sınıflandırma yapan güçlü bir makine öğrenmesi algoritmasıdır.
""")
