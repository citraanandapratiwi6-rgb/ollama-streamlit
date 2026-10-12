
import streamlit as st
import requests

# Konfigurasi aplikasi
st.set_page_config(
    page_title="Ollama AI Service",
    page_icon="🤖",
    layout="centered"
)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

st.title("🤖 Ollama AI Service")
st.write("Aplikasi AI lokal menggunakan Ollama dan Streamlit.")

# Menyimpan riwayat percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan riwayat percakapan
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kolom input pertanyaan
prompt = st.chat_input("Ketik pertanyaan kamu...")

if prompt:
    # Simpan dan tampilkan pertanyaan pengguna
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Kirim permintaan ke Ollama Service
    with st.chat_message("assistant"):
        with st.spinner("Ollama sedang memproses..."):
            try:
                response = requests.post(
                    OLLAMA_URL,
                    json={
                        "model": MODEL,
                        "messages": st.session_state.messages,
                        "stream": False
                    },
                    timeout=300
                )

                response.raise_for_status()
                result = response.json()
                answer = result["message"]["content"]

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except requests.exceptions.ConnectionError:
                st.error(
                    "Tidak dapat terhubung ke Ollama. "
                    "Pastikan Ollama Service sedang berjalan."
                )

            except requests.exceptions.Timeout:
                st.error(
                    "Waktu pemrosesan habis. "
                    "Coba lagi atau gunakan model yang lebih ringan."
                )

            except requests.exceptions.RequestException as error:
                st.error(f"Terjadi kesalahan API: {error}")

            except (KeyError, ValueError):
                st.error("Respons Ollama tidak sesuai format yang diharapkan.")
