from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='polls:question-detail'
    )
    class Meta:
        model = Question
        fields = '__all__'
        
