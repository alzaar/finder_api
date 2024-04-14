from django.test import TestCase

from ..views import FinderView


class TestFinderView(TestCase):
    def test_get_yelp_url(self):
        finder_view = FinderView()
        location = "San Francisco"
        search_term = "pizza"
        expected = (
            f"https://api.yelp.com/v3/businesses/search?location={location}"
            f"&term={search_term}&sort_by=best_match&limit=10"
        )
        assert finder_view.get_yelp_url(location, search_term) == expected
