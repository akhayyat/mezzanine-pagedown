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
        parser.add_argument('--scheme', dest='scheme_name', type=str, help="""Available color schemes:
""" + '\n'.join(["  %s" % name for name in get_all_styles()]))

        parser.add_argument('--all', dest='all_styles', action='store_true')

    def handle(self, *args, **options):
        if not PYGMENTS:
            raise CommandError('Unable to load pygments. '
                               'Please install pygments to use this command.')

        if options['all_styles']:
            for scheme in get_all_styles():
                print(HtmlFormatter(style=scheme).get_style_defs(
                    '.%s .codehilite' % scheme))
            # generated all styles, done and done
            sys.exit(0)


        if options['scheme_name']:
            scheme=options['scheme_name']
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
