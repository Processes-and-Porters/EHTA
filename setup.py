# -*- coding: utf-8 -*-
'''
可以简答介绍一下咱们这个EHTA
'''

from setuptools import setup 
 
classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Manufacturing',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: BSD',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Programming Language :: Python :: Implementation :: MicroPython',
    'Programming Language :: Python :: Implementation :: IronPython',
    'Programming Language :: Python :: Implementation :: Jython',
    'Topic :: Education',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
    'Topic :: Scientific/Engineering :: Chemistry',
    'Topic :: Scientific/Engineering :: Physics',
]

description = 'this is EHTA, a heat transfer calculation project'
keywords = ('heat transfer'
            )


setup(
  name = 'ehta',
  packages = ['ehta'],
  license='MIT',
  version = '0.1.0',
  description = description,
  author = 'EHTA team',
  platforms=["Windows", "Linux", "Mac OS", "Unix"],
  author_email = '1239151479@qq.com',
  url = 'https://github.com/steve-yyw/ehta',
  keywords = keywords,
  classifiers = classifiers,
)
