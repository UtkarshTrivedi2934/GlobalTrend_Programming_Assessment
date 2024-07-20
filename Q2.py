"""2. **Write a Python function that takes a list of URLs, attempts to download their content, and retries up to 3 times if an error occurs. Use appropriate error handling to manage different types of exceptions.**"""

import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

def download_content(urls):
    contents = {}
    for url in urls:
        attempts = 0
        success = False
        while attempts < 3 and not success:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                contents[url] = response.text
                success = True
            except HTTPError as http_err:
                print(f"HTTP error occurred: {http_err} - URL: {url}")
            except ConnectionError as conn_err:
                print(f"Connection error occurred: {conn_err} - URL: {url}")
            except Timeout as timeout_err:
                print(f"Timeout error occurred: {timeout_err} - URL: {url}")
            except RequestException as req_err:
                print(f"Error occurred: {req_err} - URL: {url}")
            finally:
                attempts += 1
                if not success and attempts < 3:
                    print(f"Retrying {url} (attempt {attempts + 1})...")

        if not success:
            contents[url] = None
            print(f"Failed to retrieve {url} after 3 attempts")

    return contents

# Example usage:
urls = [
    "https://www.example.com",
    "https://www.nonexistentwebsite.com",  # This will fail
    "https://www.google.com"
]

result = download_content(urls)
for url, content in result.items():
    if content:
        print(f"Content from {url[:30]}...: {content[:100]}")  # Print first 100 characters of the content
    else:
        print(f"No content retrieved from {url}")
