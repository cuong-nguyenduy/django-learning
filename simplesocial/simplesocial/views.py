from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'
    pass


class TestPageView(TemplateView):
    template_name = 'test.html'


class ThanksPageView(TemplateView):
    template_name = 'thanks.html'
