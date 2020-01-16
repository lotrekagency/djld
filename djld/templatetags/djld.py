import json
import os

from django import template
from django.conf import settings
from django.template import Template, Context
from django.utils.safestring import mark_safe

from djld.errors import DjLdException


register = template.Library()


@register.simple_tag(takes_context=True)
def structured_data(context, template, data_context={}):
    if type(template) == dict:
        rendered = json.dumps(template, indent=2)
    else:
        data_context['request_context'] = context
        ld_files_path = getattr(
            settings, 'LD_JSON_PATH',
            os.path.join(settings.BASE_DIR, 'ldjson')
        )
        with open(os.path.join(ld_files_path, template)) as template_file:
            tempalte_content = template_file.read()
            tmpl = Template(tempalte_content)
            rendered = tmpl.render(Context(data_context))
            rendered = rendered.replace('\n', '').replace('\r', '')
            try:
                json.loads(rendered)
            except ValueError:
                raise DjLdException('Invalid JSON content in template')
    rendered = '<script type="application/ld+json">\n' + rendered + '\n</script>'
    return mark_safe(rendered)
