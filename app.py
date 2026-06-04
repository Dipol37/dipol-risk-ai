import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="HantaAI Risk Analizi",
    page_icon="🦠",
    layout="wide"
)

# -------------------------
# CSS
# -------------------------
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background: linear-gradient(180deg, #0b1020 0%, #111827 100%);
    color: white;
}

section[data-testid="stSidebar"] {
    background: #161f33;
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero-box {
    background: linear-gradient(135deg, rgba(124,58,237,0.28), rgba(59,130,246,0.18));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 28px 30px;
    margin-bottom: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    color: #c4b5fd;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 17px;
    color: #d1d5db;
    line-height: 1.6;
}

.metric-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px;
    margin-top: 10px;
    margin-bottom: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.18);
}

.metric-title {
    font-size: 14px;
    color: #cbd5e1;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: white;
}

.section-title {
    font-size: 28px;
    font-weight: 750;
    margin-top: 10px;
    margin-bottom: 10px;
    color: #f8fafc;
}

.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 16px;
    box-shadow: 0 10px 24px rgba(0,0,0,0.18);
}

.success-box {
    background: rgba(34,197,94,0.12);
    border: 1px solid rgba(34,197,94,0.35);
    border-left: 6px solid #22c55e;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
}

.warning-box {
    background: rgba(245,158,11,0.12);
    border: 1px solid rgba(245,158,11,0.35);
    border-left: 6px solid #f59e0b;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
}

.danger-box {
    background: rgba(239,68,68,0.12);
    border: 1px solid rgba(239,68,68,0.35);
    border-left: 6px solid #ef4444;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
}

.small-text {
    color: #cbd5e1;
    font-size: 15px;
    line-height: 1.7;
}

.info-chip {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    margin-right: 8px;
    margin-bottom: 8px;
    color: #e5e7eb;
    font-size: 13px;
}

hr {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.08);
    margin: 1.2rem 0;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    padding: 16px;
    border-radius: 16px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.markdown("## 📋 Risk Formu")
    st.caption("Temas, belirti ve korunma bilgilerinizi girin.")

    st.markdown("### 1) Temas Bilgileri")
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
        "Temizlik sırasında yoğun toz çıktı mı?",
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

    st.markdown("### 2) Belirti Bilgileri")
    ates = st.checkbox("Ateş")
    halsizlik = st.checkbox("Halsizlik / yorgunluk")
    kas_agrisi = st.checkbox("Kas ağrısı")
    bas_agrisi = st.checkbox("Baş ağrısı")
    oksuruk = st.checkbox("Öksürük")
    nefes_darligi = st.checkbox("Nefes darlığı")
    bulanti = st.checkbox("Bulantı / kusma")
    karin_agrisi = st.checkbox("Karın ağrısı")
    ishal = st.checkbox("İshal")

    st.markdown("### 3) Ek Bilgiler")
    yas_grubu = st.selectbox(
        "Yaş grubunuz",
        ["18 altı", "18-30", "31-45", "46-60", "60+"]
    )

    bolge = st.selectbox(
        "Bulunduğunuz ortam",
        ["Şehir merkezi", "Kırsal alan", "Köy / çiftlik", "Ormanlık alan", "Diğer"]
    )

