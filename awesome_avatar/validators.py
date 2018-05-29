from django.core.validators import FileExtensionValidator, get_available_image_extensions

def validate_avatar_file_extension(value):
    return FileExtensionValidator(allowed_extensions=get_available_image_extensions())(value['file'])
