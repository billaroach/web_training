from django.forms import ModelForm
from .models import Comments, Beer


class CommentForm(ModelForm):

    class Meta:

        model = Comments
        fields = ['comments_name', 'comments_text']


class AddBeerForm(ModelForm):

    class Meta:

        model = Beer
        fields = ['mark', 'color', 'style', 'strength', 'country', 'info']