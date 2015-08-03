from urlparse import urlparse
from flask import abort, render_template, request
import requests

layout_url = 'http://www.keyboard-layout-editor.com/layouts/'

def fetch_kle_json(url):
    """Returns the parsed JSON for a keyboard-layout-editor URL.
    """
    url = urlparse(request.form.get('kle_url'))

    try:
        layout_id = url.fragment.split('/')[2]
        keyboard = requests.get(layout_url + layout_id)
        return keyboard.json()

    except IndexError:
        abort(400)  # They gave us an invalid URL


def render_page(page, **args):
    """Returns a rendered template.

    This is a wrapper around render_template() to make it a bit easier to
    deliver templates. It will automatically tack .html onto the end of page
    so your calls are slightly shorter, and it will add the following values
    to args so that this information is always available to your templates:

    * FIXME
    """
    return render_template(page + '.html', **args)