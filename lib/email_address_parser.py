import re
class  EmailAddressParser:
    email_regex =re.compile (r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9+._-]+\.[a-zA-Z0-9+._-]+)')
    def __init__(self,emails):
        self.emails=emails

    def parse(self):
        strings=re.split(r',|\s', self.emails)
        parsed_emails=set()
        for string in strings:
            if self.email_regex.fullmatch(string):
                parsed_emails.add(string)
        return sorted(list(parsed_emails))
    