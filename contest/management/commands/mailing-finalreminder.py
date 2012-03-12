from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.translation import activate, ugettext_lazy as _
from django.template.loader import get_template
from django.core.mail import send_mail
from django.template import RequestContext, Context
from optparse import make_option

from beoi.contest.models import ResultSemifinal, LANG_FR, LANG_NL
from beoi.core import contest_year

import time

class Command(BaseCommand):
	help = 'Send the email (fake send unless --send is given)'
	option_list = BaseCommand.option_list + (
	make_option('--send', action='store_true', dest='send', default=False,
        help='Actually send the emails'),	)
	
	def handle(self, *args, **options):
		
		fake = (not options["send"])
		queryset = ResultSemifinal.objects.select_related("contestant").filter(contestant__contest_year=contest_year(),qualified=True)
		
		for result in queryset:
			lang = result.contestant.language
			
			if lang == LANG_FR :
				activate("fr")
				tpl = "emails/fr/final-reminder.txt"
			if lang == LANG_NL:
				activate("nl")
				tpl = "emails/nl/final-reminder.txt"
			
			title = "beOI - %s" % _("Finals")
			
			mail_template = get_template(tpl)
			context = Context({})
			
			if fake: email = dict(settings.ADMINS).values()[0]
			else: email = result.contestant.email
			
			send_mail(title, mail_template.render(context), "info@be-oi.be", [email], fail_silently=True)
			self.stdout.write( "Mail (template:%s) sent to %s\n" %  (tpl, result.contestant.email) )
			time.sleep(1)
