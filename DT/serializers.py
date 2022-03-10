from rest_framework import serializers


class StudentSerializers(serializers.Serializer):
    Name = serializers.CharField(max_length=40)
    City = serializers.CharField(max_length=40)
    Country = serializers.CharField(max_length=40)
    Roll = serializers.IntegerField()
