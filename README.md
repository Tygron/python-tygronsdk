# Python-SDK

Software Development Kit in Python for interacting with the Tygron Platform.

## Using the sdk:

Add as a module to a python project, ideally in a folder named "tygronsdk". It is then possible to import the sdk with:

```python
# Import Tygron SDK
import tygronsdk
from tygronsdk import sdk as tygron
from tygronsdk import items

# Load credentials.txt for credentials, and data.txt for other connection settings
data = tygronsdk.init.init_data()

# Optionally overwrite or add additional data
data.update( {
        'platform' : 'engine',
        'computer_name' : 'PythonSDK',
} )

# Starting the Tygron SDK with the initialized data
sdk = tygron.sdk( data );

# Authenticate using the credentials data in the data store
sdk.authenticate( )

# Start and access session
sdk.base.projects.get_startable_projects()
session_id = sdk.base.sessions.start_project_session( 'demo_heat_stress' )
join_data = sdk.base.sessions.join_project_session( session_id )

# Interact with session
sdk.authenticate( join_data )
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

A generic connector is included to facilitate communication with external services through HTTP calls. Each environment also features its own subclassed implementation, to facilitate lower-level status checks and more specialized requests.
    
##### Data

Each environment features a collection of miscellaneous data objects which wrap certain responses from the Tygron Platform API in a more managable form, or to combine multiple such data objects to allow easier access to inferred information.

Examples of these are the following objects from the base environment:
* base.data.objects.UserData and base.data.objects.DomainData 1-on-1 wrap the data received from specific endpoints for "my user" and "my domain" respectively.
* base.data.objects.UsageData wraps a list of values about the usages within a domain into a more manageable object.
* base.data.objects.LicenseData is a fully synthetic object which can hold data regarding licenses.
* base.data.objects.AllowanceData is composed of LicenseData and UsageData to provide insight into how much room there still is within a license.


##### Notes
It is possible to import and access the contents of an environment directly, for example the interactions class or the connector. However, it is recommended to use the instances provided via the environments in the sdk object, as these also wrap the objects to take care of some overhead which would otherwise be the responsibility of the application using the provided components. 

## Examples:
The SDK contains a number of exmaples a publicly available practicle implementations. Examples can be run from the directory enclosing the tygronsdk.

Documentation regarding the specific examples is included in the examples directory.

[Examples](examples)