from django.core.management import BaseCommand
from worker.models import Object


class UtilsMethod:
    def choose(self):
        best_obj = Object.objects.filter(status='Остановлен').order_by('-priority', 'time_created').first()
        return best_obj.id


class Command(BaseCommand):
    help = 'Скрипт choose'

    # def add_arguments(self, parser):
    #     parser.add_argument('url_parse')

    def handle(self, *args, **options):
        # s['url'] = options['url_parse']
        p = UtilsMethod().choose()
        print(f'id объекта - {p}')
