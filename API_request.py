# -*- coding: utf-8 -*-

'''

'''

import requests, json, creds, sys
import pandas as pd


def finishProcedure():
    message = "\n\nProgram has finished successfully :)\n@0xPinillos"
    print(message)
    return sys.exit()


def responseFormatter(response:bytes) -> str: # Removes datatype bytes' characters
    rp = str(response)
    rp = rp.lstrip("b'")
    rp = rp.rstrip("'")
    return rp # returns a full string variable


def api_get_request(url: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.get(url, headers=headers, timeout=38) # HTTP GET request to reach data
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        contentResponse = response.content
        contentResponse = responseFormatter(contentResponse)
        api_content = open("xml_api_response.xml", mode="w") # Field entity
        api_content.write(contentResponse)
        api_content.close()
        return contentResponse

    # Exceptions to handle different error may occur during execution.
    # Return None to handle through all code flow
    except requests.exceptions.RequestException as e:
        print(f"\n\nError fetching data from {url}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"\n\nError decoding JSON from {url}: {e}")
        return None
    except ValueError as e:
        print(f"\n\nValue Error: {e}")
        return None
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: {e}")
        return None


def main():
    spotifyData = api_get_request(creds.urlApi, creds.authenticationToken) # API data on XML formatt
    print(spotifyData)
    if spotifyData != None: pass
    else: finishProcedure()
   

if __name__ == "__main__":
    main()