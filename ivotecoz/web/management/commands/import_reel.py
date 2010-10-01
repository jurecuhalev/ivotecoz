from django.core.management.base import BaseCommand, CommandError
from ivotecoz.web.models import Reel

class Command(BaseCommand):
    args = 'list.txt <reel number>'
    help = 'Imports Reel (boben)'

    def handle(self, *args, **options):
        f = open(args[0])
        for line in f.readlines():
            reel = Reel(order=int(args[1]),
                        text=line.strip())
            reel.save()
