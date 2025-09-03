from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495893',
        'name': 'Khayru R Prananta',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)