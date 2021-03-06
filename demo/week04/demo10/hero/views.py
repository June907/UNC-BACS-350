from django.views.generic import TemplateView


class HeroView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        id = kwargs.get('identity', 'Hulk')
        return {'hero': id, 'css': '/static/hero.css'}

class BasePage(TemplateView):
    template_name = "page_theme.html"
    
class AboutPage(TemplateView):
    template_name = "about.html"
