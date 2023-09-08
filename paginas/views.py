from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getPages(request):
    return HttpResponse("Hello, world. You're at the GetPages index.")

#concatenar el id al mensaje de HttpResponse
def getPage(request, page_id):
    return HttpResponse("This is the getPage page. Id: " + str(page_id))

def createPage(request):
    return HttpResponse("This is the createPage page.")

def updatePage(request):
    return HttpResponse("This is the updatePage page.")

def deletePage(request):
    return HttpResponse("This is the deletePage page.")
