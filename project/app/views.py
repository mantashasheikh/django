from django.shortcuts import render

# Create your views here.
def landing_page(req):
    data={
        'name':'Vinika',
        'college':'RITS'
    }
    # return render(req,'landing_page.html',data)
    # return render(req,'landing_page.html')
    # return render('landing_page.html',req) # order of parameters is wrong, it should be request first and then template name and then data.
    # return render(req) # render() missing 1 required positional argument: 'template_name'

    return render(req,'landing_page.html',data)


def login(req):
    return render(req,'login.html')

def register(req):
    return render(req,'register.html')

def contact(req):
    return render(req,'contact.html')