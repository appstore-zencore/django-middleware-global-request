import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "django",
]

setup(
    name="django-middleware-global-request",
    version="0.1.2",
    description="Django middleware that keep request instance for every thread.",
    long_description=long_description,
    url="https://github.com/appstore-zencore/django-middleware-global-request",
    author="zencore",
    author_email="appstore@zencore.cn",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords=['django-middleware-global-request'],
    packages=find_packages(".", exclude=["demo", "demo_test", "manage"]),
    requires=requires,
    install_requires=requires,
    zip_safe=False
)
