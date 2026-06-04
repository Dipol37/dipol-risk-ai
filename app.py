import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="HantaAI | Risk Değerlendirme",
    page_icon="🦠",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #07111f 0%, #0f172a 45%, #111827 100%);
    color: #f8fafc;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    display: none;
}

.hero {
    background: radial-gradient(circle at top left, rgba(139,92,246,.38), transparent 35%),
                linear-gradient(135deg, rgba(30,41,59,.98), rgba(15,23,42,.98));
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 28px;
    padding: 34px;
    box-shadow: 0 18px 50px rgba(0,0,0,.35);
    margin-bottom: 22px;
}

.hero h1 {
    font-size: 46px;
    line-height: 1.1;
    margin: 0 0 12px 0;
    color: #ddd6fe;
    letter-spacing: -1px;
}

.hero p {
    color: #cbd5e1;
    font-size: 18px;
    line-height: 1.7;
    max-width: 850px;
}

.badge {
    display: inline-block;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.10);
    padding: 8px 14px;
    border-radius: 999px;
    margin-right: 8px;
    margin-top: 10px;
    font-size: 13px;
    color: #e5e7eb;
}

.notice {
    background: rgba(250,204,21,.12);
    border: 1px solid rgba(250,204,21,.30);
    color: #fef9c3;
    border-radius: 18px;
    padding: 16px 18px;
    margin: 18px 0 28px 0;
}

.card {
    background: rgba(15,23,42,.72);
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 14px 34px rgba(0,0,0,.22);
    margin-bottom: 18px;
}

.form-card {
    background: rgba(255,255,255,.045);
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 22px;
}

.section-title {
    font-size: 27px;
    font-weight: 800;
    color: #f8fafc;
    margin: 8px 0 12px 0;
}

.muted {
    color: #cbd5e1;
    line-height: 1.7;
}

.metric-box {
    background: rgba(255,255,255,.045);
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 22px;
    padding: 22px;
    min-height: 128px;
}

.metric-label {
    color: #cbd5e1;
    font-size: 14px;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 34px;
    font-weight: 850;
    color: #fff;
}

.low {
    background: rgba(34,197,94,.12);
    border: 1px solid rgba(34,197,94,.36);
    border-left: 7px solid #22c55e;
}

.mid {
    background: rgba(245,158,11,.13);
    border: 1px solid rgba(245,158,11,.38);
    border-left: 7px solid #f59e0b;
}

.high {
    background: rgba(239,68,68,.13);
    border: 1px solid rgba(239,68,68,.38);
    border-left: 7px solid #ef4444;
}

.result-title {
    font-size: 30px;
    font-weight: 850;
    margin-bottom: 12px;
}

.result-text {
    color: #e5e7eb;
    line-height: 1.75;
    font-size: 16px;
}

.step {
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(255,255,255,.08);
    padding: 15px;
    border-radius: 16px;
    margin-bottom: 10px;
}

.footer-box {
    text-align: center;
    color: #94a3b8;
    padding: 20px;
    font-size: 14px;
}

div[data-testid="stExpander"] {
    background: rgba(255,255,255,.04);
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 16px;
}

