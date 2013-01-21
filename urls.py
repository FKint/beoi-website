# -*- coding: utf-8 -*-
from django.contrib import admin
admin.autodiscover()
from os import path
from django.conf.urls.defaults import patterns, include, url

from beoi.core import contest_year
from beoi.contest.models import *
from beoi.news.feed import RssNews
from beoi.news.views import news

from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template, redirect_to

# Those urls are resolved with the lang prefix. This prefix is prepend before template file value.
multilang_patterns = patterns('',

	url(r'^(?P<page>[0-9]+)?$', news, {'template': "home.html"}, 'home'),
	url(r'^rss$', RssNews(), {}, "rss"),

	#url(r'^agenda$', direct_to_template, {'template': 'calendar.html'}, "agenda"),
	url(r'^rules$', direct_to_template, {'template': 'rules.html'}, "rules"),
	url(r'^sample-questions$', direct_to_template, {'template': 'sample_questions.html'}, "sample-questions"),
	url(r'^faq$', "beoi.faq.views.faq",  {'template': 'faq.html'}, "faq"),
	url(r'^referrals$', "beoi.contest.views.referrals",  {'template': 'referrals.html'}, "referrals"),
	url(r'^about$', direct_to_template,  {'template': 'about.html'}, "about"),

	url(r'^contest$', direct_to_template,  {'template': 'contest.html'}, "contest"),
	url(r'^registration$', "beoi.contest.views.registration",  {'template': 'registration.html'}, "registration"),
	url(r'^registration/error$', direct_to_template, {'template': 'registration_confirm.html', "extra_context":{"error":1}}, "registration-error"),
	url(r'^registration/confirm/(?P<object_id>\d+)$', list_detail.object_detail, {	'template_name': 'registration_confirm.html', 
		"queryset": SemifinalCenter.objects.filter(active=True) }, "registration-confirm"),

	url(r'^sponsors$', direct_to_template, {'template': 'sponsors.html'}, "sponsors"),
	url(r'^press$', direct_to_template, {'template': 'press.html'}, "press"),
	
	url(r'^semifinal/places$', list_detail.object_list, {'template_name': 'semifinal_places.html',
		"queryset": SemifinalCenter.objects.filter(active=True)},"semifinal-places"),

	url(r'^training$', direct_to_template,  {'template': 'training.html'}, "training"),
	url(r'^preparing$', direct_to_template,  {'template': 'preparing.html'}, "preparing"),
			
	url(r'^archives/2010$', direct_to_template, {'template': '2010.html'}, "archives-2010"),
	url(r'^archives/2011$', direct_to_template, {'template': '2011.html'}, "archives-2011"),
	url(r'^archives/2012$', direct_to_template, {'template': '2012.html'}, "archives-2012"),
	
	# unlinked pages
	url(r'^registration/stats$', "beoi.contest.views.stats", {'template': '../common/stats.html'}, "stats"),
)

