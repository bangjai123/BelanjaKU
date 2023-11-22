from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('hapus-item/<int:id>',hapus_item,name="hapus_item"),
    path('tambah-item/<int:id>',tambah_item,name="tambah_item"),
    path('kurangi-item/<int:id>',kurangi_item,name="kurangi_item"),
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('json/', show_json, name='show_json'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]