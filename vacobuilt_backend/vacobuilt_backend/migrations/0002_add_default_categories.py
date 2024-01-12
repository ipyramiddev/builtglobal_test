from django.db import migrations

def create_default_categories(apps, schema_editor):
    Category = apps.get_model('vacobuilt_backend', 'Category')
    Category.objects.create(name='General')
    Category.objects.create(name='Technology')
    Category.objects.create(name='Random')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vacobuilt_backend', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]