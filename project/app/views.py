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

    return render('landing_page.html','landing_page.html',data)
