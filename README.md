# Python-SDK

Software Development Kit in Python for interacting with the Tygron Platform.

Add as a module to a python project, ideally in a folder named "tygronsdk". It is then possible to import the sdk with:

	from tygronsdk import sdk as tygron



And use the sdk as follows:

	sdk = tygron.sdk( {
			'platform' : 'engine',
			'username' : str(credentials.tygron_username),
			'password' : str(credentials.tygron_password)
	
		} );



Examples can be run from the enclosing project's root with:

	python3  -m "tygronsdk.examples.tygron_read_project"



Running the trigger examples is done with the tygron_api_trigger script, and providing it with the desired module and required parameters for running a trigger:

	python3  -m "tygronsdk.examples.tygron_api_trigger tygronsdk.examples.trigger_human_building_counter engine.tygron.com 25963097QVZSsMd4nchY4EZYPxKGSdIj"
	python3  -m "tygronsdk.examples.tygron_api_trigger tygronsdk.examples.trigger_geotiff_from_geoshare engine.tygron.com 25963097QVZSsMd4nchY4EZYPxKGSdIj"