from dotenv import load_dotenv
import os
load_dotenv()

BASE_URL = os.getenv("OASIS_BASE_URL")
LOGIN_URL = os.getenv("OASIS_LOGIN_URL")
GUEST_EMAIL = os.getenv("GUEST_EMAIL")
INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")
LOGIN_ERROR_MESSAGE = "Login FailedInvalid email or password. Please try again."

