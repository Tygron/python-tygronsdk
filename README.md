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


Running examples:
The SDK contains a number of exmaples a publicly available practicle implementations. Examples can be run from the enclosing project's root 

Basic Project interaction
Location a Project, starting it as a Session, reading information, and closing it:
	python -m "tygronsdk.examples.basics.project_session"

Running a trigger
Provided a running session's server and api token, call an implementation of a trigger and print its response:
	python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.implementations.triggers.trigger_generate_sewer_areas engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30"
	python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.implementations.triggers.trigger_geotiff_from_geoshare engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30 {\"bbp-value\":\"tygron/testfiles/bbp-zero.tiff\"}"
	python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.implementations.triggers.trigger_overlay_active_by_parent engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30"