#!/usr/bin/env python

#
# (C) Copyright IBM Corporation 2013
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the Eclipse Public License.
#
import os
from distutils.core import setup, Extension

# http://sourceforge.net/mailarchive/message.php?msg_id=28474701
# hack distutils so that extensions are built before python modules;
# this is necessary for SWIG-generated .py files
from distutils.command.build import build
build.sub_commands = [('build_ext', build.has_ext_modules),
                     ('build_py', build.has_pure_modules),
                     ('build_clib', build.has_c_libraries),
                     ('build_scripts', build.has_scripts)]

setup(name='platform-python-lsf-api',
      version='1.0.1',
      description='Python binding for Platform LSF APIs',
      license='LGPL',
      keywords='LSF,Grid,Cluster,HPC',
      url='http://www.platform.com',
      ext_package='pythonlsf',
      ext_modules=[Extension('_lsf', ['pythonlsf/lsf.i'],
                               include_dirs=['/usr/include/python2.4'],
                               library_dirs=[os.environ['LSF_LIBDIR']],
                               swig_opts=['-I' + os.environ['LSF_LIBDIR'] + '/../../include/lsf/'],
                               extra_compile_args=['-m64', '-I' + os.environ['LSF_LIBDIR'] + '/../../include/lsf/'],
                               extra_link_args=['-m64'],
                               libraries=['c', 'nsl', 'lsf', 'bat',
                                            'fairshareadjust', 'lsbstream'])],
      py_modules=['pythonlsf.lsf'],
      classifiers=["Development Status :: 2 - Pre-Alpha",
                     "License :: OSI Approved :: Eclipse Public License",
                     "Operating System :: OS Independent",
                     "Programming Language :: Python",
                     "Topic :: Internet",
                     "Topic :: Scientific/Engineering",
                     "Topic :: Software Development",
                     "Topic :: System :: Distributed Computing",
                     "Topic :: Utilities",
                     ],
     )

