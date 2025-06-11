from SmartApi.smartConnect import SmartConnect
import pyotp
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
CLIENT_CODE = os.getenv("CLIENT_CODE")
PASSWORD = os.getenv("PASSWORD")
TOTP_SECRET = os.getenv("TOTP_SECRET")

def get_totp_token(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

def login():
    smartApi = SmartConnect(API_KEY)
    totp = get_totp_token(TOTP_SECRET)
    data = smartApi.generateSession(CLIENT_CODE, PASSWORD, totp)

    if data['status'] == False:
        print("Login failed:", data)
        return None

    print("Login successful!")
    return smartApi

if __name__ == "__main__":
    smartApi = login()
