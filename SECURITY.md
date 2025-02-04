# Security Policy

This document outlines the security practices for the **AI-Powered Voice Assistant** project, covering how to handle vulnerabilities, report security issues, and follow best practices to secure both the frontend and backend of the application.

## Supported Versions

This project supports the following versions:

- **Backend**: Flask API (Version 1.x.x)
- **Frontend**: Tkinter GUI (Python 3.x)

## Security Vulnerabilities

If you discover a security vulnerability in this project, please follow the steps below to report it responsibly.

### Reporting a Vulnerability

1. **Do Not Open Public Issues**: Please do not open a public issue or pull request to report vulnerabilities.
2. **Report Privately**: Send an email to the project maintainer at quan.duong4work@gmail.com with details of the vulnerability, including:
   - A description of the vulnerability.
   - Steps to reproduce the issue.
   - Affected version(s).
   - Potential impact of the vulnerability.
3. **Proof of Concept**: If possible, include a proof of concept to help the maintainers understand the issue more clearly.

Once the report is received, the maintainers will assess the vulnerability and respond accordingly. Critical vulnerabilities will be addressed as quickly as possible.

### Vulnerability Response Process

1. **Triage**: Once a vulnerability report is received, it will be triaged and prioritized based on severity.
2. **Patch**: A fix will be developed, tested, and deployed.
3. **Disclose**: Once the fix is available, the vulnerability will be disclosed responsibly, following best practices. The reporter will be credited for the find.

## Security Best Practices

### Backend (Flask API)

1. **Environment Variables for Secrets**:
   - Ensure that sensitive data such as API keys, authentication tokens, or passwords are not hardcoded in the code. Store them in environment variables or a `.env` file.

2. **Cross-Site Request Forgery (CSRF)**:
   - Enable CSRF protection for any forms or endpoints handling sensitive actions. Use Flask's built-in mechanisms or extensions like `Flask-WTF` for CSRF protection.

3. **Rate Limiting**:
   - To avoid abuse and denial-of-service (DoS) attacks, implement rate limiting on API endpoints using Flask extensions like `Flask-Limiter`.

4. **OpenAI API Key**:
   - Never expose the OpenAI API key in the frontend or public repositories. Always manage it securely in the backend.

5. **HTTPS**:
   - Ensure the Flask application is running over HTTPS in production environments. Consider using Let's Encrypt for a free SSL certificate.

6. **Input Validation and Sanitization**:
   - Validate and sanitize input from external sources (e.g., voice command input) to avoid injection attacks or data corruption.

7. **Error Handling**:
   - Do not expose detailed error messages to the client. Ensure that error handling is robust and logs are secure.

### Frontend (Tkinter GUI)

1. **Secure API Communication**:
   - Ensure that communication between the frontend GUI and the backend API is encrypted by using HTTPS. Never send sensitive data (e.g., OpenAI API key) from the frontend.

2. **Input Validation**:
   - Validate all user input on the frontend to avoid sending malicious commands or invalid data to the backend API.

3. **No Sensitive Data in Frontend**:
   - Ensure that no sensitive data, including API keys or authentication credentials, are stored or exposed in the frontend code.

### General Security

1. **Regular Updates**:
   - Regularly update all dependencies (e.g., Flask, Tkinter, speech recognition libraries) to their latest stable versions to ensure vulnerabilities are patched.

2. **Logging and Monitoring**:
   - Implement proper logging for security events, such as failed API requests or suspicious activity. Regularly monitor these logs to detect anomalies.

3. **Backup and Recovery**:
   - Ensure a robust backup system is in place, particularly for AI-generated responses and any user data. Regularly back up the application and have recovery processes defined.

4. **User Privacy**:
   - For any user-related data, ensure that proper privacy policies are in place and that users' personal data is not stored unnecessarily. Follow the relevant data protection regulations (e.g., GDPR).

## Acknowledgements

We want to thank the contributors and security researchers who help identify vulnerabilities and improve the overall security of this project.
