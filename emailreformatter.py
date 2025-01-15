import re

class EmailFormatter:
    def __init__(self):
        # Define a regex pattern for a valid email address
        self.email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    def validate_email(self, email: str) -> bool:
        """
        Validates the email format using a regex pattern.
        """
        return bool(self.email_pattern.match(email))

    def format_email(self, email: str) -> str:
        """
        Formats the email by stripping spaces and converting to lowercase.
        """
        return email.strip().lower()

    def process_email(self, email: str) -> str:
        """
        Validates and formats the email. Raises an exception if invalid.
        """
        email = self.format_email(email)
        if not self.validate_email(email):
            raise ValueError(f"Invalid email address: {email}")
        return email

# Example usage
if __name__ == "__main__":
    formatter = EmailFormatter()
    emails = [
        "   Example@DOMAIN.COM   ",
        "user.name+test@example.com",
        "invalid-email@.com"
    ]

    for email in emails:
        try:
            formatted_email = formatter.process_email(email)
            print(f"Valid formatted email: {formatted_email}")
        except ValueError as e:
            print(e)
