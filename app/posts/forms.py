from django import forms

from posts.models import Post


class PostCreateForm(forms.Form):
    photo = forms.ImageField(
        widget= forms.ClearableFileInput(
            attrs={
                'class': 'form-control-file'
            }
        )
    )
    comment = forms.CharField(
        required=False,
        widget= forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '3',
            }
        )
    )

    def save(self, author):
        post = Post.objects.create(
            author=author,
            photo=self.cleaned_data['photo'],
        )

        if self.cleaned_data.get('comment'):
            post.comment_set.create(
                author=author,
                content=self.cleaned_data['comment']
            )
        return post
