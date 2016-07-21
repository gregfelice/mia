from django.test import TestCase

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Person
from .models import Group
from .models import Membership


class PersonMethodTests(TestCase):
    
    def test_can_create_and_save_person(self):
        name = "greg felice"
        title = "dude"
        p = Person(name=name, title=title)
        p.save()
        

    def test_can_retrieve_person(self):
        p = Person(name="greg felice")
        p.save()
        rp = Person.objects.filter(id=p.id).first()
        self.assertEqual(p.id, rp.id)

class GroupMethodTests(TestCase):
    
    # see https://docs.djangoproject.com/en/1.9/topics/db/models/
    def test_can_create_group_and_add_people(self):
        group_name = "testgroup"
        person_name = "greg felice"
        g = Group(name=group_name)
        p = Person(name=person_name)
        g.save()
        p.save()
        m1 = Membership(person=p, group=g, invite_reason="scrum master")
        m1.save()
        print g.members.all().first().name

    
