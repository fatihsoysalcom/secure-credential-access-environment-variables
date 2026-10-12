import os

def demonstrate_credential_management():
    print("--- Credential Management Demonstration ---")

    # BAD PRACTICE: Hardcoding credentials directly in code
    # This is highly insecure and should NEVER be done in production.
    # It exposes sensitive information if the code is leaked (e.g., via Git).
    hardcoded_db_password = "my_super_secret_hardcoded_password_123!"
    print(f"\n[BAD PRACTICE] Hardcoded Database Password: {hardcoded_db_password}")
    print("WARNING: This password is directly visible in the source code and version control.")

    # GOOD PRACTICE: Retrieving credentials from environment variables
    # This keeps sensitive data out of your source code and version control.
    # It allows different credentials for different environments (dev, test, prod)
    # without changing the application code itself.
    env_db_password = os.getenv("DATABASE_PASSWORD")

    if env_db_password:
        print(f"\n[GOOD PRACTICE] Database Password from Environment Variable: {env_db_password}")
        print("This password is NOT visible in the source code.")
    else:
        print("\n[GOOD PRACTICE] DATABASE_PASSWORD environment variable not set.")
        print("Please set the DATABASE_PASSWORD environment variable to see this in action.")
        print("Example (Linux/macOS Bash): export DATABASE_PASSWORD='your_secure_password_from_env'")
        print("Example (Windows PowerShell): $env:DATABASE_PASSWORD='your_secure_password_from_env'")

    print("\n--- End of Demonstration ---")
    print("Always prefer environment variables or dedicated secret management services (like AWS Secrets Manager) for sensitive data.")

if __name__ == "__main__":
    demonstrate_credential_management()
