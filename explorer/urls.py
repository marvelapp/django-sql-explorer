from django.conf.urls import url
from explorer import views

urlpatterns = [
    url(r'(?P<query_id>\d+)/$', views.QueryView.as_view(), name='query_detail'),
    url(r'(?P<query_id>\d+)/download$', views.download_query, name='query_download'),
    url(r'(?P<query_id>\d+)/csv', views.view_csv_query, name='query_csv'),
    url(r'(?P<pk>\d+)/delete$', views.DeleteQueryView.as_view(), name='query_delete'),
    url(r'new/$', views.CreateQueryView.as_view(), name='query_create'),
    url(r'play/$', views.PlayQueryView.as_view(), name='explorer_playground'),
    url(r'csv$', views.download_csv_from_sql, name='generate_csv'),
    url(r'schema/$', views.schema, name='explorer_schema'),
    url(r'logs/$', views.ListQueryLogView.as_view(), name='explorer_logs'),
    url(r'format/$', views.format_sql, name='format_sql'),
    url(r'^$', views.ListQueryView.as_view(), name='explorer_index'),
]
