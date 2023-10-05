# Generated by Django 4.2.6 on 2023-10-05 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_picture', models.ImageField(upload_to='donations/pictures')),
                ('back_picture', models.ImageField(upload_to='donations/pictures')),
                ('wear_tear', models.BooleanField(default=False)),
                ('stain_odor_damage', models.BooleanField(default=False)),
                ('use', models.CharField(choices=[('new', 'New'), ('lightly used', 'Lightly Used'), ('old', 'Old')], max_length=50)),
                ('ai_score', models.JSONField()),
                ('approval', models.BooleanField(default=False)),
                ('donater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.donateruser')),
            ],
        ),
    ]