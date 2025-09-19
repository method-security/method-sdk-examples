import os

from dotenv import load_dotenv
from method_security import MethodClient


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get credentials from environment variables
    client_id = os.getenv("OAUTH_CLIENT_ID")
    client_secret = os.getenv("OAUTH_CLIENT_SECRET")
    method_url = os.getenv("METHOD_URL")

    print("Hello from method-sdk-python-example!")
    print(f"Client ID loaded: {'✓' if client_id else '✗'}")
    print(f"Client Secret loaded: {'✓' if client_secret else '✗'}")
    print(f"URL: {method_url}")

    if client_id and client_secret and client_id != "your_client_id_here":
        # Initialize MethodSecurity client
        try:
            client = MethodClient(
                base_url=method_url,
                client_id=client_id,
                client_secret=client_secret,
            )
            print("MethodSecurity client initialized successfully!")

            # Example API call (only if credentials are real)
            try:
                issue_details = client.v1.issues.get_issue(id="<Issue Id>")
                print("Issue details:", issue_details)
            except Exception as e:
                print(f"API call failed (this is expected with demo credentials): {e}")

        except Exception as e:
            print(f"Error initializing client: {e}")
    else:
        print("Please set real CLIENT_ID and CLIENT_SECRET in your .env file")
        print("Current values are placeholder credentials")


if __name__ == "__main__":
    main()
