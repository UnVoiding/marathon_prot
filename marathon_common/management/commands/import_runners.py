from django.core.management.base import BaseCommand, CommandError
from marathon_utils.runners_utils import import_runners


class Command(BaseCommand):
    help = 'imports runners from a CSV file'

    # def add_arguments(self, parser):
    #     parser.add_argument('csv', nargs='+', type=int)

    def handle(self, *args, **options):
        pass
        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
