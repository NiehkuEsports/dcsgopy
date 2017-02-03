from setuptools import setup, find_packages

setup(
	name='dcsgopy',
	version='0.1',
	author=('Eskil Opdahl Nordland', 'Jan Ailo Nordsletta'),
	description='A cli tool and library to handle csgo docker containers',
	include_package_data=True,
	install_requires=[
		'appdirs==1.4.0',
		'backports.ssl-match-hostname==3.5.0.1',
		'docker==2.0.2',
		'docker-pycreds==0.2.1',
		'ipaddress==1.0.18',
		'packaging==16.8',
		'pyparsing==2.1.10',
		'requests==2.13.0',
		'six==1.10.0',
		'websocket-client==0.40.0'
	],
	entry_points={
		'console_scripts': ['dcsgo = cli:main']
	}
)
