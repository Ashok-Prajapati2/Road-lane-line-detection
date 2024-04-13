from setuptools import setup, find_packages

setup(
    name='lane_detection',
    version='1.0',
    description='Lane detection project',
    author='Ashok Kumar',
    author_email='ap86963163@gmail.com.com',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'lane_detection=app.main:main',  
        ],
    },
)

