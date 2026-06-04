import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="HantaAI Risk Analizi",
    page_icon="🦠",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #7c3aed;
}
.sub-text {
    font-size: 18px;
    color: #444;
}
.info-card {
    padding: 18px;
    border-radius: 14px;
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    margin-bottom: 12px;
}
.warning-card {
    padding: 18px;
    border-radius: 14px;
    background-color: #fff7ed;
    border: 1px solid #fed7aa;
    margin-bottom: 12px;
}
.danger-card {
    padding: 18px;
    border-radius: 14px;
    background-color: #fef2f2;
    border: 1px solid #fecaca;
    margin-bottom: 12px;
}
.success-card {
    padding: 18px;
    border-radius: 14px;
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🦠 HantaAI Risk Analizi</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-text">Hanta virüsü hakkında bilgilendirme, belirti kontrolü ve risk yönlendirme uygulaması.</p>',
    unsafe_allow_html=True
)

st.warning(
    "Bu uygulama tıbbi teşhis koymaz. Yüksek riskli temas veya ciddi belirtiler varsa en yakın sağlık kuruluşuna başvurulmalıdır."
)

st.divider()

with st.sidebar:
    st.header("📋 Risk Formu")

    st.subheader("1. Temas Bilgileri")
    kemirgen_goruldu = st.selectbox(
        "Son günlerde fare/sıçan gibi kemirgen gördünüz mü?",
        ["Hayır", "Evet", "Emin değilim"]
    )

    kemirgen_izi = st.selectbox(
        "Kemirgen dışkısı, idrar izi, yuva veya kemirilmiş eşya gördünüz mü?",
        ["Hayır", "Evet", "Emin değilim"]
    )

    kapali_alan = st.selectbox(
        "Depo, bodrum, ahır, köy evi, garaj gibi kapalı/tozlu bir alan temizlediniz mi?",
        ["Hayır", "Evet"]
    )

    toz_kalkti = st.selectbox(
        "Temizlik sırasında yoğun toz kalktı mı?",
        ["Hayır", "Evet", "Emin değilim"]
    )

    maske = st.selectbox(
        "Temizlik sırasında maske kullandınız mı?",
        ["Evet", "Hayır"]
    )

    eldiven = st.selectbox(
        "Temizlik sırasında eldiven kullandınız mı?",
        ["Evet", "Hayır"]
    )

    temas_gunu = st.slider(
        "Olası temastan kaç gün geçti?",
        0, 60, 7
    )

    st.subheader("2. Belirti Bilgileri")

    ates = st.checkbox("Ateş")
    halsizlik = st.checkbox("Halsizlik / yorgunluk")
    kas_agrisi = st.checkbox("Kas ağrısı")
    bas_agrisi = st.checkbox("Baş ağrısı")
    oksuruk = st.checkbox("Öksürük")
    nefes_darligi = st.checkbox("Nefes darlığı")
    bulanti = st.checkbox("Bulantı / kusma")
    karin_agrisi = st.checkbox("Karın ağrısı")
    ishal = st.checkbox("İshal")

    st.subheader("3. Ek Durum")
    yas_grubu = st.selectbox(
        "Yaş grubunuz",
        ["18 altı", "18-30", "31-45", "46-60", "60+"]
    )

    bolge = st.selectbox(
        "Bulunduğunuz ortam",
        ["Şehir merkezi", "Kırsal alan", "Köy / çiftlik", "Ormanlık alan", "Diğer"]
    )


def risk_hesapla():
    risk = 0
    nedenler = []

    if kemirgen_goruldu == "Evet":
        risk += 2
        nedenler.append("Kemirgen görülmesi risk puanını artırdı.")
    elif kemirgen_goruldu == "Emin değilim":
        risk += 1
        nedenler.append("Kemirgen teması net olmadığı için düşük düzeyde risk eklendi.")

    if kemirgen_izi == "Evet":
        risk += 3
        nedenler.append("Kemirgen dışkısı/idrar izi/yuva görülmesi önemli risk faktörüdür.")
    elif kemirgen_izi == "Emin değilim":
        risk += 1
        nedenler.append("Kemirgen izi net olmadığı için dikkat edilmesi önerilir.")

    if kapali_alan == "Evet":
        risk += 2
        nedenler.append("Kapalı ve tozlu alan temizliği risk puanını artırdı.")

    if toz_kalkti == "Evet":
        risk += 2
        nedenler.append("Toz kalkması, kirli partiküllerin solunma riskini artırabilir.")
    elif toz_kalkti == "Emin değilim":
        risk += 1

    if maske == "Hayır":
        risk += 1
        nedenler.append("Maske kullanılmaması koruyuculuğu azaltır.")

    if eldiven == "Hayır":
        risk += 1
        nedenler.append("Eldiven kullanılmaması temas riskini artırabilir.")

    belirti_sayisi = sum([
        ates, halsizlik, kas_agrisi, bas_agrisi,
        oksuruk, nefes_darligi, bulanti, karin_agrisi, ishal
    ])

    risk += belirti_sayisi

    if belirti_sayisi >= 3:
        nedenler.append("Birden fazla belirti işaretlendiği için risk puanı yükseldi.")

    if nefes_darligi:
        risk += 4
        nedenler.append("Nefes darlığı ciddi bir uyarı belirtisi olabilir.")

    if oksuruk:
        risk += 1
        nedenler.append("Öksürük solunumla ilgili belirti olduğu için dikkate alındı.")

    if 7 <= temas_gunu <= 45:
        risk += 1
        nedenler.append("Temas sonrası geçen süre belirti takibi açısından anlamlı aralıkta.")

    if bolge in ["Kırsal alan", "Köy / çiftlik", "Ormanlık alan"]:
        risk += 1
        nedenler.append("Kırsal/ormanlık ortam kemirgen teması ihtimalini artırabilir.")

    return risk, nedenler, belirti_sayisi


