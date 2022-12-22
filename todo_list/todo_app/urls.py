from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('' , views.listListView.as_view() , name='lists'), #done
    #path('<int:pk>/' , views.listDetail, name='list'), #done
    path('list/<int:pk>/' , views.ListDetailView.as_view() , name='list-detail'), #done
    
    path('list/add' , views.listCreateView.as_view() , name="create-list" ), #done
    path('Item/add/<int:pk>' , views.ItemCreateView.as_view() , name="create-Item" ),#done
    path('<pk>/delete/',views.listDeleteView.as_view(), name='delete-list'), #done
    

]