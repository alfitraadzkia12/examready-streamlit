import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ExamReady App",
    page_icon="📘",
    layout="centered"
)

st.title("📘 ExamReady App")
st.markdown("### Prediksi Kesiapan Ujian Mahasiswa")

st.write(
    "Aplikasi ini membantu memprediksi tingkat kesiapan mahasiswa dalam menghadapi ujian "
    "berdasarkan jam belajar, kualitas tidur, tingkat stres, latihan soal, dan kehadiran kelas."
)

st.divider()

st.header("📥 Input Data Mahasiswa")

jam_belajar = st.slider("Jam belajar per hari", 0, 10, 3)
kualitas_tidur = st.slider("Kualitas tidur", 1, 10, 7)
tingkat_stres = st.slider("Tingkat stres", 1, 10, 5)
latihan_soal = st.slider("Jumlah latihan soal", 0, 100, 30)
kehadiran = st.slider("Kehadiran kelas (%)", 0, 100, 80)

if st.button("Prediksi Sekarang"):
    skor_jam_belajar = (jam_belajar / 10) * 100
    skor_tidur = (kualitas_tidur / 10) * 100
    skor_stres = ((10 - tingkat_stres) / 9) * 100
    skor_latihan = latihan_soal
    skor_kehadiran = kehadiran

    skor_kesiapan = (
        skor_jam_belajar * 0.25 +
        skor_tidur * 0.20 +
        skor_stres * 0.20 +
        skor_latihan * 0.20 +
        skor_kehadiran * 0.15
    )

    skor_kesiapan = round(skor_kesiapan, 2)

    if skor_kesiapan < 50:
        kategori = "Belum Siap"
        saran = "Tingkatkan jam belajar, perbanyak latihan soal, perbaiki kualitas tidur, dan kelola stres dengan lebih baik."
        status = "danger"
    elif skor_kesiapan < 75:
        kategori = "Cukup Siap"
        saran = "Kamu cukup siap, tetapi masih perlu memperbaiki beberapa aspek sebelum ujian."
        status = "warning"
    else:
        kategori = "Siap"
        saran = "Kamu sudah siap mengikuti ujian. Pertahankan pola belajar dan istirahat yang cukup."
        status = "success"

    st.divider()
    st.header("📊 Hasil Prediksi")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Skor Kesiapan", f"{skor_kesiapan}/100")

    with col2:
        st.metric("Kategori", kategori)

    if status == "danger":
        st.error(f"Kategori: {kategori}")
    elif status == "warning":
        st.warning(f"Kategori: {kategori}")
    else:
        st.success(f"Kategori: {kategori}")

    st.info(saran)

    st.subheader("📌 Rincian Skor Aspek")

    data = {
        "Aspek": [
            "Jam Belajar",
            "Kualitas Tidur",
            "Manajemen Stres",
            "Latihan Soal",
            "Kehadiran"
        ],
        "Skor": [
            skor_jam_belajar,
            skor_tidur,
            skor_stres,
            skor_latihan,
            skor_kehadiran
        ]
    }

    df = pd.DataFrame(data)

    st.bar_chart(df.set_index("Aspek"))

st.divider()
st.caption("ExamReady App | Rule-Based Scoring | Dibuat dengan Python dan Streamlit")