# -------------------------
# Risk logic
# -------------------------
def risk_hesapla():
    risk = 0
    nedenler = []

    if kemirgen_goruldu == "Evet":
        risk += 2
        nedenler.append("Kemirgen görülmesi risk puanını artırdı.")
    elif kemirgen_goruldu == "Emin değilim":
        risk += 1
        nedenler.append("Kemirgen teması net olmadığı için dikkatli olunmalıdır.")

    if kemirgen_izi == "Evet":
        risk += 3
        nedenler.append("Kemirgen dışkısı/idrar izi/yuva görülmesi önemli risk faktörüdür.")
    elif kemirgen_izi == "Emin değilim":
        risk += 1
        nedenler.append("Kemirgen izi konusunda belirsizlik bulunduğu için dikkat önerilir.")

    if kapali_alan == "Evet":
        risk += 2
        nedenler.append("Kapalı ve tozlu alan temizliği risk puanını yükseltti.")

    if toz_kalkti == "Evet":
        risk += 2
        nedenler.append("Toz kalkması solunumla maruziyet ihtimalini artırabilir.")
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
        nedenler.append("Birden fazla belirti işaretlendiği için risk seviyesi yükseldi.")

    if nefes_darligi:
        risk += 4
        nedenler.append("Nefes darlığı önemli bir uyarı belirtisidir.")

    if oksuruk:
        risk += 1
        nedenler.append("Öksürük solunum sistemiyle ilgili bir belirti olduğu için dikkate alındı.")

    if 7 <= temas_gunu <= 45:
        risk += 1
        nedenler.append("Temas sonrası geçen süre belirti gelişimi açısından anlamlı aralıktadır.")

    if bolge in ["Kırsal alan", "Köy / çiftlik", "Ormanlık alan"]:
        risk += 1
        nedenler.append("Bulunulan ortam kemirgen teması ihtimalini artırabilir.")

    temas_riski = (
        (2 if kemirgen_goruldu == "Evet" else 1 if kemirgen_goruldu == "Emin değilim" else 0)
        + (3 if kemirgen_izi == "Evet" else 1 if kemirgen_izi == "Emin değilim" else 0)
    )

    belirti_riski = belirti_sayisi + (4 if nefes_darligi else 0) + (1 if oksuruk else 0)
    korunma_riski = (1 if maske == "Hayır" else 0) + (1 if eldiven == "Hayır" else 0)
    ortam_riski = (2 if kapali_alan == "Evet" else 0) + (2 if toz_kalkti == "Evet" else 0)

    return risk, nedenler, belirti_sayisi, temas_riski, belirti_riski, korunma_riski, ortam_riski

risk_puani, nedenler, belirti_sayisi, temas_riski, belirti_riski, korunma_riski, ortam_riski = risk_hesapla()

if risk_puani <= 4:
    risk_seviyesi = "Düşük Risk"
    risk_emoji = "🟢"
    risk_aciklama = "Verilen bilgilere göre risk düşük görünüyor. Yine de temizlik kurallarına dikkat edilmeli ve belirtiler takip edilmelidir."
    sonuc_class = "success-box"
elif risk_puani <= 9:
    risk_seviyesi = "Orta Risk"
    risk_emoji = "🟡"
    risk_aciklama = "Bazı risk faktörleri mevcut. Belirtiler sürerse veya artarsa sağlık kuruluşuna danışılması önerilir."
    sonuc_class = "warning-box"
else:
    risk_seviyesi = "Yüksek Risk"
    risk_emoji = "🔴"
    risk_aciklama = "Risk faktörleri ve/veya belirtiler dikkat çekicidir. Özellikle nefes darlığı varsa gecikmeden sağlık kuruluşuna başvurulmalıdır."
    sonuc_class = "danger-box"

# -------------------------
# Header
# -------------------------
st.markdown("""
<div class="hero-box">
    <div class="hero-title">🦠 HantaAI Risk Analizi</div>
    <div class="hero-subtitle">
        Hanta virüsü hakkında bilgilendirme, belirti kontrolü ve risk yönlendirme uygulaması.
        Kullanıcının verdiği cevaplara göre temas, belirti, korunma ve ortam faktörleri değerlendirilir.
    </div>
    <br>
    <span class="info-chip">Risk Değerlendirme</span>
    <span class="info-chip">Belirti Kontrolü</span>
    <span class="info-chip">Korunma Önerileri</span>
    <span class="info-chip">Yönlendirme Desteği</span>
</div>
""", unsafe_allow_html=True)

st.warning("Bu uygulama tıbbi teşhis koymaz. Yüksek riskli temas veya ciddi belirtiler varsa en yakın sağlık kuruluşuna başvurulmalıdır.")

