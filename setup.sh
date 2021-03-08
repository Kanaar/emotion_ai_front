mkdir -p ~/.streamlit/

echo "[general]
email = vandenbroek.rp@gmail.com
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableXsrfProtection = false
enableCORS = false
" > ~/.streamlit/config.toml
