from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


class CustomEmailValidator:

    def __init__(self, allowed_domains=None):
        self.allowed_domains = allowed_domains or []

    def __call__(self, value):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, value):
            raise ValidationError(
                _("Invalid email address format."),
                params={"value": value},
            )

        domain = value.split('@')[-1]
        if self.allowed_domains and domain not in self.allowed_domains:
            raise ValidationError(
                _("Email domain '%(domain)s' is not allowed. Allowed domains are: %(allowed)s."),
                params={"domain": domain, "allowed": ", ".join(self.allowed_domains)},
            )