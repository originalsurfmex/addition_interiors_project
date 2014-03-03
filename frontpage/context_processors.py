from frontpage.models import Title, Slider

def base_page(request):
    project_title = Title.objects.all()
    return { 'proj_title': project_title, }