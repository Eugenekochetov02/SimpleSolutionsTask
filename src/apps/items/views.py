from django.shortcuts import render


def items(request):
    print(SECRET_KEY)
    return render(request, 'items/items.html')


def item(request):
    return render(request, 'items/item.html')
