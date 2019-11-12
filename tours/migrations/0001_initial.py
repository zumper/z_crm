# Generated by Django 2.2.4 on 2019-11-12 05:29

import common.enums
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('opportunity', '0004_opportunity_teams'),
        ('buildings', '0001_initial'),
        ('events', '0004_event_opportunities'),
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('end', models.DateTimeField()),
                ('start', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 'SCHEDULED'), (1, 'COMPLETED'), (2, 'CANCELLED'), (3, 'RESCHEDULED'), (4, 'DELAYED')], default=common.enums.AppointmentStatus(0))),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours', to='buildings.Building')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_tours', to='events.Event')),
                ('listing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours', to='listings.Listing')),
                ('opportunities', models.ManyToManyField(related_name='tours', to='opportunity.Opportunity')),
            ],
        ),
    ]
