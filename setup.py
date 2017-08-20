from setuptools import setup

setup(
    name='quora_clone',
    packages=['quora_clone'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask-session', 'flask-pymongo', 'flask-cli', 'gunicorn'
    ],
)