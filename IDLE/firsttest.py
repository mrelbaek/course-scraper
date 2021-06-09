#  Install the Python Requests library:
# `pip install requests`
import requests

def send_request():
    response = requests.get(
        url="https://app.scrapingbee.com/api/v1/",
        params={
            "api_key": "Z0M90OBII7BXWSB2JFZR0AR9TDPM7FNO5IP17JBBFCY5AGDKHH0NIPRZDMWYSB8CEBT79PCSF6UYYM31",
            "url": "https://www.maersktraining.com/b2c-course-category/oil-gas/",
        },

    )
    print('Response HTTP Status Code: ', response.status_code)
    print('Response HTTP Response Body: ', response.content)
send_request()
