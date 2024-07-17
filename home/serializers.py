# from rest_framework import serializers
# from .models import *



# class StudentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = student
#         #fields=['name','age']
#         #exclude=[]
#         fields='__all__'

#     def validate(self,data):
#         if(data['age']<18):
#             raise serializers.ValidationError({'error':"Age must be greater than 18"})
        
#         if(data['name']):
#             for n in data['name']:
#                 if n.isdigit():
#                     raise serializers.ValidationError({'error':"name can't contain numeric values"})
#         return data
    

# class CategorySerializer(serializers.ModelSerializer):
     
#     model = category
#     fields='__all__'



# class BookSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True)
    
#     class Meta:
#         model = book
#         fields = '__all__'



# serializers.py
from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error': "Age must be greater than 18"})
        if any(char.isdigit() for char in data['name']):
            raise serializers.ValidationError({'error': "Name can't contain numeric values"})
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = book
        fields = '__all__'

