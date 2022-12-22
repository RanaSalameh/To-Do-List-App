from django.shortcuts import render,get_object_or_404
from django.views.generic import (ListView,CreateView,UpdateView,DetailView,DeleteView)
from .models import ToDoList,ToDoItem
from django.urls import reverse_lazy,reverse

# Create your views here.
class listListView(ListView):
    model = ToDoList
    template_name = "todo_app/lists.html"
    

class ListDetailView(ListView):
    model = ToDoItem
    template_name = "todo_app/listDetail.html"
    
    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs['pk'])  #nameInModel _id 
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] =ToDoList.objects.get(id = self.kwargs['pk'])
        #context['items'] = self.get_queryset()
        return context

class listCreateView(CreateView):
    model = ToDoList
    template_name = "todo_app/createForm.html"
    #fields=['todo_list' , 'title' , 'description' , 'due_date']
    fields = ['title']
    success_url=reverse_lazy('todo_app:lists')
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add new List'
        return context

class listDeleteView(DeleteView):
    model= ToDoList
    template_name="todo_app/todolist_confirm_delete.html"
    
    success_url=reverse_lazy('todo_app:lists')


class  ItemCreateView(CreateView):
    model = ToDoItem
    template_name = "todo_app/createForm.html"
    fields=['todo_list' , 'title' , 'description' , 'due_date']
    
    
    def get_initial(self):
        initial_data = super(ItemCreateView , self).get_initial()
        list_obj= get_object_or_404(ToDoList,pk= self.kwargs['pk'])
        initial_data['todo_list'] = list_obj
        return initial_data
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['listID'] = self.kwargs['pk']
        context['title'] = 'Create new item'

        return context
    
    def get_success_url(self) -> str:
        return reverse('todo_app:list-detail' ,kwargs={'pk' : self.kwargs['pk'] } )