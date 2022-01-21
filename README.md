# Python-SDK

Software Development Kit in Python for interacting with the Tygron Platform.

Add as a module to a python project, ideally in a folder named "tygronsdk". It is then possible to import the sdk with:
	from tygronsdk import sdk as tygron

And use the sdk aas follows:
	sdk = tygron.sdk( {
			'platform' : 'engine',
			'username' : str(credentials.tygron_username),
			'password' : str(credentials.tygron_password)
	
		} );

Examples can be run from the enclosing project's root with:
	python3  -m "tygronsdk.examples.tygron_read_project"
	python3  -m "tygronsdk.examples.tygron_api_trigger"