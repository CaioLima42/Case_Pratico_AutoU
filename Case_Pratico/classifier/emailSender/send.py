import smtplib
import email.message
import os
from dotenv import load_dotenv
from pathlib import Path
import re


def getAdmEmail() -> str:
    env_path = Path(__file__).resolve().parent.parent.parent.parent / '.envs'
    load_dotenv(dotenv_path=env_path / '.env')
    api_key = os.getenv("EMAIL_ADM_ADRESS")
    return api_key

def gerAdmPassWorld() -> str:
    env_path = Path(__file__).resolve().parent.parent.parent.parent / '.envs'
    load_dotenv(dotenv_path=env_path / '.env')
    api_key = os.getenv("EMAIL_ADM_PASSWORD")
    return api_key

def sendEmail(subject: str, msg: str, to: str) -> bool:
        try:
            sender = email.message.Message()
            sender['Subject'] = subject
            sender['From'] = getAdmEmail()
            sender['To'] = to
            password = gerAdmPassWorld()
            sender.add_header('Content-Type', 'text/html')
            sender.set_payload(msg)
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            msg = re.sub(r'<[^>]+>', '', msg)
            s.login(sender['From'], password)
            s.sendmail(sender['From'],[sender['To']], msg.encode('utf-8'))
            return True
        except:
             return False
