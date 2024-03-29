from setuptools import find_packages,setup
with open('login_proj/readme.MD') as f:
    long_des=f.read()

setup(
    name='Dj_login_auth',
    version='0.0.1',
    description='A reusable django login auth application',
    package_dir= {'','login_proj'},
    packages= find_packages(where='login_proj'),
    long_description= long_des,
    long_description_content_type='text/markdown',
    url='',
    author='Oladeji Olaoluwa',
    author_email='oladejiolaoluwa46@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators', 
        'Programming Language :: Python :: 3.10',
        'license' :: OSI-Approved :: MIT,
        'operating system  :: os independent'
    ],
    install_requires=[],
    keywords='django reusable app',
    
)