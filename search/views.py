from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from itertools import chain


class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        # Here we are spliting the searched string after comma 
        # and saving them in a list
        queryList = query.split(', ')
        object_list = []
        for query in queryList:
            # and here we are looping through that list one by one 
            # and looking up the query for that object in database
            # the search function returning an queryset
            # and we are merging all the list to an signle list
            object_list = chain(object_list,Product.objects.search(query))
        return object_list
        
