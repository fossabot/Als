try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='Als',
    version='0.0.1-alpha',
    description="Python-based Advanced version of Bash's \"ls\"",
    author='UltraStudioLTD (Luka Mamukashvili)',
    author_email='ultraluka0@gmail.com',
    url='https://www.github.com/UltraStudioLTD/Als',
    packages=[
        'Als',
        ],
    scripts=[
        'Als/ls.py',
        'Als/tree.py',
        'Als/runner.py',
        'Als/Als.py',
        'Als/__init__.py',
        'Als/colors.py',
        'Als/permissions.py'
        ]
)
