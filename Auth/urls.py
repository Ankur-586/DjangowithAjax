from django.urls import path
from . import views

urlpatterns = [
    path('reg/',views.reg_user,name='register'),
    
    # Login first step
    path('login/',views.email_login_first_step,name='email_login_first_step'),
    path('login_step2/',views.login_step2,name='login_step2'),
    path('logout',views.logout_view,name='logout'),
]