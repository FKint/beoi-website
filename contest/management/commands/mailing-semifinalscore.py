from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.loader import get_template
from django.core.mail import send_mail
from django.template import RequestContext, Context

from beoi.contest.models import ResultSemifinal, LANG_FR, LANG_NL
from beoi.core import contest_year

import time

class Command(BaseCommand):
    args = '[--send]'
    help = 'Give the API token for the given user'

    def handle(self, *args, **options):
	
		if len(args) > 1 : 
			raise CommandError('Invalid number of arguments')
		elif len(args) == 1 and args[0] != "--send":
			raise CommandError('Invalid argument')
		
		fake = len(args) == 0 
		queryset = ResultSemifinal.objects.select_related("contestant").filter(contestant__contest_year=contest_year())
		
		for result in queryset:
			lang = result.contestant.language
			qualified = result.qualified
			
			title = _("beOI - Semifinal results")
			
			if lang == LANG_FR and qualified: tpl = "emails/fr/semifinal-result-qualified.txt"
			if lang == LANG_FR and not qualified: tpl = "emails/fr/semifinal-result-notqualified.txt"
			if lang == LANG_NL and qualified: tpl = "emails/nl/semifinal-result-qualified.txt"
			if lang == LANG_NL and not qualified: tpl = "emails/nl/semifinal-result-notqualified.txt"
			
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
