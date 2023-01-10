# Python-SDK

Software Development Kit in Python for interacting with the Tygron Platform.

## Using the sdk:

Add as a module to a python project, ideally in a folder named "tygronsdk". It is then possible to import the sdk with:

```python
# Import Tygron SDK
from tygronsdk import sdk as tygron
from tygronsdk import items
```

And use the sdk as follows:

```python
# Starting with the Tygron SDK
sdk = tygron.sdk( {
        'platform' : 'engine',
        'computer_name' : 'PythonSDK',
    } );

username = '' # Your Tygron Platform username
password = '' # Your Tygron Platform password

sdk.base.authenticate( {'username' : username, 'password' : password} )

# Start and access session
sdk.base.projects.get_startable_projects()
session_id = sdk.base.sessions.start_project_session( 'demo_heat_stress' )
api_token = sdk.base.sessions.join_project_session( session_id )['apiToken']

# Interact with session
sdk.session.authenticate( {'api_token': api_token} )
stakeholders = sdk.session.items.load(items.Stakeholder)
print ('There are '+str(stakeholders.count())+' Stakeholders: ' + str([item.name for item in stakeholders]) )

# Terminate session
sdk.base.sessions.kill_project_session( session_id )
```

## SDK Structure
#### SDK Object
The SDK Object is the main access to all SDK functionality.

#### Environments
Functionality within the SDK is split up into a number of environments:

```python
sdk.base # For interacting with the base API. Use this for managing users, domains, and starting and stopping sessions
sdk.session # For interacting with the session API. Use this for managing data in a session, such as Overlays, Stakeholders, world locations, project area generation, etc.
sdk.share # For accessing data via the share API. Use this to access files which are uploaded to the Geo Share or the Public Share.
```

Each environment in turn has its own authentication requirements, its own events, and its own data structures.

##### Interactions
Each environment has pre-defined interactions intended for the main program flow. These interactions leverage lower-level components and wrap their functionality into use-case actions. For example:

```python    
# Base interactions
sdk.base.projects # Located in the base API, contains all predefined interactions for working with Projects (creation, deletion, permissions, data retrieval, etc)
sdk.base.projects.get_startable_projects()
sdk.base.projects.get_project( 'demo_heat_stress'  )

sdk.base.sessions # Located in the base API, contains all predefined interactions for working with Sessions (starting, stopping, joining, keep alive, etc)
sdk.base.sessions.start_project_session( 'demo_heat_stress' )
sdk.base.sessions.join_project_session( 12345678 )

# Session interactions
sdk.session.calculation # Located in the session API, contains all predefined interactions for working with calculations in a session (recalculating, waiting for responsiveness, etc)
sdk.session.calculation.recalculate()
```

##### Events

Events can be separately imported for easy access:
```python
#Import Tygron SDK events
from tygronsdk import events
```

Not all Events have been specifically defined yet. However, events can also be manually defined and used.

##### Items

Items can be separately imported for easy access:

```python
# Import Tygron SDK items
from tygronsdk import items

# Accessible items
items.Item # Base class for all Items
items.ItemMap # Specialized collection to store and iterrate through items
items.Stakeholder # Item class specifically for Stakeholders
items.Overlay # Item class specifically for Overlays
# etc
```

Not all Items have a specialized Item class as of yet. However, all Items served by the Tygron Platform can at least be instantiated as the Item base class, and stored in the ItemMap.

##### Connector
    
##### Data

##### Notes
It is possible to import and access the contents of an environment directly, for example the interactions class or the connector. However, it is recommended to use the instances provided via the environments in the sdk object, as these also wrap the objects to take care of some overhead which would otherwise be the responsibility of the application using the provided components. 

## Running examples:
The SDK contains a number of exmaples a publicly available practicle implementations. Examples can be run from the directory enclosing the tygronsdk.

Depending on the examples, credentials are required to authenticate against the Tygron Platform. Credentials for the examples can be provided by placing a credentials.py file in the directory from where the the command is run, with content structured as follows:

```python
# credentials.py
tygron_username = 'example@tygron.com' # Your username
tygron_password = 'SuperSecretPassword123' # Your password
tygron_api_token = '12345678abcdabcdabcdabcdabcdabcd' # Api token of your session (only used if applicable)
```

#### Basic Project interaction
Locating a Project, starting it as a Session, reading information, and closing it:

```bash
python -m "tygronsdk.examples.basics.project_session"
```

#### Running a trigger
Provided a running session's server and api token, call an implementation of a trigger and print its response. Any of the following can be tried:
```bash
python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.implementations.triggers.trigger_generate_sewer_areas engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30"
python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.implementations.triggers.trigger_geotiff_from_geoshare engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30 {\"bbp-value\":\"tygron/testfiles/bbp-zero.tiff\"}"
python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.implementations.triggers.trigger_overlay_active_by_parent engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30"
```