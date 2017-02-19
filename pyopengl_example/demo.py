"""
This function calls the main script along with the obj file to open a new pygame window.
For the main code, see the test.py file.

"""

import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def demo():
	path_to_main = os.path.join(BASE_DIR, 'pyopengl_example', 'main.py')
	path_to_final_obj = os.path.join(BASE_DIR, 'pyopengl_example', 'data', 'final.obj')
	command = "python"+" "+path_to_main+" "+path_to_final_obj
	os.system(command)
