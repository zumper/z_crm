# Generated by Django 2.2.4 on 2019-11-12 05:29

import common.enums
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0019_auto_20191112_1059'),
        ('accounts', '0010_account_teams'),
        ('teams', '0004_auto_20191112_1059'),
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('listed_on', models.DateTimeField(blank=True, null=True)),
                ('zumper_id', models.BigIntegerField(db_index=True, null=True, unique=True)),
                ('zumper_agent_id', models.BigIntegerField(null=True)),
                ('zumper_brokerage_id', models.BigIntegerField(null=True)),
                ('agent_email', models.CharField(blank=True, max_length=256, null=True, verbose_name='Agent Email')),
                ('bathrooms', models.IntegerField(blank=True, null=True)),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('brokerage_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Brokerage Name')),
                ('brokerage_key', models.CharField(blank=True, max_length=256, null=True, verbose_name='Brokerage Key')),
                ('capped', models.BooleanField(default=False)),
                ('contact_email', models.EmailField(blank=True, max_length=256, null=True)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email_override', models.CharField(blank=True, max_length=256, null=True, verbose_name='Email Override')),
                ('features', models.BigIntegerField(blank=True, choices=[(1, 'APPLICATION_FEE'), (2, 'ASSISTED_LIVING'), (3, 'SPECIALS'), (4, 'INCOME_RESTRICTED'), (5, 'SECTION_8'), (6, 'SENIOR_LIVING'), (7, 'SHORT_TERM'), (8, 'STUDENT_HOUSING'), (9, 'VIP'), (10, 'SWEET_DEAL'), (11, 'SELECT'), (12, 'SELECT_MONETIZED'), (13, 'PAID_PROMOTION'), (14, 'META_NO_INDEX'), (15, 'REX'), (16, 'EXCLUSIVE'), (17, 'MM_EXCLUDE'), (18, 'MM_PREVENT'), (19, 'DIRECT_DEAL'), (20, 'HAS_UNITS'), (21, 'BOOK_NOW'), (22, 'THIRD_PARTY_PAID'), (23, 'LARGE_LIST_CARD'), (24, 'REQ_PHONE_NUMBER'), (25, 'REQ_MOVE_IN_DATE'), (26, 'REQ_CUSTOM_MSG'), (27, 'FACEBOOK_EXCLUDE'), (28, 'LEASELOCK'), (29, 'FEATURED'), (30, 'TOUR')])),
                ('feed_name', models.CharField(blank=True, max_length=128, null=True)),
                ('internal_features', models.BigIntegerField(blank=True, choices=[(1, 'SHOWING_SPECIALIST')])),
                ('listing_status', models.IntegerField(choices=[(0, 'UNKNOWN'), (1, 'ACTIVE'), (2, 'DRAFT'), (3, 'ARCHIVED'), (4, 'LEASED'), (5, 'DELETED'), (6, 'WITHDRAWN'), (7, 'FETCHING_MEDIA'), (8, 'MODERATION'), (9, 'PENDING'), (10, 'DUPLICATE'), (11, 'BANNED'), (12, 'SPAM'), (13, 'HONEYPOT'), (14, 'FOR_SALE'), (15, 'PRIVATE')], default=common.enums.PropertyStatus(0))),
                ('listing_title', models.CharField(max_length=128, verbose_name='Listing Title')),
                ('min_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('max_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('syndications', models.BigIntegerField(blank=True, choices=[(1, 'TRULIA')])),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='accounts.Account')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='listings', to='common.Address')),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='buildings.Building')),
                ('teams', models.ManyToManyField(related_name='listings', to='teams.Teams')),
            ],
        ),
    ]
