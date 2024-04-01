from setuptools import find_packages,setup
import os
# with open('readme.MD') as f:
#     long_des=f.read()

base_dir = os.path.abspath(os.path.dirname('login_proj'))
# base_dir=os.listdir('')

# Read the contents of the readme file
with open(os.path.join(base_dir, 'readme.MD'), encoding='utf-8') as f:
    long_des = f.read()

setup(
    name='Dj_login_auth',
    version='0.0.1',
    description='A reusable django login auth application',
    packages= find_packages(where='login_proj'),
    long_description= long_des,
    long_description_content_type='text/markdown',
    url='https://github.com/Boluex/Custom-django-package-using-wheels-django.git',
    author='Oladeji Olaoluwa',
    author_email='oladejiolaoluwa46@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators', 
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    install_requires=[],
    keywords='django reusable app',
    
)