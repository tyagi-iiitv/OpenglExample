from setuptools import setup, find_packages
import os

setup(
	name='OpenglExample',
	version='1.2',
	description='A simple example demonstrating how to render an obj file to visualize in 3-D using Pyopengl and Pygame.',
	long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),

	author='Anjul Kumar Tyagi',
	author_email='atyagi@codemyway.in',
	url='https://codemyway.in',
	download_url='https://github.com/tyagi-iiitv/PyopenglExample/archive/master.zip',
	
	keywords= (
		'pyopengl example',
		'blender with pyopengl',
		'pyopengl',
		'pygame',
		'pygame with pyopengl',
		'reading blender obj files'
	),

	packages=['pyopengl_example'],

	include_package_data=True,

	package_data={
		'data':
			['data/final.mtl',
			'data/final.obj'	
			],	
	},

	setup_requires = (
    	'setuptools',
	),

	install_requires=[
		'pygame >= 1.9.1release',
		'pyopengl >= 3.1.1a1',
		'numpy >= 1.8.2'
	],

	scripts=[
		'pyopengl_example/demo.py',
		'pyopengl_example/main.py',
		'pyopengl_example/load_room_obj.py'
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