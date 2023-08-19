import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28185220")

API_HASH = os.environ.get("API_HASH", "7775088403abbe110d5a38cfc75addce")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6186689074:AAE-QC_SF682gMoOcWbgH6OoOeNLOpPSzm0") 

FORCE_SUB = os.environ.get("FORCE_SUB", "QTVS_BOT_X_CLOUD") 

DB_NAME = os.environ.get("DB_NAME","kamaran1")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://hillsking1222:kuraman1@kumaran1.d6ahc05.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/0be9278fd31679386f55c.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '885675538').split()]

PORT = os.environ.get("PORT", "8080")
