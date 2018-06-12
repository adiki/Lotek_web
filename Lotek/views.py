from django.http import HttpResponse
from django.shortcuts import render
from random import randint
from datetime import datetime
import json
import math
import uuid

from Lotek.models import User

lookup = {}


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
    randoms_number = int(request.POST.get('randomsNumber'))

    results = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 ,6: 0 }
    for i in range(0, randoms_number):
        number = randint(0, 13983815)
        randomed = lookup[number]

        result = 0
        for selected_number in selected_numbers:
            if selected_number in randomed:
                result += 1
        results[result] += 1

    try:
        u = User.objects.get(token=uuid.UUID(request.POST.get('token')))
        u.money += randoms_number * -3 + results[3] * 24 + results[4] * 120 + results[5] * 3600 +  results[6] * 2000000
        u.randoms += randoms_number
        u.save()
    except User.DoesNotExist:
        pass


    response_data = {"results": results}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def ranking(_):

    results = User.objects.all().order_by("-money")
    results = [ { "money": r.money, "randoms": r.randoms } for r in results]

    return HttpResponse(json.dumps(results), content_type="application/json")


def user(_):
    u = User()
    u.save()
    response_data = {"token": str(u.token) }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def money(request):

    loteks_money = reduce(lambda r, m: r + m, map(lambda usr: -usr.money, User.objects.all()), 0)

    try:
        u = User.objects.get(token=uuid.UUID(request.POST.get('token')))
        response_data = {"yours": u.money, "loteks": loteks_money}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    except User.DoesNotExist:
        response_data = {"yours": 0, "loteks": loteks_money}
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def number_for_selected_numbers(selected_numbers):
    selected_numbers = sorted(selected_numbers)
    result = 0
    for i, number in enumerate(selected_numbers):
        result += newton(49 - number, 6 - i)
    return result


def random_numbers():
    bools = [False for _ in range(49)]
    numbers = []

    while len(numbers) < 6:
        number = randint(0, 48)
        if not bools[number]:
            numbers.append(number)
            bools[number] = True

    return sorted(numbers)

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

for a in range(1, 45):
    for b in range(a + 1, 46):
        for c in range(b + 1, 47):
            for d in range(c + 1, 48):
                for e in range(d + 1, 49):
                    for f in range(e + 1, 50):
                        r = number_for_selected_numbers([a,b,c,d,e,f])
                        lookup[r] = [a,b,c,d,e,f]
                        print(str(r) + str(lookup[13983815]))
print('Done')