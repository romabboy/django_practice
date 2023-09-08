import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import *


#
# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')

class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    # In this class fields must be the same as in Model class
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance - instance of Model
        # validate_data - data which appear after serializer.is_valid
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("is_published", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()

        return instance


def encode():
    model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
    model_sr = {'title': 'Angelina Jolie', 'content': 'Content: Angelina Jolie'}

    print(model_sr)
    print(dir(model_sr))
    print(model_sr, type(model_sr), type(model_sr), sep='\n')
    json = JSONRenderer().render(model_sr)
    print(json)


def decode():
    stream = io.BytesIO(b'{"title":"AJ","content":"Content: AJ"}')
    data = JSONParser().parse(stream)
    print(data)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
