from django.conf.urls import url

urlpatterns = [
    url(r'^hello/', 'myapp.views.hello', name='hello'),
    url(r'^empty_literature_search', 'myapp.views.render_graph', name='render_graph'),
]
