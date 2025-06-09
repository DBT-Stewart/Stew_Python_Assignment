import re

def is_valid_email(s):
    
    pattern = re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s)
    return bool(pattern)

def filter_emails(emails):
    
    return list(filter(is_valid_email, emails))
