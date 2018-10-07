from django.conf.urls import url, include
from . import views
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views
from django.contrib.auth.views import login 


router = routers.DefaultRouter()
router.register('myendpoint',ProductView )

urlpatterns = [
    # url(r'^$', views.home),
    url(r'', include(router.urls)),
    url(r'^api-token-auth', views.obtain_auth_token, name='api-token-auth'),

    #not sure how to test it with postman

    #test with httpie commandline program
    #aman@vostro:~$ http POST http://localhost:8000/api-token-auth username="aman" password="amandeep"
    #use the generated token like this
    #aman@vostro:~$ http GET http://localhost:8000/myendpoint/ "Authorization: Token ad061e8b1b6d4fc76718a5cb0dc32fe8106312fb"
 	#you should see the JSON response output

	#for testing session auth (admin can also be used instead)

    url(r'^login$', login, name='login'), #login using the predefined view
    url(r'^logout$', logoutView, name='logout'),
    url(r'^signup/$', signup, name='signup'),

    # this gives a predefined login button, also a callable api, but it gives csrf error on POST
    #https://asciinema.org/a/42177 #httpie POST request on this url
	url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),

]
