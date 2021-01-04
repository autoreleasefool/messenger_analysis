from setuptools import setup

with open('VERSION', 'r') as f:
    version = f.read()

setup(
    name='messenger_analysis'
    description='Analyze your Facebook Messenger conversations, for interesting facts',
    version=version,
    author='Joseph Roque',
    url='https://github.com/josephroquedev/messenger-analysis',
    license='MIT',
    packages=['messenger_analysis']
    entry_points={
        'console_scripts': [
            'messenger_analysis = messenger_analysis.__main__:main'
        ]
    }
)
th