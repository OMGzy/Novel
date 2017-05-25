from django.shortcuts import render
from django.http import HttpResponse
from people.models import Novel, Chapter

def index(request):
    novel = Novel.objects.order_by('novelid')[:30]
    return render(request, 'index.html', {'novels':novel})

def novel_list(request, novelid):
    novel = Novel.objects.filter(novelid=novelid)[0]
    chapters = Chapter.objects.filter(novelid=novelid).order_by('chapterid')[:50]
    return render(request, 'chapter.html', {'novel':novel, 'chapters': chapters})

def chapter_list(request, chapterid):
    chapter = Chapter.objects.get(chapterid=chapterid)
    return render(request, 'content.html', {'chapter':chapter})
