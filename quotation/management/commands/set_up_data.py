from django.core.management.base import BaseCommand, CommandError

from quotation.utils.integrations import get_data


class Command(BaseCommand):
    help = 'Set up data'

    def handle(self, *args, **kwargs):
        try:
            print('Setting up data')
            get_data()
            print('done')
        except:
            raise CommandError('Initalization failed.')
