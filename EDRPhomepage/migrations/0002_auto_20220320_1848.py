# Generated by Django 3.0 on 2022-03-20 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EDRPhomepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='division',
            field=models.CharField(blank=True, default='9A4', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='subjectteacher',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(choices=[('TERMINALEXAM', 'TERMINALEXAM'), ('MONDAYTEST', 'MONDAYTEST'), ('ANNUALEXAM', 'ANNUALEXAM'), ('HOMEASSIGNMENT', 'HOMEASSIGNMENT'), ('LABWORK', 'LABWORK')], default='HOMEASSIGNMENT', max_length=30)),
                ('scorecard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
