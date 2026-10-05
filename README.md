# Censys IPv4 Search

Searches an IP address or website name using the Censys API, prints the JSON response and saves the results to `Result.csv`.

**Created by:** Saurabh Modi
**Created on:** 11-03-2018

## Installation

```bash
pip install -r requirements.txt
```

## Setup

Get your API ID and secret from your Censys account and set them as environment variables:

```bash
export CENSYS_API_ID="your-api-id"
export CENSYS_API_SECRET="your-api-secret"
```

(On Windows: `set CENSYS_API_ID=...`)

## Usage

```bash
python censys_lookup.py
```

Enter an IP (e.g. `10.2.13.45`) or a name (e.g. `google.com`) when asked.

## Notes

- Never commit your API credentials. `.env` is already in `.gitignore`.
- The Censys v1 API used here has since been superseded by newer API versions, so the endpoint may need updating for current accounts.

## License

MIT
