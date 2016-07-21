from __future__ import unicode_literals

from django.db import models

'''
ok - models -- we want to be able to enter people, their titles, and their roles within groups
'''


class Person(models.Model):
    name = models.CharField(max_length=50, default='No Name Provided')
    title = models.CharField(max_length=50, default='No Title Provided')
    
    
class Group(models.Model):
    name = models.CharField(max_length=128, default='No Name Provided')
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    invite_reason = models.CharField(max_length=64)    
    



