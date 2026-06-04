import requests
from requests.exceptions import Timeout, RequestException
from services.fallback_manager import fallback_response

API_URL ="https://httpstat.us/200?sleep=15000"

MAX_RETRIES = 3
TIMEOUT_SECONDS = 10


def call_ai_service(data):
    """
    Handles timeout, retry, and fallback logic.
    """

    for attempt in range(MAX_RETRIES):

        try:
            response = requests.post(
                API_URL,
                json=data,
                timeout=TIMEOUT_SECONDS
            )

            response.raise_for_status()

            return {
                "status": "success",
                "data": response.json()
            }

        except Timeout:
            print(f"Timeout occurred. Retry {attempt+1}/{MAX_RETRIES}")

        except RequestException as e:
            print(f"Request failed: {e}")

    return fallback_response("AI Service")