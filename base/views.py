from django.shortcuts import render

from django.views.generic import TemplateView
from wagtail.core.models import Site


class RobotsView(TemplateView):
    content_type = 'text/plain'
    template_name = 'robots.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = context['view'].request
        context['wagtail_site'] = Site.find_for_request(request)
        return context


def page_not_found(request, exception):
    return render(request, "404.html", {})


def error_view(request, exception=None):
    return render(request, "500.html", {})
