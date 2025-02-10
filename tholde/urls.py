from django.urls import path
from tholde.views import *

urlpatterns = [
    path('', index, name='index'),
    path('www.linkedin.com/in/tholde-rftn', redirect_linkedin),
    path('https://github.com/Tholde', redirect_github),
    path('https://www.facebook.com/ambanimaso.technology', redirect_facebook),
    path('https://www.instagram.com/tholde.rftn', redirect_instagram),
    path('https://x.com/tholde_rftn', redirect_twitter),
]
