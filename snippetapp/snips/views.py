from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, Http404
from .models import Snip
from django.core.urlresolvers import reverse_lazy

def add(request):
    if request.method == 'POST':
        # save dat data
        Snip(
            title=request.POST['title'],
            language=request.POST['language'],
            description=request.POST['description'],
            snip=request.POST['snip']
        ).save()

    return render(request, 'snips/add.html', {})

def delete_snip(request, pk):
    snip = Snip.objects.get(pk=pk)
    context = { 'snip': snip }
    snip.delete()

    return render(request,'snips/delete_snip.html', context)

def index(request):
    snips = Snip.objects.all()
    context = {'snips': snips}
    return render(request, 'snips/index.html', context)

class SnipUpdate(UpdateView):
    model = Snip
    fields = ['title','language','description','snip']
    success_url = reverse_lazy('snips:index')

# class SnippetCreate(CreateView):
#     model = Snippet
#     fields = ['title','language','description','snippet']

# class SnippetDelete(DeleteView):
#     model = Snippet
#     success_url = reverse_lazy('snippets:home')

def detail(request, snip_id):
    try:
        snip = Snip.objects.get(id=snip_id)
        context = { 'snip': snip  }
    except Snip.DoesNotExist:
        raise Http404('Aint no snip by that id!')

    return render(request, 'snips/detail.html', context)
