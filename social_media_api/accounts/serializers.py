from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)  # ✅ Ensures CharField is explicitly present
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})  # ✅ Ensures CharField is explicitly present

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # ✅ Using get_user_model().objects.create_user() as required
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # ✅ Assign a token after successful user creation
        Token.objects.create(user=user)
        return user
