import pickle
import os
import base64
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string
import random

def random_code(length):
    LETTERS = string.ascii_letters
    DIGITS = string.digits  
    x = list(f'{LETTERS}{DIGITS}')
    random.shuffle(x)
    code = random.choices(x, k = length)
    code = ''.join(code)
    return(code)
def Create_Service(client_secret_file, api_name, api_version, *scopes):
    print(client_secret_file, api_name, api_version, scopes, sep="-")
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    cred = None

    pickle_file = f"token_{API_SERVICE_NAME}_{API_VERSION}.pickle"

    if os.path.exists(pickle_file):
        with open(pickle_file, "rb") as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, "wb") as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, "service created successfully")
        return service
    except Exception as e:
        print("Unable to connect!")
        print(e)
        return None

def sendEmail():
    CLIENT_SECRET_FILE = "a.json"
    API_NAME = "gmail"
    API_VERSION = "v1"
    SCOPES = ["https://mail.google.com/"]

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    emailMsg = random_code(length = 12)
    mimeMessage = MIMEMultipart()
    mimeMessage["to"] = "nguyenducthang150909@gmail.com"     
    mimeMessage["subject"] = "Authentic"
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(userId="me", body={"raw": raw_string}).execute()
sendEmail()