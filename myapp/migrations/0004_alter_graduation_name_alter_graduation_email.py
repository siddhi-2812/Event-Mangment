# Generated by Django 5.0 on 2024-01-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_graduation_alter_user_email_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduation',
            name='Name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='email',
            field=models.EmailField(max_length=10),
        ),
    ]
