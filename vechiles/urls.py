from django.urls import path
from vechiles.views import SignupView,SignInView,IndexView,VechileCreateView,logoutview,VechileListView,VechileDetailView,\
delete_view,VechileUpdateView

urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('signin/', SignInView.as_view(), name="signin"),
    path('signout/', logoutview, name="signout"),
    path('index/', IndexView.as_view(), name="home"),
    path('add/', VechileCreateView.as_view(), name="add"),
    path('list/', VechileListView.as_view(), name="list"),
    path('<int:pk>/', VechileDetailView.as_view(), name="detail"),
    path('<int:pk>/delete', delete_view, name="delete"),
    path('<int:pk>/update', VechileUpdateView.as_view(), name="update"),
]