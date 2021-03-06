# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xmgr', '0002_group_grouprole_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_reason', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='GroupRole',
        ),
        migrations.RemoveField(
            model_name='group',
            name='title',
        ),
        migrations.RemoveField(
            model_name='person',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='person',
            name='lastname',
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='No Name Provided', max_length=128),
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='No Name Provided', max_length=50),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='membership',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmgr.Group'),
        ),
        migrations.AddField(
            model_name='membership',
            name='inviter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_invites', to='xmgr.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmgr.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='xmgr.Membership', to='xmgr.Person'),
        ),
    ]
