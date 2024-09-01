import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

thid_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        precent = (page_qs.count() * 100.0) / qs.count()
    except:
        precent = 0
    my_title = "My Page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "precent": precent,
        "total_visit_count": qs.count()
    }
    path = request.path
    print("path", path)
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Document</title>
        </head>
        <body>
            <h1>{page_title} is anything?</h1>
        </body>
        </html>
    """.format(**my_context)
    # html_file_path = thid_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)