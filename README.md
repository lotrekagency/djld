# Djld

Structured data with Django

[![Latest Version](https://img.shields.io/pypi/v/djld.svg)](https://pypi.python.org/pypi/djld/)
[![codecov](https://codecov.io/gh/lotrekagency/djld/branch/master/graph/badge.svg)](https://codecov.io/gh/lotrekagency/djld)
[![Build Status](https://travis-ci.org/lotrekagency/djld.svg?branch=master)](https://travis-ci.org/lotrekagency/djld)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/lotrekagency/djld/blob/master/LICENSE)

## Installation
```sh
pip install djld
```

## Configuration

Add `djld` to your INSTALLED_APPS in settings.py, you can specify the folder containing your structured data overriding the `LD_JSON_PATH` variable

## Usage

To render structured data in your templates you need the `structured_data` template tag

```py
{% load djld %}

{% structured_data 'mydata.json' %}
```

You can use Django template sintax in your json files, and pass a context to the template tag

```py
render(request, 'myapp/index.html', {
    'user_data' : {
        'url' : 'https://lotrek.it',
        'name' : 'Human Before Digital'
    }
})
```

```py
{% load djld %}

{% structured_data 'mydata.json' user_data %}
```

You can also render a structured data from a dictionary, without using templates

```py
render(request, 'myapp/index.html', {
    'user_data' : {
        'url' : 'https://lotrek.it',
        'name' : 'Human Before Digital'
    }
})
```

```py
{% load djld %}

{% structured_data user_data %}
```


## Run tests
```sh
$ pip install -r requirements-dev.txt
$ make test
```
