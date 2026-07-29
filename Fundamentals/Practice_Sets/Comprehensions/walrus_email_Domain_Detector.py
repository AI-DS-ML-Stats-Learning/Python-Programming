raw_emails = ['  salil@gmail.com  ', 'invalid_email', ' AMIT@YAHOO.COM ', '  ']

# We want to:

# Clean the email (remove outer whitespace and convert to lowercase).
# Validate it (only keep it if it contains @).
# Extract and return the domain name (the part after the @).
# Your Task: Write a single list comprehension using the Walrus Operator (:=) that cleans the email, 
# validates it, and extracts the domain.

# Example Output: ['gmail.com', 'yahoo.com']

cleaned_domain = [ y.split('@')[1] for x in raw_emails if '@' in (y:=x.lower().strip())]

print(cleaned_domain)