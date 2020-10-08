# Generated by Django 3.1.2 on 2020-10-07 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_mgr_rel', '0003_auto_20201007_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp_mgr_rel.employee'),
        ),
    ]