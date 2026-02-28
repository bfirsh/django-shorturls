import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-shorturls",
    version = "3.0.0",
    url = 'https://github.com/bfirsh/django-shorturls',
    license = 'BSD',
    description = "A URL shortening app for Django.",
    long_description = read('README.rst'),

    author = 'Simon Willison, Jacob Kaplan-Moss',
    author_email = 'jacob@jacobian.org',

    packages = find_packages('src'),
    package_dir = {'': 'src'},

    python_requires = '>=3.8',
    install_requires = ['setuptools', 'Django>=4.2'],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Framework :: Django :: 5.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
