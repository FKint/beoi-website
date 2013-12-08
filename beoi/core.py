
from django.utils import translation
from django.utils._os import safe_join
from django.template.loaders import filesystem

from django.conf import settings
from datetime import datetime

class TranslatedTemplateLoader(filesystem.Loader):
	def get_template_sources(self, template_name, template_dirs=None):
		template_dirs = map(lambda x: safe_join(x,translation.get_language()),settings.TEMPLATE_DIRS)
		return super(TranslatedTemplateLoader, self).get_template_sources(template_name, template_dirs=template_dirs)

def registration_open():
	return settings.REGISTRATION_DEADLINE > datetime.now()

def semifinal_started():
	return settings.SEMIFINAL_START > datetime.now()

def contest_year():
	if settings.REGISTRATION_DEADLINE.month < 6 : return settings.REGISTRATION_DEADLINE.year
	else: return settings.REGISTRATION_DEADLINE.year + 1

def contest_context(request):
	return {
		"REGISTRATION_OPEN": registration_open(),
		"REGISTRATION_DEADLINE": settings.REGISTRATION_DEADLINE
	}
