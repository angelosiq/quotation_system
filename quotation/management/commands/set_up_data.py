from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext_lazy as _

from quotation.utils.integrations import get_data


class Command(BaseCommand):
    help = 'Set up data'

    def handle(self, *args, **kwargs):
        try:
            print('Setting up data')
            get_data()
            print('done')
        except:
            raise CommandError('An error occurred.')
