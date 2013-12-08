from beoi.news.models import News
from django.views.generic.list import ListView
from django.utils import translation

''' 
No directly in urls.py because request customization by language is needed 
'''
class NewsView(ListView):

	paginate_by = 5

	def get_queryset(self):
		if translation.get_language() == "fr": 
			lang = News.LANG_FR
		else :
			lang = News.LANG_NL

		return News.online_objects.filter(lang=lang).order_by("-publication_date")
