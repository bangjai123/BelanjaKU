from django.urls import path
from main.views import show_main, create_item, show_json, show_xml, show_json_by_id,show_xml_by_id,register,login_user,logout_user,hapus_item, tambah_item,kurangi_item


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
]