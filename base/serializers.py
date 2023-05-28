from rest_framework import serializers
from base.models import Quiz, Option

class OptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"

#for create
class QuizSerializers(serializers.ModelSerializer):
    option = OptionSerializers(many=True)
    start_date = serializers.DateTimeField(input_formats=["%d/%m/%Y %H:%M:%S"])
    end_date = serializers.DateTimeField(input_formats=["%d/%m/%Y %H:%M:%S"])

    class Meta:
        model = Quiz
        fields = "__all__"

    def validate(self, data):
       # check date occurence
       if data['start_date'] > data['end_date']:
           raise serializers.ValidationError("end_date must occur after start_date")
       return data

    def create(self, validated_data):
        option_list = validated_data.pop('option')
        quiz_instance = Quiz.objects.create(**validated_data)
        for option in option_list:
            Option.objects.create(from_quiz=quiz_instance, **option)
        return quiz_instance
    
#for get
class QuizListSerializers(serializers.ModelSerializer):
    option = serializers.SerializerMethodField()
    right_answer = serializers.SerializerMethodField()
    start_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    end_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    def get_option(self, obj):
        choices = obj.option_set.all()
        return [choice.text for choice in choices]
        
    def get_right_answer(self, obj):
        choices = obj.option_set.all()
        right_choice = [choice.correct for choice in choices].index(True)
        return right_choice
    
    class Meta:
        model = Quiz
        exclude = ['created_date', ]

