from django.test import TestCase
from legendary.models import Company, Internship, UserProfile
from django.template.defaultfilters import slugify
import datetime
from populate_legendary import populate

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

        self.assertEqual(str(company), "testing")

class InternshipTests(TestCase):
    def test_default_description(self):
        internship = Internship()

        self.assertEqual(internship.description, "This is an internship...")

    def test_default_closing_date(self):
        internship = Internship()

        self.assertEqual(internship.closing_date, None)

    def test_default_start_date(self):
        internship = Internship()

        self.assertEqual(internship.start_date, None)

    def test_default_end_date(self):
        internship = Internship()

        self.assertEqual(internship.end_date, None)

    def test_default_salary(self):
        internship = Internship()

        self.assertEqual(internship.salary, None)

    def test_default_address(self):
        internship = Internship()

        self.assertEqual(internship.address, "None")

    def test_default_checklist(self):
        internship = Internship()

        self.assertEqual(internship.checklist, "No extra items")

    def test_slug(self):
        internship = Internship(name = "testing slug")
        internship.slug = slugify(internship.name)
    
        self.assertEqual(internship.slug, "testing-slug")

    def test_save_without_all_params(self):
        # If certain fields are not filled should raise an error
        internship = Internship()
        error_to_save = False

        try:
            internship.save()
        except:
            error_to_save = True
        
        self.assertTrue(error_to_save)

    def test_self_str(self):
        internship = Internship()
        internship.name = "Test"

        self.assertEqual(str(internship), "Test")

class ProfileTests(TestCase):
    def test_picture_creation(self):
        userProfile = UserProfile()
        userProfile.picture = "index.jpg"

        self.assertEqual(userProfile.picture, "index.jpg")

class DatabaseTests(TestCase):
    populate()

    def test_no_of_categories(self):
        companies = Company.objects.filter()

        self.assertEqual(len(companies), 1, f"Expected only one company")
    
    def test_no_of_internships(self):
        internships = Internship.objects.filter()

        self.assertEqual(len(internships), 2, f"Expected 2 internships")

## Add tests to test admin functionality