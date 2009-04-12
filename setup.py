import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-shorturls",
    version = "1.0",
    url = 'http://github.com/jacobian/django-shorturls',
    license = 'BSD',
    description = "A short URL (rev=cannonical) handler for Django apps.",
    long_description = read('README'),

    author = 'Simon Willison, Jacob Kaplan-Moss',
    author_email = 'jacob@jacobian.org',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
    ]
)