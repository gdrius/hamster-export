from distutils.core import setup

setup(
    name='hamster-export',
    version='0.1',
    url='http://github.com/gdrius/hamster-export/',
    license='MIT',
    author='Giedrius Slavinskas',
    author_email='giedrius@inovera.lt',
    description='A command line tool to export logged time from Hamster '
                'time-tracking application',
    scripts=['hamster-export'],
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Time tracking :: Communications',
    ],
)
