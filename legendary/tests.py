from django.test import TestCase
from legendary.models import Company

# Create your tests here.
class CompanyTests(TestCase):
    # Ensures when company default that defualt fields are set
    def test_company_default_address(self):
        company = Company(name = "Company")

        self.assertEqual(company.address, "None")
    
    def test_company_default_email(self):
        company = Company()

        self.assertEqual(company.email, "no.email@provided")

    def test_company_default_website(self):
        company = Company()

        self.assertEqual(company.website, "https://en.wikipedia.org/w/index.php?search=&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1")

    def test_larger_than_field_length(self):
        # Can be greater than limit?
        company = Company(name = "test")
        company.email = "1" * Company.MAX_EMAIL_LENGTH

        self.assertEqual(company.email, "1" * Company.MAX_EMAIL_LENGTH)

    def test_self_str(self):
        company = Company(name = "testing")

        self.assertEqual(company.name, "testing")