urlpatterns = patterns('',
	# admin panel
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),

	# Serving public files
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': path.join(path.dirname(__file__), 'static').replace('\\','/')}),

	# main
	url(r'^$', direct_to_template, {'template': 'home.html'}, "home"),

	# meta
	(r'^(?P<language>(fr|nl))/', include(multilang_patterns)),
	
	# for transition/compatibity purpose with migration 2013/01
	(r'^fr/final', redirect_to, {'url': '/fr/contest'}),
	(r'^nl/final', redirect_to, {'url': '/nl/contest'}),
	(r'^fr/final/rules', redirect_to, {'url': '/fr/contest'}),
	(r'^nl/final/rules', redirect_to, {'url': '/nl/contest'}),
	(r'^fr/semifinal', redirect_to, {'url': '/fr/contest'}),
	(r'^nl/semifinal', redirect_to, {'url': '/nl/contest'}),
	(r'^fr/semifinal/rules', redirect_to, {'url': '/fr/contest'}),
	(r'^nl/semifinal/rules', redirect_to, {'url': '/nl/contest'}),
	(r'^fr/ioi', redirect_to, {'url': '/fr/contest'}),
	(r'^nl/ioi', redirect_to, {'url': '/nl/contest'}),
	(r'^fr/agenda', redirect_to, {'url': '/fr/contest'}),
	(r'^nl/agenda', redirect_to, {'url': '/nl/contest'}),
	(r'^fr/team', redirect_to, {'url': '/fr/about'}),
	(r'^nl/team', redirect_to, {'url': '/nl/about'}),
	(r'^fr/archives/2012/semifinal$', redirect_to, {'url': '/fr/archives/2012'}),
	(r'^nl/archives/2012/semifinal$', redirect_to, {'url': '/nl/archives/2012'}),
	(r'^fr/archives/2012/final', redirect_to, {'url': '/fr/archives/2012'}),
	(r'^nl/archives/2012/final', redirect_to, {'url': '/nl/archives/2012'}),
	(r'^fr/archives/2012/ioi', redirect_to, {'url': '/fr/archives/2012'}),
	(r'^nl/archives/2012/ioi', redirect_to, {'url': '/nl/archives/2012'}),
	(r'^fr/archives/2011/semifinal$', redirect_to, {'url': '/fr/archives/2011'}),
	(r'^nl/archives/2011/semifinal$', redirect_to, {'url': '/nl/archives/2011'}),
	(r'^fr/archives/2011/final', redirect_to, {'url': '/fr/archives/2011'}),
	(r'^nl/archives/2011/final', redirect_to, {'url': '/nl/archives/2011'}),
	(r'^fr/archives/2011/ioi', redirect_to, {'url': '/fr/archives/2011'}),
	(r'^nl/archives/2011/ioi', redirect_to, {'url': '/nl/archives/2011'}),
	(r'^fr/archives/2010/semifinal$', redirect_to, {'url': '/fr/archives/2010'}),
	(r'^nl/archives/2010/semifinal$', redirect_to, {'url': '/nl/archives/2010'}),
	(r'^fr/archives/2010/final', redirect_to, {'url': '/fr/archives/2010'}),
	(r'^nl/archives/2010/final', redirect_to, {'url': '/nl/archives/2010'}),
	(r'^fr/archives/2010/ioi', redirect_to, {'url': '/fr/archives/2010'}),
	(r'^nl/archives/2010/ioi', redirect_to, {'url': '/nl/archives/2010'}),
	
	# for transition/compatibity purpose for migration in 2011
	(r'^inscription', redirect_to, {'url': '/fr/registration'}),
	(r'^inschrijven', redirect_to, {'url': '/nl/registration'}),
	(r'^tenirajour$', redirect_to, {'url': '/fr'}),
	(r'^todo$', redirect_to, {'url': '/nl'}),
	(r'^calendrier$', redirect_to, {'url': '/fr/agenda'}),
	(r'^agenda$', redirect_to, {'url': '/nl/agenda'}),
	(r'^reglement$', redirect_to, {'url': '/fr/rules'}),
	(r'^reglement-nl$', redirect_to, {'url': '/nl/rules'}),
	(r'^demi-finales', redirect_to, {'url': '/fr/semifinal'}),
	(r'^halve-finale', redirect_to, {'url': '/nl/semifinal'}),
	(r'^olympiades-internationales$', redirect_to, {'url': '/fr/ioi'}),
	(r'^internationale-olympiade$', redirect_to, {'url': '/nl/ioi'}),
	(r'^finales-fr', redirect_to, {'url': '/fr/final'}),
	(r'^finales-nl', redirect_to, {'url': '/nl/final'}),
	(r'^formations$', redirect_to, {'url': '/fr/training'}),
	(r'^opleidingen$', redirect_to, {'url': '/nl/training'}),
	(r'^exemple-questions$', redirect_to, {'url': '/fr/sample-questions'}),
	(r'^voorbeeldvragen$', redirect_to, {'url': '/nl/sample-questions'}),
	(r'^archives', redirect_to, {'url': '/fr/archives'}),
	(r'^archieven', redirect_to, {'url': '/nl/archives'}),
	(r'^equipe$', redirect_to, {'url': '/fr/team'}),
	(r'^team$', redirect_to, {'url': '/nl/team'}),
	(r'^sponsors$', redirect_to, {'url': '/fr/sponsors'}),
	(r'^sponsors-nl$', redirect_to, {'url': '/nl/sponsors'}),
	(r'^presse$', redirect_to, {'url': '/fr/press'}),
	(r'^pers$', redirect_to, {'url': '/nl/press'}),
	(r'^centres-regionaux$', redirect_to, {'url': '/fr/semifinal/places'}),
	(r'^regionalecentra$', redirect_to, {'url': '/nl/semifinal/places'}),
	(r'^accueil', redirect_to, {'url': '/fr/'}),
	(r'^home$', redirect_to, {'url': '/nl/'}),
	(r'^rss-fr', redirect_to, {'url': '/fr/rss'}),
	(r'^rss-nl$', redirect_to, {'url': '/nl/rss'}),
)
