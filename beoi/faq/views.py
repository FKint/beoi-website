from django.views.generic.base import TemplateView
from beoi.faq.models import *
from django.utils import translation

class FaqView(TemplateView):

	def get_context_data(self, **kwargs):

		from django.utils import translation
		cur_language = translation.get_language()
		text = translation.ugettext("News")
		print "%s %s %s" %( cur_language, text, translation.ugettext('welcome'))

		if translation.get_language() == "fr": quest_lang = LANG_FR
		else: quest_lang = LANG_NL
		
		def compare_cat(a,b):
			return cmp(a.order, b.order)

		questions = Question.objects.select_related("category").filter(lang=quest_lang)
		categories = sorted(list(set(map(lambda q:q.category, questions))),  compare_cat)

		for cat in categories:
			cat.questions = filter(lambda q: q.category == cat, questions)

		context = super(FaqView, self).get_context_data(**kwargs)
		context['categories'] = categories
		return context
