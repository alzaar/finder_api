import os
import requests
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from django.http import JsonResponse


class FinderView(RetrieveModelMixin, GenericAPIView):
    BASE_URL = "https://api.yelp.com/v3/businesses/search"

    def get_yelp_url(self, location, search_term):
        return (
            f"{self.BASE_URL}?location={location}&term={search_term}"
            "&sort_by=best_match&limit=10"
        )

    def get(self, request, *args, **kwargs):
        response = requests.get(
            self.get_yelp_url(
                request.GET.get("location"), request.GET.get("search_term")
            ),
            headers={"Authorization": f"Bearer {os.getenv('YELP_API_KEY')}"},
        ).json()

        return JsonResponse(response)
