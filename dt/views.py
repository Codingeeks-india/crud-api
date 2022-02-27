from django.shortcuts import render
from api.models import *
# Create your views here.
from django_serverside_datatable.views import ServerSideDatatableView


class ItemListView(ServerSideDatatableView):
	queryset = Product.objects.all()
	columns = ['title']
