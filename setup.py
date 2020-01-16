from setuptools import setup, find_packages


setup(
    name='djld',
    version='1.0.1',
    url='https://github.com/lotrekagency/djld',
    install_requires=[],
    description="Structured data with Django",
    long_description=open('README.rst').read(),
    license="MIT",
    author="Lotrek",
    author_email="dimmitutto@lotrek.it",
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
