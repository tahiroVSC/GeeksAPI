from rest_framework.generics import ListAPIView
from apps.contacts.serializers import ContactSerializer
from apps.contacts.models import Contact


class ContactListCreate(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'


# class ContactsDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     lookup_field = 'id'
