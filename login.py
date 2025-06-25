from SmartApi.smartConnect import SmartConnect
import pyotp
import os

# 🔹 Load credentials from environment variables
API_KEY = os.getenv("API_KEY")
CLIENT_CODE = os.getenv("CLIENT_CODE")
PASSWORD = os.getenv("PASSWORD")
TOTP_SECRET = os.getenv("TOTP_SECRET")

def get_totp_token(secret):
    try:
        totp = pyotp.TOTP(secret)
        return totp.now()
    except Exception as e:
        print("❌ Error generating TOTP:", e)
        return None

def login():
    if not all([API_KEY, CLIENT_CODE, PASSWORD, TOTP_SECRET]):
        print("❌ Missing environment variables for login.")
        return None

    try:
        smartApi = SmartConnect(api_key=API_KEY)
        totp = get_totp_token(TOTP_SECRET)

        if not totp:
            print("❌ TOTP generation failed.")
            return None

        data = smartApi.generateSession(CLIENT_CODE, PASSWORD, totp)

        if not data.get('status'):
            print("❌ Login failed:", data)
            return None

        print("✅ Login successful!")
        return smartApi

    except Exception as e:
        print("❌ Exception during login:", e)
        return None