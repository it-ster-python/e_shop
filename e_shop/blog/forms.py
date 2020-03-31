from django import forms
from blog import models


class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = "__all__"
        exclude = ["add_time"]
        widgets = {
            "comment_article": forms.HiddenInput()
        }
