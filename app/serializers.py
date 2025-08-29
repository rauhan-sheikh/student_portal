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


from rest_framework import serializers
from .models import CustomUser

class ProfileSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "user_type", "address", "course"]
        read_only_fields = fields

    def get_address(self, obj):
        if obj.user_type == 2 and hasattr(obj, "staff"):
            return obj.staff.address
        elif obj.user_type == 3 and hasattr(obj, "student"):
            return obj.student.address
        return None

    def get_course(self, obj):
        if obj.user_type == 3 and hasattr(obj, "student") and obj.student.course:
            return obj.student.course.name
        return None

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect")
        return value

    def save(self, **kwargs):
        user = self.context["request"].user
        new_password = self.validated_data["new_password"]
        user.set_password(new_password)
        user.save()
        return user
