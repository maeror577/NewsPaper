from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from news.models import Category, Post


class Command(BaseCommand):
    help = 'Removes all news within selected categories'
    missing_args_message = 'Not enough arguments!'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument('argument', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Do you really want to delete all news '
                          'within selected categories? (y/n)')
        existing_categories = []
        not_existing_categories = []
        if input() in ('y', 'Y'):
            for argument in options['argument']:
                try:
                    category = Category.objects.get(name=argument)
                    existing_categories.append(argument)
                    Post.objects.filter(category=category).delete()
                    category.delete()
                except ObjectDoesNotExist:
                    not_existing_categories.append(argument)

            if existing_categories:
                self.stdout.write(
                    self.style.SUCCESS(f'All news within these categories were removed: {", ".join(existing_categories)}')
                )
            if not_existing_categories:
                self.stdout.write(
                    self.style.ERROR(f'These categories do not exist: {", ".join(not_existing_categories)}')
                )

            return
