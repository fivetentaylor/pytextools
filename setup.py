from setuptools import setup

def readme():
    with open('README.md') as f:
	        return f.read()

setup(name='pytextools',
	version='0.1',
	description='Family of command line text processing tools that builds upon the gnu core utils',
	url='https://github.com/fivetentaylor/pytextools',
	long_description=readme(),
	classifiers=[
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Topic :: Text Processing :: Linguistic',
	],
	scripts=[
		'pytextools/bin/describe',
		'pytextools/bin/jscut',
		'pytextools/bin/jslist2csv',
		'pytextools/bin/jsprint',
		'pytextools/bin/rm_quotes',
		'pytextools/bin/scatter',
		'pytextools/bin/tdate',
		'pytextools/bin/tuniq',
		'pytextools/bin/widen',
	],
	author='Taylor Sather',
	author_email='fivetentaylor@gmail.com',
	license='MIT',
	packages=['pytextools'],
	install_requires=[
		'pandas','ipdb',
		'matplotlib','numpy',
	],
	dependency_links=[
		'https://github.com/fivetentaylor/pytextools.git'
	],
	zip_safe=False)

