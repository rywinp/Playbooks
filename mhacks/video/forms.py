from .models import Video
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['caption', 'video']

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Check if the field is a CharField (text input)
            if isinstance(field, forms.CharField):
                field.widget.attrs.update({
                    'class': 'border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
                })