"""
Censys IPv4 Search Tool

Created on : 12-11-2018
Created by : Saurabh Modi

Asks for an IP address or website name, searches it through the Censys API,
prints the raw JSON response on screen and also saves the results to
Result.csv.
"""

import csv
import json
import os
import sys

import requests

API_URL = "https://censys.io/api/v1"
OUTPUT_FILE = "Result.csv"


class CensysSearch:
   
    def __init__(self, api_id, api_secret):
        self.api_id = api_id
        self.api_secret = api_secret

    def search_ipv4(self, query):
        #Query Censys and return the reply as parsed JSON
        payload = {"query": query}
        response = requests.post(
            API_URL + "/search/ipv4",
            json=payload,
            auth=(self.api_id, self.api_secret),
            timeout=30,
        )

        #Status other than 200 means Censys rejected the request.
        if response.status_code != 200:
            print("Error occurred... (HTTP " + str(response.status_code) + ")\n")
            sys.exit(1)

        return response.json()


def save_to_csv(results, file_name):
    
    if not results:
        print("No results found.")
        return

    ##List every distinct column, in the order first seen    
    columns = []
    for item in results:
        for key in item.keys():
            if key not in columns:
                columns.append(key)

    with open(file_name, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(results)

    print("Results saved to " + file_name)


def main():
    api_id = os.environ.get("CENSYS_API_ID")
    api_secret = os.environ.get("CENSYS_API_SECRET")

    if not api_id or not api_secret:
        print("Please set CENSYS_API_ID and CENSYS_API_SECRET first.")
        sys.exit(1)

    query = input("Enter IP address / website name (eg. 10.2.13.45 or google.com):\t").strip()
    if not query:
        print("No input provided.")
        sys.exit(1)

    data = CensysSearch(api_id, api_secret).search_ipv4(query)

    # Show the full response on screen and save the result.
    print(json.dumps(data, indent=2))
    save_to_csv(data.get("results", []), OUTPUT_FILE)


if __name__ == "__main__":
    main()
