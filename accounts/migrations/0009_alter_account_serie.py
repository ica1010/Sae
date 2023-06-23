# Generated by Django 4.1.7 on 2023-04-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_account_serie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='serie',
            field=models.CharField(choices=[('C4', 'C4'), ('G1', 'G1'), ('E', 'E'), ('G2', 'G2'), ('D', 'D'), ('A4', 'A4'), ('F4', 'F4'), ('G3', 'G3'), ('F2', 'F2')], default='D', max_length=10),
        ),
    ]