risk_puani, nedenler, belirti_sayisi = risk_hesapla()

if risk_puani <= 4:
    risk_seviyesi = "Düşük Risk"
    risk_emoji = "🟢"
    risk_aciklama = "Verilen bilgilere göre risk düşük görünüyor. Yine de ortam temizliği ve belirti takibi önemlidir."
elif risk_puani <= 9:
    risk_seviyesi = "Orta Risk"
    risk_emoji = "🟡"
    risk_aciklama = "Bazı risk faktörleri mevcut. Belirtiler devam ederse veya artarsa sağlık kuruluşuna danışılması önerilir."
else:
    risk_seviyesi = "Yüksek Risk"
    risk_emoji = "🔴"
    risk_aciklama = "Risk faktörleri ve/veya belirtiler dikkat çekiyor. Özellikle nefes darlığı varsa gecikmeden sağlık kuruluşuna başvurulmalıdır."

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Risk Seviyesi", f"{risk_emoji} {risk_seviyesi}")

with col2:
    st.metric("Risk Puanı", risk_puani)

with col3:
    st.metric("Belirti Sayısı", belirti_sayisi)

st.divider()

if risk_seviyesi == "Düşük Risk":
    st.markdown(f"""
    <div class="success-card">
    <h3>🟢 Sonuç: {risk_seviyesi}</h3>
    <p>{risk_aciklama}</p>
    </div>
    """, unsafe_allow_html=True)

elif risk_seviyesi == "Orta Risk":
    st.markdown(f"""
    <div class="warning-card">
    <h3>🟡 Sonuç: {risk_seviyesi}</h3>
    <p>{risk_aciklama}</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown(f"""
    <div class="danger-card">
    <h3>🔴 Sonuç: {risk_seviyesi}</h3>
    <p>{risk_aciklama}</p>
    </div>
    """, unsafe_allow_html=True)

st.subheader("🧠 AI Yorumlama")

if nedenler:
    for neden in nedenler:
        st.write(f"• {neden}")
else:
    st.write("Belirgin risk faktörü seçilmedi.")

st.divider()

st.subheader("📊 Risk Dağılımı")

grafik_verisi = pd.DataFrame({
    "Kategori": ["Temas Riski", "Belirti Riski", "Korunma Eksikliği", "Ortam Riski"],
    "Puan": [
        (2 if kemirgen_goruldu == "Evet" else 0) + (3 if kemirgen_izi == "Evet" else 0),
        belirti_sayisi + (4 if nefes_darligi else 0),
        (1 if maske == "Hayır" else 0) + (1 if eldiven == "Hayır" else 0),
        (2 if kapali_alan == "Evet" else 0) + (2 if toz_kalkti == "Evet" else 0)
    ]
})

fig = px.bar(
    grafik_verisi,
    x="Kategori",
    y="Puan",
    title="Risk Faktörlerinin Dağılımı"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("🚨 Ne Zaman Sağlık Kuruluşuna Başvurulmalı?")

st.markdown("""
<div class="danger-card">
<b>Aşağıdaki durumlardan biri varsa gecikmeden sağlık kuruluşuna başvurulmalıdır:</b><br><br>
• Nefes darlığı<br>
• Göğüste sıkışma hissi<br>
• Yüksek ateşin devam etmesi<br>
• Şiddetli halsizlik<br>
• Kemirgen teması sonrası birden fazla belirti görülmesi<br>
</div>
""", unsafe_allow_html=True)

st.subheader("🧼 Korunma ve Temizlik Önerileri")

st.markdown("""
<div class="info-card">
<b>Güvenli temizlik için genel öneriler:</b><br><br>
• Kemirgen izi olan alanları kuru şekilde süpürmemek<br>
• Temizlik öncesi ortamı havalandırmak<br>
• Maske ve eldiven kullanmak<br>
• Toz kaldırmamaya dikkat etmek<br>
• Kemirgen giriş noktalarını kapatmak<br>
• Gıdaları kapalı kaplarda saklamak<br>
• Çöp ve yiyecek artıklarını açıkta bırakmamak<br>
</div>
""", unsafe_allow_html=True)

st.subheader("📚 Hanta Virüsü Nedir?")

st.markdown("""
<div class="info-card">
Hanta virüsleri, bazı kemirgenlerde bulunabilen virüslerdir. İnsanlar genellikle kemirgenlerin
idrar, dışkı veya tükürük kalıntılarıyla temas ettiklerinde ya da kirlenmiş tozu soluduklarında
risk altında olabilir. Bu uygulama, kullanıcıdan alınan bilgilere göre basit bir risk değerlendirmesi yapar.
</div>
""", unsafe_allow_html=True)

st.subheader("📌 Projede Kullanılan Yöntem")

st.write("""
Bu uygulamada kural tabanlı bir risk puanlama sistemi kullanılmıştır.
Kullanıcının verdiği cevaplar; temas, belirti, korunma ve ortam faktörlerine göre puanlanır.
Toplam puana göre düşük, orta veya yüksek risk sonucu üretilir.
""")

st.info(
    "Not: Bu sistem eğitim amaçlıdır. Gerçek sağlık değerlendirmesi için doktor veya sağlık kuruluşu gereklidir."
)
