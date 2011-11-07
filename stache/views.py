import logging

from django import http
from django import template
from django.conf import settings
from django.template import loader

from stache import db

def results(request, version=None, run=None):
  """Show the table with the results of the tests."""
  results = db.get_results(version=version, run=run)

  c = template.RequestContext(request, locals)
  t = loader.get_template('results.html')
  return http.HttpResponse(t.render(c))
