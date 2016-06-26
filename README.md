1.
```
INSTALLED_APPS = (
    ...
    'easy_thumbnails',
    'filer',
    'mptt',
    'ckeditor_filer',
    ...
)

```

2.
```
urlpatterns = [
    ...
    url(r'^ckeditor_filer/', include('ckeditor_filer.urls')),
    ...
]

```
3.
```
from django import forms

from ckeditor_filer.widget import CKEditorWidget


class MyForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Content

        ck_editor_config = {
            'height': '350',
            'extraPlugins': 'filerimage',
            'removePlugins': 'image'
        }
        widgets = {
            'content': CKEditorWidget(attrs={'id': 'X-content'}, editor_options=ck_editor_config),
        }

```
