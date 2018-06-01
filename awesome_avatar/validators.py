from django.core.validators import FileExtensionValidator, get_available_image_extensions

def validate_avatar_file_extension(value):
    
    validator = FileExtensionValidator(allowed_extensions=get_available_image_extensions())
    validation = None    
    
    try:
        value.get('box', None)
        value = value['file']
        if value:
            validation = validator(value['file'])
    except:
        validation = validator(value)

    return validation
