# Generated by Django 2.2.9 on 2020-02-05 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerinfo',
            name='IP_address',
        ),
        migrations.RemoveField(
            model_name='volunteerinfo',
            name='MAC_address',
        ),
        migrations.RemoveField(
            model_name='volunteerinfo',
            name='location',
        ),
        migrations.RemoveField(
            model_name='volunteerinfo',
            name='users_name',
        ),
        migrations.AlterField(
            model_name='volunteerinfo',
            name='volunteer_name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('complete', models.BooleanField()),
                ('volunteerinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteers.Volunteerinfo')),
            ],
        ),
    ]
