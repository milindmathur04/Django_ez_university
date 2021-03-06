# Generated by Django 2.1.1 on 2018-10-27 20:02

from django.db import migrations

SEMESTERS = [
    {
        'semester_name': '2019 - Fall',
    },
{
        'semester_name': '2020 - Spring',
    },
{
        'semester_name': '2020 - Summer',
    },
{
        'semester_name': '2020 - Fall',
    },
{
        'semester_name': '2021 - Spring',
    },
]


def add_semester_data(apps, schema_editor):
    semester_model_class = apps.get_model('courseinfo', 'Semester')
    for semester in SEMESTERS:
        semester_object = semester_model_class.objects.create(
            semester_name=semester['semester_name'],
        )


def remove_semester_data(apps, schema_editor):
    semester_model_class = apps.get_model('courseinfo', 'Semester')
    for semester in SEMESTERS:
        semester_object = semester_model_class.objects.get(
            semester_name=semester['semester_name']
        )
        semester_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0003_auto_20181027_1455'),
    ]

    operations = [
        migrations.RunPython(
            add_semester_data,
            remove_semester_data
        )
    ]
