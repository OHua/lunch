# stores/view.py

from django.shortcuts import redirect,render
#from django.forms.models import modelform_factory
from .forms import StoreForm
from .models import Store

#from django.http import HttpResponse

# Create your views here.

def store_list(request):
	stores = Store.objects.all()
	return render(request, 'stores/store_list.html', {'stores': stores})

def store_detail(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    return render(request, 'stores/store_detail.html', {'store': store})
	
def store_create(request):
    #StoreForm = modelform_factory(Store, fields=('name', 'notes',))
    if request.method == 'POST':
        form = StoreForm(request.POST,submit_title='建立')
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(submit_title='建立')
    return render(request, 'stores/store_create.html', {'form': form})
	
def store_update(request, pk):
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        raise Http404
    #StoreForm = modelform_factory(Store, fields=('name', 'notes',))
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store,submit_title='更新')
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())
    else:
        form = StoreForm(instance=store,submit_title='更新')
    return render(request, 'stores/store_update.html', {
        'form': form, 'store': store,
    })