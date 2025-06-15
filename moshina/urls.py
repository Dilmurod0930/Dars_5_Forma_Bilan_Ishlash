from  django.urls import path
from  .views import main, moshina_lst, moshina_info, moshina_update_form, moshina_add_form, moshina_delete
urlpatterns = [
    path('', main, name='main'),
    path('moshina/', moshina_lst, name='moshina_lst'),
    path('moshina/<int:id>/', moshina_info, name='moshina_info'),
    path('moshina_update/<int:id>/', moshina_update_form, name='moshina_update'),
    path('moshina_add/', moshina_add_form, name='moshina_add'),
    path('moshina_delete/<int:id>/', moshina_delete, name='moshina_delete'),
]
