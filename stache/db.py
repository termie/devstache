"""The various calls to fetch data from the db."""

from stache import Models


def get_results(version=None, run=None):
  """Get stored results from a set of test runs.

  Params:
    version - a version identifier, corresponds to a variety of config options
    run - uuid of which run this result is associated with

  """

