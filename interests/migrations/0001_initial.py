# Generated by Django 2.2.4 on 2019-11-12 05:29

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0004_contact_teams'),
        ('leads', '0010_lead_teams'),
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('tracking_id', models.CharField(max_length=256, null=True, unique=True, verbose_name='Tracking Id')),
                ('agent_email', models.CharField(blank=True, max_length=256, null=True, verbose_name='Agent Email')),
                ('brokerage_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Brokerage Name')),
                ('brokerage_key', models.CharField(blank=True, max_length=256, null=True, verbose_name='Brokerage Key')),
                ('min_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('max_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('availability_start', models.DateTimeField(blank=True, null=True)),
                ('availability_end', models.DateTimeField(blank=True, null=True)),
                ('budget', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('clazz', models.CharField(blank=True, max_length=256, null=True, verbose_name='Clazz')),
                ('email', models.EmailField(blank=True, max_length=256, null=True)),
                ('features', models.BigIntegerField(blank=True, choices=[(1, 'APPLICATION_FEE'), (2, 'ASSISTED_LIVING'), (3, 'SPECIALS'), (4, 'INCOME_RESTRICTED'), (5, 'SECTION_8'), (6, 'SENIOR_LIVING'), (7, 'SHORT_TERM'), (8, 'STUDENT_HOUSING'), (9, 'VIP'), (10, 'SWEET_DEAL'), (11, 'SELECT'), (12, 'SELECT_MONETIZED'), (13, 'PAID_PROMOTION'), (14, 'META_NO_INDEX'), (15, 'REX'), (16, 'EXCLUSIVE'), (17, 'MM_EXCLUDE'), (18, 'MM_PREVENT'), (19, 'DIRECT_DEAL'), (20, 'HAS_UNITS'), (21, 'BOOK_NOW'), (22, 'THIRD_PARTY_PAID'), (23, 'LARGE_LIST_CARD'), (24, 'REQ_PHONE_NUMBER'), (25, 'REQ_MOVE_IN_DATE'), (26, 'REQ_CUSTOM_MSG'), (27, 'FACEBOOK_EXCLUDE'), (28, 'LEASELOCK'), (29, 'FEATURED'), (30, 'TOUR')])),
                ('move_in_date', models.DateField(blank=True, null=True)),
                ('origin', models.TextField(blank=True, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interests', to='buildings.Building')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interests', to='contacts.Contact')),
                ('lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interests', to='leads.Lead')),
            ],
        ),
    ]
