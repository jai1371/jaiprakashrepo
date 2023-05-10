from rest_framework import serializers
from .models import Employee


class Employeeserializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    phone = serializers.IntegerField()
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    def update(self, employee, validated_data):
        newemployee=Employee(**validated_data)
        newemployee.id= employee.id
        newemployee.save()
        return newemployee
class Userserializer(serializers.Serializer):
    username=serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
