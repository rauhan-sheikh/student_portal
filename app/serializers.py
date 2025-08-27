from rest_framework import serializers
from .models import CustomUser, Staff, Student, Course, Subject
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "user_type", "is_active"]
        extra_kwargs = {
            "password": {"write_only": True},  # don’t expose password in GET
        }
    def create(self, validated_data):
        password = validated_data.pop("password", None)  # remove password safely
        user = User(**validated_data)                    # no raw password here
        if password:
            user.set_password(password)                  # hash if provided
        user.save()
        return user


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)

    class Meta:
        model = Staff
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = "__all__"
