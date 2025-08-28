import socket
import streamlit as st

st.set_page_config(page_title="🚀 SuperScan", layout="wide")

st.title("🚀 SuperScan")
st.write("Verifique rapidamente se portas estão abertas em um host.")

host = st.text_input("Host", "example.com")
ports_input = st.text_input("Portas (separadas por vírgula)", "80")

if st.button("Verificar"):
    ports = [int(p.strip()) for p in ports_input.split(",") if p.strip().isdigit()]
    st.write("✅ SuperScan conectado com sucesso!")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                st.success(f"Porta {port} aberta em {host}.")
            else:
                st.error(f"Porta {port} fechada em {host}.")