@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }

    .hero {
        padding: 22px;
        border-radius: 20px;
    }

    .hero h1 {
        font-size: 32px;
    }

    .hero p {
        font-size: 15px;
    }

    .badge {
        font-size: 12px;
        padding: 7px 10px;
    }

    .section-title {
        font-size: 22px;
    }

    .metric-value {
        font-size: 28px;
    }

    .card, .form-card {
        padding: 18px;
        border-radius: 18px;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------------------
# HERO
# -------------------------------
st.markdown("""
<div class="hero">
    <h1>🦠 HantaAI Risk Değerlendirme</h1>
    <p>
        Hanta virüsüyle ilgili olası temas, ortam, korunma ve belirti bilgilerini analiz eden
        bilgilendirme amaçlı risk değerlendirme sistemi. Soruları cevaplayarak düşük, orta veya
        yüksek risk sonucunu ve önerilen yönlendirmeleri görebilirsiniz.
    </p>
    <span class="badge">Temas Analizi</span>
    <span class="badge">Belirti Kontrolü</span>
    <span class="badge">Korunma Önerileri</span>
    <span class="badge">Yönlendirme Desteği</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="notice">
    ⚠️ Bu uygulama tıbbi teşhis koymaz. Ciddi belirti, nefes darlığı veya yüksek riskli temas varsa
    en yakın sağlık kuruluşuna başvurulmalıdır.
</div>
""", unsafe_allow_html=True)


# -------------------------------
# INFO SECTIONS
# -------------------------------
info1, info2, info3 = st.columns(3)

with info1:
    st.markdown("""
    <div class="card">
        <h3>Hanta Virüsü Nedir?</h3>
        <p class="muted">
        Hanta virüsleri bazı kemirgenlerde bulunabilen virüslerdir.
        İnsanlar çoğunlukla enfekte kemirgenlerin dışkı, idrar veya tükürük kalıntılarına
        maruz kaldığında risk altında olabilir.
        </p>
    </div>
    """, unsafe_allow_html=True)

with info2:
    st.markdown("""
    <div class="card">
        <h3>Nasıl Risk Oluşur?</h3>
        <p class="muted">
        Depo, bodrum, ahır, köy evi veya uzun süre kapalı kalan alanlarda kemirgen izlerinin
        temizlenmesi sırasında toz kalkması risk değerlendirmesinde önemlidir.
        </p>
    </div>
    """, unsafe_allow_html=True)

with info3:
    st.markdown("""
    <div class="card">
        <h3>Ne Zaman Dikkat?</h3>
        <p class="muted">
        Ateş, halsizlik, kas ağrısı gibi belirtilere ek olarak öksürük veya nefes darlığı varsa
        tıbbi değerlendirme geciktirilmemelidir.
        </p>
    </div>
    """, unsafe_allow_html=True)


# -------------------------------
# FORM
# -------------------------------
st.markdown('<div class="section-title">📋 Risk Değerlendirme Formu</div>', unsafe_allow_html=True)
st.markdown('<p class="muted">Sorular yan tarafta değil, ana sayfa içinde adım adım düzenlenmiştir.</p>', unsafe_allow_html=True)

with st.form("hanta_risk_formu"):
    st.markdown('<div class="form-card">', unsafe_allow_html=True)

    st.markdown("### 1. Ortam ve Temas Bilgileri")
    c1, c2 = st.columns(2)

    with c1:
        kemirgen_goruldu = st.selectbox(
            "Son 2 ay içinde fare/sıçan gibi kemirgen gördünüz mü?",
            ["Hayır", "Evet", "Emin değilim"]
        )

        kemirgen_izi = st.selectbox(
            "Kemirgen dışkısı, idrar izi, yuva veya kemirilmiş eşya gördünüz mü?",
            ["Hayır", "Evet", "Emin değilim"]
        )

        temas_turu = st.selectbox(
            "Kemirgen veya kemirgen iziyle temas şekliniz neydi?",
            [
                "Temas olmadı",
                "Sadece uzaktan gördüm",
                "Yakınında bulundum",
                "Temizlik yaptım",
                "Doğrudan temas ettim",
                "Isırık / çizik oldu"
            ]
        )

    with c2:
        ortam = st.selectbox(
            "Bulunduğunuz ortam hangisine daha yakın?",
            [
                "Şehir merkezi / apartman",
                "Depo / bodrum / garaj",
                "Köy evi / bağ evi",
                "Ahır / çiftlik",
                "Ormanlık veya kırsal alan"
            ]
        )

        kapali_alan = st.selectbox(
            "Uzun süre kapalı kalmış/tozlu bir alanı açtınız veya temizlediniz mi?",
            ["Hayır", "Evet"]
        )

        toz_kalkti = st.selectbox(
            "Temizlik sırasında belirgin şekilde toz kalktı mı?",
            ["Hayır", "Evet", "Emin değilim"]
        )

    st.markdown("---")
    st.markdown("### 2. Korunma Bilgileri")
    c3, c4, c5 = st.columns(3)

    with c3:
        maske = st.selectbox("Maske kullandınız mı?", ["Evet", "Hayır"])
    with c4:
        eldiven = st.selectbox("Eldiven kullandınız mı?", ["Evet", "Hayır"])
    with c5:
        havalandirma = st.selectbox("Temizlik öncesi ortamı havalandırdınız mı?", ["Evet", "Hayır"])

    dezenfekte = st.selectbox(
        "Kemirgen izi olan alanı süpürmeden önce ıslatıp/dezenfekte ettiniz mi?",
        ["Evet", "Hayır", "Böyle bir alan yoktu"]
    )

    st.markdown("---")
    st.markdown("### 3. Zaman ve Belirti Bilgileri")

    temas_gunu = st.slider("Olası temastan kaç gün geçti?", 0, 60, 7)

    b1, b2, b3 = st.columns(3)

    with b1:
        ates = st.checkbox("Ateş")
        halsizlik = st.checkbox("Halsizlik / yorgunluk")
        kas_agrisi = st.checkbox("Kas ağrısı")
        bas_agrisi = st.checkbox("Baş ağrısı")

    with b2:
        bulanti = st.checkbox("Bulantı / kusma")
        karin_agrisi = st.checkbox("Karın ağrısı")
        ishal = st.checkbox("İshal")
        bas_donmesi = st.checkbox("Baş dönmesi")

    with b3:
        oksuruk = st.checkbox("Öksürük")
        nefes_darligi = st.checkbox("Nefes darlığı")
        gogus_sikisma = st.checkbox("Göğüste sıkışma")
        belirtiler_artiyor = st.checkbox("Belirtiler gün geçtikçe artıyor")

    st.markdown("---")
    st.markdown("### 4. Kişisel Durum")
    k1, k2 = st.columns(2)

    with k1:
        yas_grubu = st.selectbox("Yaş grubunuz", ["18 altı", "18-30", "31-45", "46-60", "60+"])
    with k2:
        riskli_durum = st.selectbox(
            "Bağışıklık düşüklüğü, kronik hastalık veya hamilelik gibi ek risk var mı?",
            ["Hayır", "Evet", "Emin değilim"]
        )

    submitted = st.form_submit_button("🔍 Riskimi Değerlendir")

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------
# RISK CALCULATION
# -------------------------------
def risk_hesapla():
    puan = 0
    nedenler = []
    acil = False

    # Temas
    if kemirgen_goruldu == "Evet":
        puan += 2
        nedenler.append("Kemirgen görülmesi temas ihtimalini artırır.")
    elif kemirgen_goruldu == "Emin değilim":
        puan += 1
        nedenler.append("Kemirgen varlığı net olmadığı için düşük düzeyde risk eklendi.")

    if kemirgen_izi == "Evet":
        puan += 4
        nedenler.append("Kemirgen dışkısı/idrar izi/yuva görülmesi önemli risk faktörüdür.")
    elif kemirgen_izi == "Emin değilim":
        puan += 2
        nedenler.append("Kemirgen izi konusunda belirsizlik bulunduğu için dikkat önerilir.")

    if temas_turu == "Yakınında bulundum":
        puan += 1
    elif temas_turu == "Temizlik yaptım":
        puan += 3
        nedenler.append("Kemirgen izi olabilecek alanı temizlemek risk puanını artırdı.")
    elif temas_turu == "Doğrudan temas ettim":
        puan += 4
        nedenler.append("Doğrudan temas bildirilmesi risk puanını belirgin artırdı.")
    elif temas_turu == "Isırık / çizik oldu":
        puan += 6
        acil = True
        nedenler.append("Isırık veya çizik bildirilmesi nedeniyle sağlık kuruluşuna danışılmalıdır.")

    # Ortam
    if ortam == "Depo / bodrum / garaj":
        puan += 2
        nedenler.append("Depo/bodrum/garaj gibi alanlarda kemirgen izi bulunma ihtimali olabilir.")
    elif ortam == "Köy evi / bağ evi":
        puan += 2
        nedenler.append("Köy evi/bağ evi gibi alanlar risk değerlendirmesinde dikkate alındı.")
    elif ortam == "Ahır / çiftlik":
        puan += 3
        nedenler.append("Ahır/çiftlik ortamı kemirgen teması açısından daha dikkatli değerlendirilir.")
    elif ortam == "Ormanlık veya kırsal alan":
        puan += 2
        nedenler.append("Kırsal/ormanlık alan teması risk puanına eklendi.")

    if kapali_alan == "Evet":
        puan += 2
        nedenler.append("Uzun süre kapalı kalan/tozlu alan temizliği risk puanını artırdı.")

    if toz_kalkti == "Evet":
        puan += 3
        nedenler.append("Temizlik sırasında toz kalkması solunum yoluyla maruziyet ihtimalini artırabilir.")
    elif toz_kalkti == "Emin değilim":
        puan += 1

    # Korunma
    if maske == "Hayır":
        puan += 2
        nedenler.append("Maske kullanılmaması koruyuculuğu azaltır.")
    if eldiven == "Hayır":
        puan += 1
        nedenler.append("Eldiven kullanılmaması temas riskini artırabilir.")
    if havalandirma == "Hayır":
        puan += 1
        nedenler.append("Ortamın havalandırılmaması risk puanına eklendi.")
    if dezenfekte == "Hayır":
        puan += 2
        nedenler.append("Kirli alanın süpürmeden önce ıslatılmaması/dezenfekte edilmemesi risk oluşturabilir.")

    # Belirtiler
    belirti_listesi = [
        ates, halsizlik, kas_agrisi, bas_agrisi, bulanti,
        karin_agrisi, ishal, bas_donmesi, oksuruk,
        nefes_darligi, gogus_sikisma, belirtiler_artiyor
    ]
    belirti_sayisi = sum(belirti_listesi)

    puan += belirti_sayisi

    if ates:
        puan += 1
    if kas_agrisi:
        puan += 1
    if oksuruk:
        puan += 2
        nedenler.append("Öksürük solunum belirtisi olduğu için dikkate alındı.")
    if nefes_darligi:
        puan += 6
        acil = True
        nedenler.append("Nefes darlığı ciddi uyarı belirtisidir.")
    if gogus_sikisma:
        puan += 5
        acil = True
        nedenler.append("Göğüste sıkışma ciddi uyarı belirtisi olabilir.")
    if belirtiler_artiyor:
        puan += 4
        nedenler.append("Belirtilerin artması tıbbi değerlendirme gerektirebilir.")

    if belirti_sayisi >= 4:
        puan += 3
        nedenler.append("Birden fazla belirti işaretlendiği için risk puanı yükseldi.")

    # Zaman
    if 7 <= temas_gunu <= 45:
        puan += 2
        nedenler.append("Temas sonrası geçen süre belirti takibi açısından anlamlı aralıktadır.")
    elif temas_gunu > 45:
        puan += 1

    # Kişisel risk
    if yas_grubu in ["18 altı", "60+"]:
        puan += 1
        nedenler.append("Yaş grubu nedeniyle dikkat önerilir.")

    if riskli_durum == "Evet":
        puan += 2
        nedenler.append("Ek sağlık riski bildirildiği için dikkat seviyesi artırıldı.")
    elif riskli_durum == "Emin değilim":
        puan += 1

    temas_riski = (
        (2 if kemirgen_goruldu == "Evet" else 1 if kemirgen_goruldu == "Emin değilim" else 0)
        + (4 if kemirgen_izi == "Evet" else 2 if kemirgen_izi == "Emin değilim" else 0)
        + (6 if temas_turu == "Isırık / çizik oldu" else 4 if temas_turu == "Doğrudan temas ettim" else 3 if temas_turu == "Temizlik yaptım" else 1 if temas_turu == "Yakınında bulundum" else 0)
    )

    ortam_riski = (
        (2 if ortam in ["Depo / bodrum / garaj", "Köy evi / bağ evi", "Ormanlık veya kırsal alan"] else 3 if ortam == "Ahır / çiftlik" else 0)
        + (2 if kapali_alan == "Evet" else 0)
        + (3 if toz_kalkti == "Evet" else 1 if toz_kalkti == "Emin değilim" else 0)
    )

    korunma_riski = (
        (2 if maske == "Hayır" else 0)
        + (1 if eldiven == "Hayır" else 0)
        + (1 if havalandirma == "Hayır" else 0)
        + (2 if dezenfekte == "Hayır" else 0)
    )

    belirti_riski = belirti_sayisi + (6 if nefes_darligi else 0) + (5 if gogus_sikisma else 0)

    if acil:
        seviye = "Yüksek Risk"
        emoji = "🔴"
        css = "high"
        aciklama = "Ciddi uyarı belirtisi veya yüksek riskli temas bildirildi. Gecikmeden sağlık kuruluşuna başvurmanız önerilir."
    elif puan <= 7:
        seviye = "Düşük Risk"
        emoji = "🟢"
        css = "low"
        aciklama = "Yanıtlarınıza göre risk düşük görünüyor. Yine de ortam temizliği ve belirti takibi önemlidir."
    elif puan <= 16:
        seviye = "Orta Risk"
        emoji = "🟡"
        css = "mid"
        aciklama = "Bazı risk faktörleri mevcut. Belirtiler devam ederse veya artarsa sağlık kuruluşuna danışmanız önerilir."
    else:
        seviye = "Yüksek Risk"
        emoji = "🔴"
        css = "high"
        aciklama = "Risk faktörleri ve/veya belirtiler dikkat çekici. Özellikle solunum belirtisi varsa tıbbi destek alınmalıdır."

    guven = min(98, 55 + puan * 2)
    if kemirgen_izi == "Emin değilim" or kemirgen_goruldu == "Emin değilim" or toz_kalkti == "Emin değilim":
        guven -= 8
    guven = max(45, guven)

    return {
        "puan": puan,
        "seviye": seviye,
        "emoji": emoji,
        "css": css,
        "aciklama": aciklama,
        "belirti_sayisi": belirti_sayisi,
        "nedenler": nedenler,
        "temas_riski": temas_riski,
        "ortam_riski": ortam_riski,
        "korunma_riski": korunma_riski,
        "belirti_riski": belirti_riski,
        "guven": guven
    }


sonuc = risk_hesapla()


# -------------------------------
# RESULTS
# -------------------------------
st.markdown('<div class="section-title">📌 Değerlendirme Sonucu</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Risk Seviyesi</div>
        <div class="metric-value">{sonuc["emoji"]} {sonuc["seviye"]}</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Risk Puanı</div>
        <div class="metric-value">{sonuc["puan"]}</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Belirti Sayısı</div>
        <div class="metric-value">{sonuc["belirti_sayisi"]}</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Karar Güveni</div>
        <div class="metric-value">%{sonuc["guven"]}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="card {sonuc["css"]}">
    <div class="result-title">{sonuc["emoji"]} Sonuç: {sonuc["seviye"]}</div>
    <div class="result-text">{sonuc["aciklama"]}</div>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.1, .9])

