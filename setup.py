from setuptools import setup, find_packages
import os

version = '2.7dev'

setup(name='Products.ExtendedPathIndex',
      version=version,
      description="Zope catalog index for paths",
      long_description=open("README.txt").read() + "\n" + \
              open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        ],
      keywords='Zope catalog index',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            # 'transaction',
        ]
      ),
      install_requires=[
          'setuptools',
          # 'ZODB3',
          # 'Zope2',
      ],
      )
