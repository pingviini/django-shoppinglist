from setuptools import setup, find_packages

version = '0.1'

setup(name='django-shoppinglist',
      version=version,
      description="",
      long_description="%s\n%s" % (
          open("README.rst").read(),
          open("CHANGES.rst").read()),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Django",
          "Framework :: Django :: 1.6",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.3",
      ],
      keywords='',
      author='Jukka Ojaniemi',
      author_email='jukka.ojaniem@gmail.com',
      url='https://github.com/pingviini/django-shoppinglist',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Django',
          'setuptools',
          'zope.interface',
          'zope.component',
          # -*- Extra requirements: -*-
      ],
      extras_require={
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )