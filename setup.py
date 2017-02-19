from setuptools import setup
import os

setup(
	name='PyopenglExample',
	version='0.0.1',
	description='A simple example demonstrating how to render an obj file to visualize in 3-D using Pyopengl and Pygame.',
	long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
	author='Anjul Kumar Tyagi',
	author_email='atyagi@codemyway.in',
	url='https://codemyway.in',
	download_url=''
	packages=['app'],
	install_requires=[
		'pygame >= 1.9.1release',
		'pyopengl >= 3.1.1a1'
	],
	scripts=[
		'app/demo.py',
		'app/demo.py',
		'app/load_room_obj.py'
	],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: Education',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2 :: Only'
	]
)