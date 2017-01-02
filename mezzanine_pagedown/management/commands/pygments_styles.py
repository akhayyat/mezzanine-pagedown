import sys
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

try:
    from pygments.styles import get_all_styles
    from pygments.formatters import HtmlFormatter
except ImportError:
    PYGMENTS = False
else:
    PYGMENTS = True

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('scheme')
        parser.add_argument('--all', dest='all_styles', action='store_true')

    def handle(self, *args, **options):
        if not PYGMENTS:
            raise CommandError('Unable to load pygments. '
                               'Please install pygments to use this command.')

        print args
        print options

        if options['all_styles']:
            for scheme in get_all_styles():
                print(HtmlFormatter(style=scheme).get_style_defs(
                    '.%s .codehilite' % scheme))
            # generated all styles, done and done
            sys.exit(0)


        if len(args) == 0:
            print("""
Usage: ./manage.py pygments_styles <scheme_name>
Available color schemes:
""" + '\n'.join(["  %s" % name for name in get_all_styles()]))
        else:
            scheme=args[0]
            try:
                assert(scheme in list(get_all_styles()))
            except AssertionError:
                raise CommandError('Invalid scheme name "% s"\n' % scheme +
                                   'Please use one of the available color'
                                   ' schemes on your system:\n' +
                                   '\n'.join(["  %s" % name for name in \
                                              get_all_styles()]))
            print(HtmlFormatter(style=scheme).get_style_defs('.codehilite'))
            sys.exit(0)
