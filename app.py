import streamlit as st

st.set_page_config(
    page_title="ExamReady App",
    page_icon="📘",
    layout="centered"
)

st.title("📘 ExamReady App")
st.subheader("Prediksi Kesiapan Ujian Mahasiswa")

st.write(
    "Aplikasi ini memprediksi tingkat kesiapan ujian mahasiswa "
    "berdasarkan jam belajar, kualitas tidur, tingkat stres, latihan soal, dan kehadiran kelas."
)

st.divider()

st.header("Input Data")

jam_belajar = st.slider("Jam belajar per hari", 0, 10, 3)
kualitas_tidur = st.slider("Kualitas tidur", 1, 10, 7)
tingkat_stres = st.slider("Tingkat stres", 1, 10, 5)
latihan_soal = st.slider("Jumlah latihan soal", 0, 100, 30)
kehadiran = st.slider("Kehadiran kelas (%)", 0, 100, 80)

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
    saran = "Tingkatkan jam belajar, perbanyak latihan soal, dan kelola stres dengan lebih baik."
elif skor_kesiapan < 75:
    kategori = "Cukup Siap"
    saran = "Kamu cukup siap, tetapi masih perlu memperbaiki beberapa aspek sebelum ujian."
else:
    kategori = "Siap"
    saran = "Kamu sudah siap mengikuti ujian. Pertahankan pola belajar dan istirahat yang cukup."

st.divider()

st.header("Hasil Prediksi")

st.metric("Skor Kesiapan", f"{skor_kesiapan}/100")

if kategori == "Belum Siap":
    st.error(f"Kategori: {kategori}")
elif kategori == "Cukup Siap":
    st.warning(f"Kategori: {kategori}")
else:
    st.success(f"Kategori: {kategori}")

st.info(saran)

st.divider()

st.caption("Aplikasi ini menggunakan metode rule-based scoring dan dapat dikembangkan menjadi model machine learning.")
