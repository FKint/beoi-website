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
		queryset = ResultSemifinal.objects.select_related("contestant").filter(contestant__contest_year=contest_year())
		
		for result in queryset:
			lang = result.contestant.language
			qualified = result.qualified
			
			if lang == LANG_FR :
				activate("fr")
				if qualified: tpl = "emails/fr/semifinal-result-qualified.txt"
				else:  tpl = "emails/fr/semifinal-result-notqualified.txt"
			if lang == LANG_NL:
				activate("nl")
				if qualified: tpl = "emails/nl/semifinal-result-qualified.txt"
				else: tpl = "emails/nl/semifinal-result-notqualified.txt"
			
			title = _("beOI - Semifinal results")
			
			score = result.score
			position = 1 + ResultSemifinal.objects.filter(
				contestant__contest_year=contest_year(), 
				score__gt=score
				).count()

			mail_template = get_template(tpl)
			context = Context({
				"SCORE": score,
				"POSITION": position
			})
			
			if fake: email = dict(settings.ADMINS).values()[0]
			else: email = result.contestant.email
			
			send_mail(title, mail_template.render(context), "info@be-oi.be", [email], fail_silently=True)
			self.stdout.write( "Mail (template:%s) sent to %s\n" %  (tpl, result.contestant.email) )
			time.sleep(1)
