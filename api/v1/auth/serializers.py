from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from posts.models import User, Customer


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","role","email","is_superuser")


class UserAllDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('username', 'email', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validate_data):
        # role = validate_data['role']
        role = validate_data.get('role',User.Role.ADMIN)
        print(role)

        if(role == "ADMIN"):
            user = User(
                username=validate_data['username'],
                email=validate_data['email'],
                # role=role
                role=validate_data.get('role', User.Role.CUSTOMER)
            )
            user.set_password(validate_data['password'])
            user.save()
            return user
        if(role == "USER"):
            user = Customer(
                username=validate_data['username'],
                email=validate_data['email'],
                # role=role
                role=validate_data.get('role', User.Role.CUSTOMER)
            )
            user.set_password(validate_data['password'])
            user.save()
            return user




        # def create(self, validated_data):
        #     role = validated_data['role']
        #     password = make_password(validated_data['password'])
        #     if role == "ADMIN":
        #         user = User.objects.create_superuser(
        #             username=validated_data['username'],
        #             email=validated_data['email'],
        #             password=password,
        #             role=role,
        #             is_superuser=True
        #     )
        #     elif role == "USER":
        #         user = User.objects.create_user(
        #             username=validated_data['username'],
        #             email=validated_data['email'],
        #             password=password,
        #             role=role,
        #             is_superuser=False
        #         )
        #     return user