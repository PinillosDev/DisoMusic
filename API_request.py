import requests, json, creds, sys

def finishProcedure():
    message = "\n\nProgram has finished.\n@0xPinillos"
    print(message)
    return sys.exit()


def api_get_request(url: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.get(url, headers=headers, timeout=38) # HTTP GET request to reach data
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        contentResponse = response.content
        return contentResponse

    # Exceptions to handle different error may occur during execution.
    # Return None to handle through all code flow
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching data from {url}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"\nError decoding JSON from {url}: {e}")
        return None
    except ValueError as e:
        print(f"\nValue Error: {e}")
        return None
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return None


def main():
    data = api_get_request(creds.urlApi, creds.authenticationToken)
    if data != None: pass
    else: finishProcedure()
    print(data)


if __name__ == "__main__":
    main()