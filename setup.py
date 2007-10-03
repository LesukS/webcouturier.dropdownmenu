from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='webcouturier.dropdownmenu',
      version=version,
      description="Adds a dropdown functionality to global navigation in Plone",
      long_description="""\
You will get the dropdown menus for those items in global navigation that have the subitems. Submenus are build based on the same policy as the Site Map, so it will show the same tree as you would get in the Site Map or navigation portlet being in appropriate section. Requires plone.browserlayer to be installed in your site.""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web couturier dropdown menu navigation',
      author='Denis Mishunov (Web Couturier)',
      author_email='denis@webcouturier.com',
      url='http://svn.plone.org/svn/collective/webcouturier.dropdownmenu',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['webcouturier'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.browserlayer',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )