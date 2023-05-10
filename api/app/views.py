from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Employee
from .serializers import Employeeserializer,Userserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def employeelistview(request):
    if request.method=='GET':
        employees=Employee.objects.all()#queryset list
        employeedata=Employeeserializer(employees,many=True)#name,email,password,phone
        return JsonResponse(employeedata.data,safe=False)#[orderdict([('name,jai),(email,ja@gmail.com)])]
    else:
        jsondata=JSONParser().parse(request)
        serializer=Employeeserializer(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            JsonResponse(serializer.errors,safe=False)
def userlistview(request):
    user=User.objects.all()
    userdata=Userserializer(user,many=True)
    return JsonResponse(userdata.data,safe=False)

@csrf_exempt
def employeedetailview(request,pk):
    try:
        employee=Employee.objects.get(pk=pk)
    except:
        return JsonResponse("not found",safe=False)
    if request.method=="GET":
        employee=Employeeserializer(employee)
        return JsonResponse(employee.data,safe=True)

    if request.method == "PUT":
        jsondata=JSONParser().parse(request)
        serializer=Employeeserializer(employee,data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)

    if request.method=="DELETE":
        employee.delete()
        return JsonResponse("DELETED SUCCESSFULLY",safe=False)
