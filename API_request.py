import requests, json, creds

def api_get_request(url: str, token: str) -> dict[str, any]:
    headers = {
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.get(url, headers=headers, timeout=38)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        contentResponse = response.content
        return contentResponse

    except requests.exceptions.RequestException as e:
        print(f"\nError fetching data from {url}: {e}")
        return {}  # Return empty dict on error, or you may choose to raise the exception.
    except json.JSONDecodeError as e:
        print(f"\nError decoding JSON from {url}: {e}")
        return {}
    except ValueError as e:
        print(f"\nValue Error: {e}")
        return {}
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return {}


def main():
    data = api_get_request(creds.urlApi, creds.authenticationToken)
    print(data)


if __name__ == "__main__":
    main()