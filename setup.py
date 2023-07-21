from setuptools import setup, find_packages

setup(name='GOT_IT',version='0.0.2',
      author = 'Sourav',
      author_email = 'dharsourav03@gmail.com',
      packages = find_packages(),
      import_requires = ['numpy', 'pandas', 'flask']
      )