import json

from django.forms import Textarea
from django.conf import settings
from django.utils.safestring import mark_safe


class CKEditorWidget(Textarea):
    class Media:
        js = (
            '//cdn.ckeditor.com/4.5.9/full/ckeditor.js',
        )

    def __init__(self, attrs=None, editor_options=None):
        super().__init__(attrs)
        self.editor_options = editor_options or {}

    def render(self, name, value, attrs=None):
        output = super().render(name, value, attrs)
        output += mark_safe('<script type="text/javascript">CKEDITOR.replace("{0}", {1});'
                            'CKEDITOR.plugins.addExternal("filerimage", "{2}ckeditor/plugins/filerimage/plugin.js");'
                            '</script>'.format(self.attrs['id'], json.dumps(self.editor_options), settings.STATIC_URL))
        return output
