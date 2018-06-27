from django import forms

from awesome_avatar.settings import config
from awesome_avatar.widgets import AvatarWidget
from awesome_avatar.validators import validate_avatar_file_extension 


class AvatarField(forms.ImageField):
    default_validators = [validate_avatar_file_extension]
    widget = AvatarWidget

    def __init__(self, **defaults):
        self.width = defaults.pop('width', config.width)
        self.height = defaults.pop('height', config.height)
        super(AvatarField, self).__init__(**defaults)

    def to_python(self, data):
        try:
            fp = data.get('file', None)
        except:
            fp = data           
        super(AvatarField, self).to_python(data)
        return data

    def widget_attrs(self, widget):
        return {'width': self.width, 'height': self.height}
