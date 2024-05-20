from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name="home"), 
    path('about',views.about,name="about"), 
    path('signup',views.signup,name="signup"), 
    path('signin',views.signin,name="login"),
    path('myprofile',views.myprofile,name="myprofile"),
    path('signout',views.signout,name="signout"),
    path('adminLogin',views.adminLogin,name="adminLogin"),
    path('allUser',views.allUsers,name="allUser"),
    path('allServiceMan',views.allServiceMan,name="allServiceMan"),
    path('admin1',views.admin1,name="admin1"),
    path('user',views.user,name="user"),
    path('order',views.order,name="order"),
   
    path('myorder',views.myorder,name="myorder"),
    path('bookNow/<int:id>/',views.bookNow,name="bookNow"),
    path('services',views.services,name="services"),
    path('addServices',views.addServices,name="addServices"),
    path('del-service',views.delServices,name="delServices"),
    path('deleteServices/<int:id>/',views.deleteServices,name="deleteServices"),
    path('deleteUser/<int:id>/',views.deleteUser,name="deleteUser"),
    path('deleteOrder/<int:id>/',views.deleteOrder,name="deleteOrder"),
    
    path('deleteServiceman/<int:id>/',views.deleteServiceman,name="deleteServiceman"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)