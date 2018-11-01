# Generated by Django 2.1.2 on 2018-11-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostelAnnouncements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement_title', models.CharField(blank=True, max_length=30, null=True)),
                ('announcement', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImportantContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalAnnouncements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement_title', models.CharField(blank=True, max_length=30, null=True)),
                ('announcement', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessAnnouncements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement_title', models.CharField(blank=True, max_length=30, null=True)),
                ('announcement', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
    ]
