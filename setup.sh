mkdir -p ~/.streamlit/

echo "[general]
email = vandenbroek.rp@gmail.com
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
enableXsrfProtection = false
" > ~/.streamlit/config.toml
