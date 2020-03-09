from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from core.models import WebsiteSetting, QuestionAnswer


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, *args, **kwargs):
        ctx = {}
        return ctx

class CerimeView(TemplateView):
    template_name = 'website_setting/cerime.html'

    def get_context_data(self, *args, **kwargs):
        ctx = {}
        ctx['show'] = WebsiteSetting.objects.first()
        return ctx

class ElaqeView(TemplateView):
    template_name = 'website_setting/elaqe.html'

    def get_context_data(self, *args, **kwargs):
        ctx = {}
        ctx['show'] = WebsiteSetting.objects.first()
        return ctx

class RusumView(TemplateView):
    template_name = 'website_setting/rusum_vergi.html'

    def get_context_data(self, *args, **kwargs):
        ctx = {}
        ctx['show'] = WebsiteSetting.objects.first()
        return ctx

class MeqsedlerView(TemplateView):
    template_name = 'website_setting/saytin_meqsedi.html'

    def get_context_data(self, *args, **kwargs):
        ctx = {}
        ctx['show'] = WebsiteSetting.objects.first()
        return ctx

class SuselerView(TemplateView):
    template_name = 'website_setting/suselerinin_tundlesdirilmesi.html'

    def get_context_data(self, *args, **kwargs):
        ctx = {}
        ctx['show'] = WebsiteSetting.objects.first()
        return ctx

class TexnikiView(TemplateView):
    template_name = 'website_setting/texniki_baxis.html'

    def get_context_data(self, *args, **kwargs):
        ctx = {}
        ctx['show'] = WebsiteSetting.objects.first()
        return ctx


class QuestionAnswerView(ListView):
    model = QuestionAnswer
    template_name = 'question_answer/question_answer.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['show'] = QuestionAnswer.objects.all()
        return ctx