# -------------------------
# Metrics
# -------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Risk Seviyesi</div>
        <div class="metric-value">{risk_emoji} {risk_seviyesi}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Risk Puanı</div>
        <div class="metric-value">{risk_puani}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Belirti Sayısı</div>
        <div class="metric-value">{belirti_sayisi}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Result
# -------------------------
st.markdown(f"""
<div class="{sonuc_class}">
    <h3 style="margin-top:0;">{risk_emoji} Sonuç: {risk_seviyesi}</h3>
    <p class="small-text" style="margin-bottom:0;">{risk_aciklama}</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# Main content
# -------------------------
left, right = st.columns([1.1, 0.9])

with left:
    st.markdown('<div class="section-title">🧠 Yapay Zeka Yorumlama</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if nedenler:
        for neden in nedenler:
            st.write(f"• {neden}")
    else:
        st.write("Belirgin risk faktörü seçilmedi.")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📊 Risk Dağılımı</div>', unsafe_allow_html=True)

    grafik_verisi = pd.DataFrame({
        "Kategori": ["Temas Riski", "Belirti Riski", "Korunma Eksikliği", "Ortam Riski"],
        "Puan": [temas_riski, belirti_riski, korunma_riski, ortam_riski]
    })

    fig = px.bar(
        grafik_verisi,
        x="Kategori",
        y="Puan",
        text="Puan",
        color="Kategori",
        title="Risk Faktörlerinin Dağılımı"
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.03)",
        font=dict(color="white"),
        title_font=dict(size=20),
        xaxis_title="",
        yaxis_title="Puan",
        legend_title=""
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown('<div class="section-title">🚨 Ne Zaman Sağlık Kuruluşuna Başvurulmalı?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="small-text">
        <b>Aşağıdaki durumlardan biri varsa gecikmeden sağlık kuruluşuna başvurulmalıdır:</b><br><br>
        • Nefes darlığı<br>
        • Göğüste sıkışma hissi<br>
        • Yüksek ateşin devam etmesi<br>
        • Şiddetli halsizlik<br>
        • Kemirgen teması sonrası birden fazla belirti görülmesi
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🧼 Korunma Önerileri</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="small-text">
        • Kemirgen izi olan alanları kuru şekilde süpürmeyin.<br>
        • Temizlik öncesinde ortamı havalandırın.<br>
        • Maske ve eldiven kullanın.<br>
        • Toz kaldırmamaya dikkat edin.<br>
        • Kemirgen giriş noktalarını kapatın.<br>
        • Gıdaları kapalı kaplarda saklayın.<br>
        • Çöp ve yiyecek artıklarını açıkta bırakmayın.
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Additional info
# -------------------------
st.markdown('<div class="section-title">📚 Hanta Virüsü Nedir?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div class="small-text">
    Hanta virüsleri, bazı kemirgenlerde bulunabilen virüslerdir. İnsanlar genellikle kemirgenlerin
    idrar, dışkı veya tükürük kalıntılarıyla temas ettiklerinde ya da kirlenmiş tozu soluduklarında
    risk altında olabilir. Bu uygulama, kullanıcıdan alınan bilgilere göre bilgilendirme amaçlı
    basit bir risk değerlendirmesi yapar.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">📌 Projede Kullanılan Yöntem</div>', unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div class="small-text">
    Bu uygulamada <b>kural tabanlı risk puanlama sistemi</b> kullanılmıştır.
    Kullanıcının verdiği cevaplar; temas, belirti, korunma ve ortam faktörlerine göre puanlanır.
    Toplam puana göre düşük, orta veya yüksek risk sonucu üretilir.
    </div>
</div>
""", unsafe_allow_html=True)

st.info("Not: Bu sistem eğitim amaçlıdır. Gerçek sağlık değerlendirmesi için doktor veya sağlık kuruluşu gereklidir.")
