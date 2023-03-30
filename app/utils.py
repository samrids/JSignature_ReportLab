import base64
import io

from django import template

from django.utils.encoding import iri_to_uri

from jsignature.utils import draw_signature

# register = template.Library()


# @register.filter
def signature_base64(value):
    if value is None or not isinstance(value, str):
        return ""
    in_mem_file = io.BytesIO()
    draw_signature(value).save(in_mem_file, format="PNG")
    in_mem_file.seek(0)

    # print ( iri_to_uri(base64.b64encode(in_mem_file.read()).decode('utf8')) )
    

    return "data:image/png;base64,{}".format(
        iri_to_uri(base64.b64encode(in_mem_file.read()).decode('utf8'))
    )

def signature_2base64(value):
    if value is None or not isinstance(value, str):
        return ""
    in_mem_file = io.BytesIO()
    draw_signature(value).save(in_mem_file, format="PNG")
    in_mem_file.seek(0)
    
    # print ( iri_to_uri(base64.b64encode(in_mem_file.read()).decode('utf8')) )
    return "{s}".format(s=iri_to_uri(base64.b64encode(in_mem_file.read()).decode('utf8')))