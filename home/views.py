
# views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import *
from .serializers import *
from rest_framework.views import APIView



class studentAPI(APIView):
    def get(self,request):
        student_obj = student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        return Response({"status": 200, "payload": serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "payload": serializer.data, "message": "Your data is saved"})
        return Response({"status": 403, "errors": serializer.errors, "message": "Something went wrong"})


    def put(self,request):
        try:
            student_obj = student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({"status": 403, "errors": serializer.errors, "message": "Something went wrong"})
            serializer.save()
            return Response({"status": 200, "payload": serializer.data, "message": "Your new data data is saved"})
        except Exception as e:
            return Response({"status": 403, "message": "Invalid ID", "error": str(e)})


    def patch(self,request):
        pass
    
    def delete(self,request):
        try:
            id=request.GET.get('id')
            student_obj = student.objects.get(id=id)
            student_obj.delete()
            return Response({"status": 200, "message": "Data has been deleted"})
        except Exception as e:
            return Response({"status": 403, "message": "Invalid ID", "error": str(e)})
        
    






















# @api_view(['GET'])
# def home(request):
#     student_obj = student.objects.all()
#     serializer = StudentSerializer(student_obj, many=True)
#     return Response({"status": 200, "payload": serializer.data})

@api_view(['GET'])
def viewBook(request):
    try:
        book_obj = book.objects.all()
        serializer = BookSerializer(book_obj, many=True)
        return Response({"status": 200, "payload": serializer.data})
    except Exception as e:
        return Response({"status": 403, "message": "Error in the function", "error": str(e)})

# @api_view(['POST'])
# def post_student(request):
#     serializer = StudentSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response({"status": 403, "errors": serializer.errors, "message": "Something went wrong"})
#     serializer.save()
#     return Response({"status": 200, "payload": serializer.data, "message": "Your data is saved"})

# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student_obj = student.objects.get(id=id)
#         serializer = StudentSerializer(student_obj, data=request.data, partial=True)
#         if not serializer.is_valid():
#             return Response({"status": 403, "errors": serializer.errors, "message": "Something went wrong"})
#         serializer.save()
#         return Response({"status": 200, "payload": serializer.data, "message": "Your data is saved"})
#     except Exception as e:
#         return Response({"status": 403, "message": "Invalid ID", "error": str(e)})

# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = student.objects.get(id=id)
#         student_obj.delete()
#         return Response({"status": 200, "message": "Data has been deleted"})
#     except Exception as e:
#         return Response({"status": 403, "message": "Invalid ID", "error": str(e)})

