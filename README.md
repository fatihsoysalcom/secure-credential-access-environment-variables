# Secure Credential Access Environment Variables

This example demonstrates the critical difference between hardcoding sensitive credentials directly into your application code and securely retrieving them from environment variables. Hardcoding is a major security risk, while using environment variables is a fundamental step towards secure credential management, especially in cloud environments like AWS.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. (Optional, but recommended for demonstration) Set the environment variable: `export DATABASE_PASSWORD='my_secure_password'` (Linux/macOS) or `$env:DATABASE_PASSWORD='my_secure_password'` (Windows PowerShell).
3. Run the script: `python main.py`

## Original Article

This example accompanies the Turkish article: [AWS Kimlik Bilgisi Yönetimi: Hardcoding'e Son Verin](https://fatihsoysal.com/blog/aws-kimlik-bilgisi-yonetimi-hardcodinge-son-verin/).

## License

MIT — see [LICENSE](LICENSE).
