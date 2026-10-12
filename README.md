# Ollama AI Service with Streamlit

Aplikasi AI lokal berbasis web yang menggunakan Ollama untuk menjalankan model AI dan Streamlit sebagai antarmuka pengguna. Aplikasi ini memungkinkan pengguna mengirim pertanyaan dan menerima jawaban dari model AI melalui browser.

## Technologies Used

- Python
- Ollama
- Streamlit
- Requests
- Llama 3.2

## How to Run

### 1. Install Ollama

Unduh dan instal Ollama untuk Windows melalui situs resmi:

https://ollama.com/download/windows

### 2. Download the AI Model

Jalankan perintah berikut untuk mengunduh model Llama 3.2:

```powershell
ollama run llama3.2
```

Setelah model berhasil dijalankan, coba kirim pertanyaan untuk memastikan model dapat memberikan jawaban. Ketik `/bye` untuk keluar dari sesi percakapan.

### 3. Create the Project Folder

Buka PowerShell dan jalankan:

```powershell
cd $HOME\Downloads
mkdir ollama
cd ollama
```

Jika folder proyek sudah tersedia, langsung buka terminal pada folder tersebut.

### 4. Create a Python Virtual Environment

Buat lingkungan virtual Python:

```powershell
python -m venv .venv
```

Aktifkan lingkungan virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

Instal Streamlit dan Requests:

```powershell
python -m pip install --upgrade pip
pip install streamlit requests
```

### 6. Create the Application

Buat file bernama `app.py` di dalam folder proyek.

Salin kode aplikasi Streamlit yang menghubungkan antarmuka web ke Ollama API ke dalam file tersebut.

Pastikan nama model pada kode adalah `llama3.2` dan alamat API yang digunakan adalah:

```text
http://localhost:11434/api/chat
```

### 7. Start Ollama Service

Pastikan Ollama sudah berjalan di komputer.

Untuk memeriksa API, buka browser:

http://localhost:11434

Jika muncul pesan `Ollama is running`, layanan sudah merespons.

Jika layanan belum berjalan, buka terminal terpisah dan jalankan:

```powershell
ollama serve
```

Jika layanan sudah berjalan, langkah ini tidak perlu dilakukan lagi.

### 8. Run the Streamlit Application

Buka terminal pada folder proyek, aktifkan virtual environment jika belum aktif, kemudian jalankan:

```powershell
python -m streamlit run app.py
```

Tunggu hingga server Streamlit berjalan.

### 9. Open the Application

Buka browser dan akses alamat berikut:

http://localhost:8501

Aplikasi Ollama AI Service siap digunakan. Masukkan pertanyaan pada kolom chat untuk mendapatkan jawaban dari model AI.

