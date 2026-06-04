import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fallback_response(service_name):
    logging.error(f"{service_name} failed. Using fallback.")

    return {
        "status": "fallback",
        "message": f"{service_name} is currently unavailable. Please try again later."
    }