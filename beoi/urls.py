
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin

from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView

from beoi.core import contest_year
from beoi.contest.models import *
from beoi.news.feed import RssNews
from beoi.news.views import NewsView
from beoi.faq.views import FaqView

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='root.html'), name="root"),
    url(r'^admin/', include(admin.site.urls)),
  	(r'^robots\.txt', TemplateView.as_view(template_name='robots.txt')),	
)

urlpatterns += i18n_patterns('',

	url(r'^$', NewsView.as_view(template_name='home.html'), name='home'),
	url(r'^rss$', RssNews(), {}, name="rss"),

	#url(r'^agenda$', direct_to_template, {'template': 'calendar.html'}, "agenda"),
	url(r'^rules$', TemplateView.as_view(template_name='rules.html'), name="rules"),
	url(r'^sample-questions$', TemplateView.as_view(template_name='sample_questions.html'), name="sample-questions"),
	url(r'^faq$', FaqView.as_view(template_name='faq.html'), name="faq"),
	url(r'^about$', TemplateView.as_view(template_name='about.html'), name="about"),

	url(r'^contest$', TemplateView.as_view(template_name='contest.html'), name="contest"),
	url(r'^registration$', "beoi.contest.views.registration",  {'template': 'registration.html'}, name="registration"),
	# #fixit for registration:
	# # url(r'^registration/error$', TemplateView.as_view(template_name='registration_confirm.html', "extra_context":{"error":1}}, "registration-error"),
	url(r'^registration/confirm/(?P<object_id>\d+)$', ListView.as_view(
		template_name='registration_confirm.html',
		queryset=SemifinalCenter.objects.filter(active=True)
		), name="registration-confirm"),

	url(r'^sponsors$', TemplateView.as_view(template_name='sponsors.html'), name="sponsors"),
	url(r'^membership$', TemplateView.as_view(template_name='membership.html'), name="membership"),
	url(r'^press$', TemplateView.as_view(template_name='press.html'), name="press"),
	
	url(r'^semifinal/places$', ListView.as_view(template_name='semifinal_places.html',
		queryset=SemifinalCenter.objects.filter(active=True)), name="semifinal-places"),

	url(r'^final/results$', ListView.as_view(template_name='final_results.html',
		queryset=ResultFinal.objects.select_related('contestant', 'contestant__school')
		.extra(select={"total":"score_written+score_computer"})
		.filter(contestant__contest_year=contest_year())
		.order_by("rank")), name="final-results"),

	url(r'^semifinal/results$', ListView.as_view(template_name='semifinal_results.html',
		queryset=ResultSemifinal.objects.select_related('contestant', 'contestant__school')
		.filter(qualified=True,contestant__contest_year=contest_year())
		.order_by("contestant__surname","contestant__firstname")), name="semifinal-results"),

	url(r'^training$', TemplateView.as_view(template_name='training.html'), name="training"),
	url(r'^preparing$', TemplateView.as_view(template_name='preparing.html'), name="preparing"),
	url(r'^learn-programming$', TemplateView.as_view(template_name='learn_programming.html'), name="learn-programming"),
	
	url(r'^archives/1992$', TemplateView.as_view(template_name='1992.html'), name="archives-1992"),		
	url(r'^archives/2010$', TemplateView.as_view(template_name='2010.html'), name="archives-2010"),
	url(r'^archives/2011$', TemplateView.as_view(template_name='2011.html'), name="archives-2011"),
	url(r'^archives/2012$', TemplateView.as_view(template_name='2012.html'), name="archives-2012"),
	url(r'^archives/2013$', TemplateView.as_view(template_name='2013.html'), name="archives-2013"),
	
	# unlinked pages
	# url(r'^registration/stats$', "beoi.contest.views.stats", {'template': '../common/stats.html'}, name="stats"),
)
