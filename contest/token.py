from datetime import datetime 
from django.utils.hashcompat import md5_constructor
from django.core.exceptions import ObjectDoesNotExist
from beoi.contest.models import *

def full_token(godfather_token, registration_time):
	return full_token_from_stat_token(stat_token(godfather_token, registration_time))

def full_token_from_stat_token(stat_token):
	return md5_constructor("%s" % stat_token).hexdigest()[0:8]

def stat_token(godfather_token, registration_time):
	return md5_constructor("%s%s" % (godfather_token, registration_time)).hexdigest()[0:12]

def is_valid_token(token):
	try:
		contestant = Contestant.objects.get(token=token)
		return True
	except ObjectDoesNotExist:
		return False
