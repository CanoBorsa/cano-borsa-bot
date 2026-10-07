import os
import time
import requests

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def telegram_mesaj_gonder(mesaj):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": mesaj
        }
    )

def tarama_yap():
    # İlk test aşaması
    mesaj = (
        "📊 CANO BORSA BOT\n\n"
        "🟢 Bot çalışıyor!\n"
        "🇹🇷 BIST taraması hazırlanıyor.\n"
        "⏱️ Tarama aralığı: 5 dakika\n\n"
        "⚠️ Bu aşamada gerçek alım-satım yapılmaz."
    )

    telegram_mesaj_gonder(mesaj)

while True:
    try:
        tarama_yap()
        time.sleep(300)

    except Exception as hata:
        print("Hata:", hata)
        time.sleep(60)
