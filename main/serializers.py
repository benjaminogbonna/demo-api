"""Serializers for the user API View"""
from django.contrib.auth import get_user_model, authenticate, update_session_auth_hash
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     """Serializer fot the user object."""
#
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'password', 'agreed_to_terms_and_p_policy']
#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#                 'min_length': 8,
#             }
#         }
#
#     def create(self, validated_data):
#         """Create and return a user with encrypted password"""
#         return get_user_model().objects.create_user(**validated_data)
#
#     def update(self, instance, validated_data):
#         """Update and return user"""
#         password = validated_data.pop('password', None)
#         user = super().update(instance, validated_data)
#
#         if password:
#             user.set_password(password)
#             user.save()
#
#         return user
#
#
# class AuthTokenSerializer(serializers.Serializer):
#     """Serializer for the user auth token."""
#     email = serializers.EmailField()
#     password = serializers.CharField(
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#     )
#
#     def validate(self, attrs):
#         """Validate and authenticate the user."""
#         email = attrs.get('email')
#         password = attrs.get('password')
#         user = authenticate(
#             request=self.context.get('request'),
#             username=email,
#             password=password,
#         )
#         if not user:
#             msg = _('Unable to authenticate with provided credentials.')
#             raise serializers.ValidationError(msg, code='authorization')
#
#         attrs['user'] = user
#         return attrs
#
#
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "name",
            "phone",
            "address",
            "city",
            "country",
            "agreed_to_terms_and_p_policy",
            "is_active",
            "date_joined",
        ]
        read_only_fields = ["id", "date_joined", "is_active"]

class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer fot the user object."""

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'agreed_to_terms_and_p_policy']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
            }
        }

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
