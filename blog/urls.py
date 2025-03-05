from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
		path('', PostList.as_view(), name='home'),
        path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about'),
        path('contact/', TemplateView.as_view(template_name='blog/contact.html', 
											extra_context={'work':"Разработка программного обеспечения"})
											,name='contact'),
        path('bootstrap/', index, name='bootstrap'),
        path('<str:slug>/', PostDetailView.as_view(), name='post'),
        
        ]
