from dotenv import load_dotenv
import os


load_dotenv(override=True)

'''если этих переменных не будет в .env, то использую значение отсюда'''
AUTH_SERVICE_URL = os.getenv(
    'AUTH_SERVICE_API_URL',
    'http://127.0.0.1:8000'
)

UNIVERSITY_SERVICE_URL = os.getenv(
    'UNIVERSITY_SERVICE_API_URL',
    'http://127.0.0.1:8001'
)
TEST_USERNAME = os.getenv(
    'TEST_USERNAME',
    "example"
)
TEST_PASSWORD = os.getenv(
    'TEST_PASSWORD',
    "P@ssw0rd123!"
)