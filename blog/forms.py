from django import forms
from .models import Category, Post, Comment, Response
from ckeditor.widgets import CKEditorWidget

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': 'Nombre'}
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'description', 'content', 'category']
        labels = {
            'title': 'Título',
            'image': 'Imagen',
            'description': 'Descripción',
            'content': 'Contenido',
            'category': 'Categoría',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment']
        labels = {
            'author': 'Autor',
            'comment': 'Comentario',
        }
        
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['response']
        labels = {
            'response': 'Respuesta',
        }