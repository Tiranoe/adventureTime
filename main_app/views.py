from django.shortcuts import render
from django.views import View 
# this handles viewing class to handle requests
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Post:
    def __init__(self, name, location, image, currency, description):
        self.name = name
        self.location = location
        self.image = image
        self.currency = currency
        self.description = description

posts = [
    Post("The Heart and Seoul", "Seoul, South Korea", "https://i.imgur.com/s3und9c.jpeg", "Won", "an extraordinary country filled with beautiful beaches, thriving cities, ancient temples, remarkable natural scenery and most importantly, friendly people."),
    Post("Land of many ports", "Portland, Maine", "https://i.imgur.com/gbnrNC4.jpeg", "Dollar", "Situated on Maine's southern coast along Casco Bay, Portland is recognized as the center of economy, tourism, and growth in the region. The city has a rich history in industry, fishing, agriculture, and Americana - and you probably don't know the half of it!"),
    Post("World's First class meat", "Kobe, Japan", "https://i.imgur.com/WKFSVm1.jpeg", "Yen", "The city is the place of origin of the world famous Kobe beef, and is home to Japan's most famous hot spring resort: Arima Onsen. Most breeds of Japanese Wagyu beef are associated with the area in which the cattle are raised – hence, Kobe beef is the breed of Wagyu from Kobe."),
    Post("Very COOL place to visit", "Swiss Alps, Switzerland", "https://i.imgur.com/z70URaK.jpeg", "Swiss Franc", "home to some of the most dramatic scenery in the world. From mountain tops that's height will crane your neck to so many beautiful, isolated lakes that you'll never want to leave. To give you a small taste of what to expect, the ski resort of Zermatt boasts 38 peaks over 4,000 metres alone."),
]

class PostList(TemplateView):
    template_name = "post_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = posts
        return context