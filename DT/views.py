from . models import Student
from . serializers import StudentSerializers
from django.http import HttpResponse
from rest_framework_xml.renderers import XMLRenderer

def student_details(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu, many=True)
    XML_data = XMLRenderer().render(serializer.data)
    return HttpResponse(XML_data)

def XML_DATA(request):
    return HttpResponse(student_details(request))