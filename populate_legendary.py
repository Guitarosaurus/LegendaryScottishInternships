import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'legendary_project.settings')

import datetime

import django
django.setup()

from legendary.models import Internship, Comment, Company

def populate():
    
    internships = [
        {
            'name': 'A Legendary Scottish Internship',
            'description':'...',
            'address': None,
            'closing_date': datetime.date(2025,5,15),
            'start_date': datetime.date(2125,6,15),
            'end_date': datetime.date(2999,7,17),
            'salary': 8740,
            'checklist': '''Item 1
            Item 2
            Item 3
            Item 4'''
        },
        {
            'name': 'Another Legendary Scottish Internship',
            'description':'....',
            'address':'Scotland',
            'closing_date': datetime.date(2026,5,15),
            'start_date': datetime.date(2125,6,15),
            'end_date': datetime.date(2999,7,17),
            'salary': 8740,
            'checklist': '''No Items'''
        }
    ]
    companies = {
        'A Scottish Company': {
            'internships': internships, 
            'name': 'A Scottish Company', 
            'address': 'Scotland',
            'email': 'noreply@scotland',
            'website': None
        } 
    }
    # If you want to add more categories or pages,
    # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for company, company_data in companies.items():
        c = add_company(company_data['name'], company_data['address'], company_data['email'], company_data['website'])
        for i in company_data['internships']:
            add_internship(c, i['name'], i['description'], i['address'], i['closing_date'], i['start_date'], i['end_date'], i['salary'], i['checklist'])
    # Print out the categories we have added.
        for c in Company.objects.all():
            for i in Internship.objects.filter(company_id=c):
                print(f'- {c}: {i}')

def add_internship(company, name, description, address, closing_date, start_date, end_date, salary, checklist):
    i = Internship.objects.get_or_create(company_id=company, name=name, description=description, closing_date=closing_date, start_date=start_date, end_date=end_date, salary=salary, checklist=checklist)[0]
    if address is not None:
        i.address=address
    i.save()
    return i

def add_company(name, address, email, website):
    c = Company.objects.get_or_create(name=name)[0]
    if address is not None:
        c.address=address
    if email is not None:
        c.email=email
    if website is not None:
        c.website=website
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Legendary population script...')
    populate()
