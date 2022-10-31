from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from teacher.models import Class, Teacher
from teacher.serializers import TeacherSerializer, RegisterClassSerializer, ClassSerializer

class TeacherAPIView(APIView):
  def get(self, request, format=None):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data, HTTP_200_OK)

class RegisterClassAPIView(APIView):
  def post(self, request, id, format=None):
    teachers = get_object_or_404(Teacher, id=id)
    serializer = RegisterClassSerializer(data=request.data)

    if serializer.is_valid():
      class_teacher = Class(
        name=serializer.validated_data.get('name'), 
        email=serializer.validated_data.get('email'), 
        teacher=teachers
        )
      class_teacher.save()
      class_serializer = ClassSerializer(class_teacher, many=False)
      return Response(class_serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)