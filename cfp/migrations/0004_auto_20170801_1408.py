# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def generate_participant_conversation(apps, schema_editor):
    MessageThread = apps.get_model("mailing", "MessageThread")
    Participant = apps.get_model("cfp", "Participant")
    db_alias = schema_editor.connection.alias
    for participant in Participant.objects.using(db_alias).filter(conversation=None):
        participant.conversation = MessageThread.objects.create()
        participant.save()


def generate_talk_conversation(apps, schema_editor):
    MessageThread = apps.get_model("mailing", "MessageThread")
    Talk = apps.get_model("cfp", "Talk")
    db_alias = schema_editor.connection.alias
    for talk in Talk.objects.using(db_alias).filter(conversation=None):
        talk.conversation = MessageThread.objects.create()
        talk.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
        ('cfp', '0003_auto_20170801_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='conversation',
            field=models.OneToOneField(null=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='mailing.MessageThread'),
            preserve_default=False,
        ),
        migrations.RunPython(generate_participant_conversation),
        migrations.AlterField(
            model_name='participant',
            name='conversation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mailing.MessageThread'),
        ),
        migrations.AddField(
            model_name='talk',
            name='conversation',
            field=models.OneToOneField(null=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='mailing.MessageThread'),
            preserve_default=False,
        ),
        migrations.RunPython(generate_talk_conversation),
        migrations.AlterField(
            model_name='talk',
            name='conversation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mailing.MessageThread'),
        ),
    ]
