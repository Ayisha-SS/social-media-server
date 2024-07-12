from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import CreatePost

class CreateSerializer(ModelSerializer):

    # category = serializers.SerializerMethodField()

    class Meta:
        model = CreatePost
        fields = ("id",'title','image','category','description')

        # def to_internal_value(self, data):
        #     if 'category' in data:
        #         category_name = data.get('category')
        #         category, created = Categories.objects.get_or_create(name=category_name)
        #         data['category'] = category.id
        #     return super().to_internal_value(data)

    # def get_category(self,instance):
    #     return instance.category.name


# class CreateViewSerializer(ModelSerializer):

#     category = serializers.SerializerMethodField()

#     class Meta:
#         fields = ("id",'title','image','category','created_by','description')
#         model = ViewPost

#     def get_category(self,instance):
#         return instance.category.name