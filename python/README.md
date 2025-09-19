# Python Method SDK Example

This directory contains a Python implementation using the `methodsdk` package.

## Setup

1. **Install UV** (if not already installed):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install dependencies**:

   ```bash
   cd python
   uv sync
   ```

3. **Configure environment**:
   Copy and edit the `.env` file with your credentials:
   ```bash
   cp .env .env.local  # Optional: use .env.local for local overrides
   # Edit .env with your actual CLIENT_ID and CLIENT_SECRET
   ```

## Running

```bash
# From the python directory
uv run main.py
```

## Environment Variables

The Method Client can transparently pull the OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET environment variables without direct configuration. This example shows how to directly configure it, by pulling it from the same environment variables. However, you can inject those variables however you manage secrets.

- `OAUTH_CLIENT_ID`: Your Method Security client ID
- `OAUTH_CLIENT_SECRET`: Your Method Security client secret
- `METHOD_URL`: API endpoint URL

## Dependencies

- **methodsdk**: Method Security Python SDK
- **python-dotenv**: Environment variable loading from .env files

## Project Structure

```
python/
├── main.py          # Main example script
├── pyproject.toml   # UV project configuration
├── .env             # Environment variables (template)
├── .venv/          # Virtual environment (auto-generated)
└── README.md       # This file
```

## Example Usage

The `main.py` file demonstrates:

- Loading environment variables from `.env`
- Initializing the Method Security client
- Making a basic API call to get issue details

## Security

- Never commit actual credentials
- The `.env` file should be added to `.gitignore`
- Consider using `.env.local` for local development overrides