with left:
    st.markdown('<div class="section-title">🧠 HantaAI Yorumu</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if sonuc["nedenler"]:
        for neden in sonuc["nedenler"]:
            st.markdown(f"<div class='step'>• {neden}</div>", unsafe_allow_html=True)
    else:
        st.write("Belirgin risk faktörü seçilmedi.")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📊 Risk Dağılımı</div>', unsafe_allow_html=True)

    df = pd.DataFrame({
        "Kategori": ["Temas", "Ortam", "Korunma Eksikliği", "Belirti"],
        "Puan": [
            sonuc["temas_riski"],
            sonuc["ortam_riski"],
            sonuc["korunma_riski"],
            sonuc["belirti_riski"]
        ]
    })

    fig = px.bar(
        df,
        x="Kategori",
        y="Puan",
        text="Puan",
        color="Kategori",
        title="Risk faktörlerinin puan dağılımı"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,.04)",
        font=dict(color="white"),
        title_font=dict(size=20),
        xaxis_title="",
        yaxis_title="Puan",
        legend_title=""
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown('<div class="section-title">🚨 Yönlendirme</div>', unsafe_allow_html=True)

    if sonuc["seviye"] == "Yüksek Risk":
        st.markdown("""
        <div class="card high">
            <h3>Sağlık kuruluşuna başvurun</h3>
            <p class="result-text">
            Özellikle nefes darlığı, göğüs sıkışması, artan belirtiler veya doğrudan temas varsa
            gecikmeden sağlık kuruluşuna başvurulmalıdır.
            </p>
        </div>
        """, unsafe_allow_html=True)

    elif sonuc["seviye"] == "Orta Risk":
        st.markdown("""
        <div class="card mid">
            <h3>Belirti takibi yapın</h3>
            <p class="result-text">
            Belirtiler devam ederse, artarsa veya solunum belirtisi eklenirse sağlık kuruluşuna danışın.
            </p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="card low">
            <h3>Genel önlem yeterli olabilir</h3>
            <p class="result-text">
            Risk düşük görünse de kemirgen kontrolü, güvenli temizlik ve belirti takibi sürdürülmelidir.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🧼 Korunma Önerileri</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="step">1. Kemirgen izi olan alanları kuru süpürmeyin.</div>
        <div class="step">2. Temizlik öncesinde ortamı havalandırın.</div>
        <div class="step">3. Maske ve eldiven kullanın.</div>
        <div class="step">4. Toz kaldırmamaya dikkat edin.</div>
        <div class="step">5. Gıda ve çöpleri açıkta bırakmayın.</div>
        <div class="step">6. Kemirgen giriş noktalarını kapatın.</div>
    </div>
    """, unsafe_allow_html=True)


# -------------------------------
# EXTRA EXPLANATION
# -------------------------------
st.markdown('<div class="section-title">📚 Bilgilendirme Bölümü</div>', unsafe_allow_html=True)

with st.expander("🦠 Hanta virüsü hakkında kısa bilgi"):
    st.write("""
    Hanta virüsleri bazı kemirgenlerde bulunabilir. İnsanlar, kemirgenlerin idrar, dışkı veya
    tükürük kalıntılarıyla kirlenmiş ortamlarla temas ettiğinde risk altında olabilir.
    Bu uygulama, verilen cevaplara göre eğitim amaçlı risk sınıflandırması yapar.
    """)

with st.expander("🧹 Güvenli temizlik neden önemli?"):
    st.write("""
    Kapalı, tozlu ve kemirgen izi olan alanlarda kuru süpürme veya toz kaldırma riskli kabul edilir.
    Bu nedenle havalandırma, maske, eldiven ve dikkatli temizlik önemlidir.
    """)

with st.expander("🏥 Hangi durumda doktora gidilmeli?"):
    st.write("""
    Nefes darlığı, göğüste sıkışma, yüksek ateş, giderek artan halsizlik veya kemirgen teması sonrası
    birden fazla belirti varsa sağlık kuruluşuna başvurulmalıdır.
    """)

with st.expander("📌 Projede kullanılan yöntem"):
    st.write("""
    Bu projede kural tabanlı risk puanlama sistemi kullanılmıştır. Kullanıcının cevapları temas,
    ortam, korunma ve belirti gruplarına ayrılır. Her faktör puanlanır ve toplam puana göre
    düşük, orta veya yüksek risk sonucu oluşturulur.
    """)

st.markdown("""
<div class="footer-box">
    HantaAI Risk Değerlendirme Sistemi • Eğitim amaçlı proje • Tıbbi teşhis yerine geçmez
</div>
""", unsafe_allow_html=True)
