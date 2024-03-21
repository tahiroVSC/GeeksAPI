from django.urls import path
from apps.contacts import views

urlpatterns = [
    path('contacts/', views.ContactListCreate.as_view()),
    # path('contacts/<int:id>/', views.ContactsDetailView.as_view())
]
