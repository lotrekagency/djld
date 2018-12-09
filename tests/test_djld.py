import djld
from djld import DjLdException
import pytest
from django.shortcuts import render


def test_djld():
    response = render({}, 'tests/index.html')
    assert 'application/ld+json' in str(response.content)
    assert 'https://pypi.org/projects/djld' in str(response.content)


def test_djld_with_invalid_data():
    with pytest.raises(DjLdException):
        response = render({}, 'tests/invalid_index.html')


def test_djld_with_context():
    response = render({}, 'tests/index_with_context.html', {
        'myjson' : {
            'url' : 'https://lotrek.it',
            'name' : 'Human Before Digital'
        }
    })
    assert 'application/ld+json' in str(response.content)
    assert 'https://lotrek.it' in str(response.content)
    assert 'Human Before Digital' in str(response.content)
    assert '@type' not in str(response.content)


def test_djld_with_template_sintax():
    response = render({}, 'tests/index_with_template.html', {
        'myjson' : {
            'url' : 'https://lotrek.it',
            'name' : 'Human Before Digital'
        }
    })
    assert 'application/ld+json' in str(response.content)
    assert 'https://lotrek.it' in str(response.content)
    assert 'Human Before Digital' in str(response.content)
    assert '@type' in str(response.content)
