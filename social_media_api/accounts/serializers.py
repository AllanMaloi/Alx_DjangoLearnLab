from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)  # ✅ Explicitly using CharField
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})  # ✅ Explicitly using CharField

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        # ✅ Explicitly using get_user_model().objects.create_user()
        user = get_user_model().objects.create_user(username=username, email=email, password=password)

        # Create and assign a token to the new user
        Token.objects.create(user=user)

        return user
