mkdir -p ~/.streamlit/

echo "[general]
email = \"bruno.sp.prates@gmail.com\"
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
enableXsrfProtection = false
" > ~/.streamlit/config.toml
