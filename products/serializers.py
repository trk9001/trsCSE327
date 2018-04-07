from rest_framework import serializers
from .models import Product 

class productsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('url', 'id' , 'title' , 'description', 'image', 'price' )

     

   
     
