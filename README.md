# 🧠 Mental Health Detection System

Mental Health Detection System merupakan aplikasi berbasis Artificial Intelligence (AI) yang digunakan untuk melakukan skrining awal kondisi kesehatan mental pengguna.

Sistem ini menggabungkan dua metode deteksi:

## 1. Questionnaire Detection

Deteksi dilakukan berdasarkan jawaban kuisioner yang diisi oleh pengguna.

Model yang digunakan:

- Stress Detection
- Depression Detection
- Anxiety Detection

Ketiga model tersebut dibangun menggunakan algoritma **Logistic Regression** dari **Scikit-Learn**.

Output yang dihasilkan berupa prediksi kondisi pengguna berdasarkan jawaban kuisioner yang diberikan.

---

## 2. NLP Detection

Selain kuisioner, sistem juga menyediakan deteksi berbasis teks (Natural Language Processing).

Pengguna dapat menuliskan perasaan, pengalaman, atau kondisi yang sedang dialami, kemudian sistem akan melakukan analisis menggunakan model **Transformer berbasis PyTorch**.

Model NLP digunakan untuk memahami konteks kalimat dan mendeteksi indikasi kondisi kesehatan mental berdasarkan teks yang diberikan pengguna.

---

## Teknologi yang Digunakan

### Backend

- FastAPI
- Scikit-Learn
- PyTorch
- Transformers
- Uvicorn

### Frontend

- React.js
- Axios
- Vite

---

## Instalasi Backend

Masuk ke folder backend:

```bash
cd backend
```

Install seluruh dependency:

```bash
pip install -r requirements.txt
```

Jalankan server FastAPI:

```bash
uvicorn app.main:app --reload
```

atau sesuaikan dengan entry point project:

```bash
uvicorn main:app --reload
```

Backend akan berjalan pada:

```text
http://localhost:8000
```

Dokumentasi API:

```text
http://localhost:8000/docs
```

---

## Instalasi Frontend

Masuk ke folder frontend:

```bash
cd frontend
```

Install dependency:

```bash
npm install
```

Jalankan aplikasi:

```bash
npm run dev
```

Frontend akan berjalan pada:

```text
http://localhost:5173
```

---

## Konfigurasi API

Seluruh komunikasi antara frontend dan backend dilakukan melalui file:

```text
src/service/api.js
```

File tersebut digunakan untuk melakukan request ke endpoint FastAPI dan mengelola seluruh pemanggilan API dari frontend.

---

## Disclaimer

Sistem ini dibuat untuk tujuan edukasi dan skrining awal kesehatan mental. Hasil prediksi yang diberikan bukan merupakan diagnosis medis dan tidak dapat menggantikan konsultasi dengan psikolog maupun psikiater profesional.