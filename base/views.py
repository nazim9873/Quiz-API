from .models import Quiz, Option
from .serializers import QuizSerializers, QuizListSerializers
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import datetime 
from django.utils import timezone
utc=timezone.utc
now = datetime.datetime.now().replace(tzinfo=utc)

@cache_page(5*60)
@api_view(['GET','POST'])
def quiz_list(request):
    if request.method == 'GET':
        quizzes = Quiz.objects.all()
        serializers = QuizListSerializers(quizzes,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        # add option as dictionary
        option_list_to_dict(request)

        serializers = QuizSerializers(data=request.data)
        if serializers.is_valid():
            obj = serializers.save()
            return Response({"created quiz with id": str(obj.id) }, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
def option_list_to_dict(request):
    option =[]
    option_list = request.data['option']
    for index, value in enumerate(option_list):
        if index  == request.data['right_answer']:
            correct = True
        else:
            correct = False
        option.append({"text":value,'correct':correct})
    request.data['option'] = option

@cache_page(5*60)
@api_view(['GET'])
def quiz_active(request):
    if request.method == 'GET':
        quizzes = Quiz.objects.filter(start_date__lte=now,end_date__gte=now)
        serializers = QuizListSerializers(quizzes,many=True)
        return Response(serializers.data)

@api_view(['GET'])
def quiz_result(request ,pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
    except Quiz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # making datetime naive for comparison
        if quiz.end_date.replace(tzinfo=utc) <  now - datetime.timedelta(minutes=5):
            serializers = QuizListSerializers(quiz)
            result = serializers.data['option'][serializers.data['right_answer']]
            return Response({"result" : result})
        else:
            result_time = quiz.end_date.replace(tzinfo=utc) + datetime.timedelta(minutes=5)
            return Response({"status" : f"results will be available after {result_time}"})

    
