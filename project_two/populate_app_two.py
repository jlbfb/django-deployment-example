import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')

import django
django.setup()

## Fake population script
import random
from app_two.models import Headings, SubHeadings, Documents, Images, Relations, States, Texts
from faker import Faker

fakegen = Faker()
titles = [1, 2, 3]

def add_titles():
    t = Documents.objects.get_or_create(document_id = random.choice(titles))[0]  # the [0] is because the object returned is a tuple and we need the reference to the model instance
    print(t)
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        
        # get the topic for the entry
        # top = add_titles()
        
        # Create the fake data for that entry
        fake_heading = fakegen.sentence()
        fake_subheading = fakegen.company()
        fake_pos = entry + 4
        fake_state = fakegen.state()
        fake_url = fakegen.url()
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        

        # Create the new webpage entry
        # subheads = SubHeadings.objects.get_or_create(heading_id = top, subheading = fake_subheading, position = fake_pos)[0]
        
        # Create a fake images entry
        # image_entry = Images.objects.get_or_create(imageURL = fake_url, caption = fake_heading)[0]

        # Create fake headings
        heading_entry = Headings.objects.get_or_create(heading = fake_heading, position = fake_pos)

if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete!')


