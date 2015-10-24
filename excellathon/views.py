from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse

@api_view(['POST'])
def fibonacci(request):
    input = request.data
    output = []
    response = '{"data":['
    for i in input:
        index = 0
        num1, num2 = 0, 1
        j = 0
        while j < i:
            fibonacci = num1 + num2;
            num1 = num2
            num2 = fibonacci
            j = j+1
        output.append(str(num1))
    output_str = ', '.join(output)
    response = response + output_str + ']}'
    return HttpResponse(response, content_type='application/json')
    

@api_view(['POST'])
def fizzbuzz(request):
    input = request.data
    output = []
    response = {'data': ''}
    print input
    for i in input:
        text = str(i)
        if i % 2 == 0:
            text = 'Fizz'
        if i % 3 == 0:
            text = 'Buzz'
        if i % 2 == 0 and i % 3 == 0: 
            text = 'FizzBuzz'
        output.append(str(text))
    response['data'] = output
    print response
    return JsonResponse(response)
    
@api_view(['POST'])
def anagram(request):
    input = request.data
    print input
    output = []
    response = {'data': ''}
    print input
    for i in input:
        text1 = str(i[0])
        text2 = str(i[1])
        sorted_1 = sorted(text1)
        sorted_2 = sorted(text2)
        print sorted_1
        print sorted_2
        if sorted_1 == sorted_2:
            check = True
        else:
            check = False
        output.append(check)
    response['data'] = output
    print response
    return JsonResponse(response)

@api_view(['POST'])
def prime_number(request):
    input = request.data
    print input
    output = []
    response = {'data': ''}
    print input
    for i in input:
        check = True
        if i >= 2:
            for j in range(2,i):
                if not ( i % j ):
                    check = False
        else:
    	   check =  False
        output.append(check)
    response['data'] = output
    print response
    return JsonResponse(response)

@api_view(['POST'])
def palindrome(request):
    input = request.data
    print input
    output = []
    response = {'data': ''}
    print input
    for i in input:
        text = str(i)
        reverse = text[::-1]
        if text == reverse:
            check = True
        else:
            check = False
        output.append(check)
    response['data'] = output
    print response
    return JsonResponse(response)
