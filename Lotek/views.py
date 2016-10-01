from django.http import HttpResponse
from django.shortcuts import render
from random import randint
from datetime import datetime
import json
import math

from Lotek.models import Result


def index(request):
    numbers = []

    for i in range(7):
        row = []
        for j in range(7):
            number = i * 7 + j + 1
            row.append(number)
        numbers.append(row)

    return render(request, 'index.html', {'numbers': numbers})


def random(request):
    selected_numbers = [int(n) for n in request.POST.getlist('selectedNumbers[]')]

    # CHECK NUMBERS

    selected_number = number_for_selected_numbers(selected_numbers)

    found = False
    i = 0
    while not found:
        number = randint(0, 13983815)
        found = selected_number == number
        i += 1
    print(i)

    r = Result(date=datetime.now(), number=i)
    r.save()

    results = Result.objects.all().order_by("number")
    results = [r.number for r in results]

    order = results.index(i) + 1

    response_data = {"number": i, "order": order}

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def ranking(_):

    results = Result.objects.all().order_by("number")
    results = [r.number for r in results]

    if len(results) > 25:
        results = results[:25]

    return HttpResponse(json.dumps(results), content_type="application/json")


def number_for_selected_numbers(selected_numbers):
    selected_numbers = sorted(selected_numbers)
    result = 0
    for i, number in enumerate(selected_numbers):
        result += newton(49 - number, 6 - i)
    return result


# def random_numbers():
#     bools = [False for _ in range(49)]
#     numbers = []
#
#     while len(numbers) < 6:
#         number = randint(0, 48)
#         if not bools[number]:
#             numbers.append(number)
#             bools[number] = True
#
#     return sorted(numbers)


def newton(x, y):
    if y == x:
        return 1
    elif y == 1:  # see georg's comment
        return x
    elif y > x:  # will be executed only if y != 1 and y != x
        return 0
    else:  # will be executed only if y != 1 and y != x and x <= y
        a = math.factorial(x)
        b = math.factorial(y)
        c = math.factorial(x - y)  # that appears to be useful to get the correct result
        div = a // (b * c)
        return div
