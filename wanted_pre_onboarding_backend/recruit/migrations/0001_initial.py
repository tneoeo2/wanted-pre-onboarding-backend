# Generated by Django 3.2.18 on 2023-10-18 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit.company')),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('reward', models.PositiveIntegerField()),
                ('detail', models.TextField()),
                ('skill', models.CharField(max_length=255)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit.jobinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruit.recruit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
