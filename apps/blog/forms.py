from django import forms
from .models import Post, Comment

from ckeditor.widgets import CKEditorWidget


class CommentCreateForm(forms.ModelForm):
    """
    Форма добавления комментариев к статьям
    """

    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 5, 'placeholder': 'Комментарий', 'class': 'form-control'}),
    )

    class Meta:
        model = Comment
        fields = ('content',)


class PostCreateForm(forms.ModelForm):
    """
    Форма добавления статей на сайте
    """

    title = forms.CharField(widget=CKEditorWidget(
        config_name='awesome_ckeditor'))

    class Meta:
        model = Post
        fields = ('title', 'slug', 'category', 'description', 'text', 'thumbnail', 'status')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


class PostUpdateForm(PostCreateForm):
    """
    Форма обновления статьи на сайте
    """

    class Meta:
        model = Post
        fields = PostCreateForm.Meta.fields + ('fixed',)

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)

        self.fields['fixed'].widget.attrs.update({'class': 'form-check-input'})
