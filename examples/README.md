The SDK contains a number of publicly available examples, which are intended to be used in the following ways:
* They are stand-alone, runnable example scripts, which use the SDK's built-in functionalities to perform simple tasks. They can be ran to see the functionality in action.
* They are brief, documented descriptions of common use-cases which may be similar to your own pratical requirements. The files can be opened and read through to see the exact steps taken and required for any of these processes.

## Running Examples
The examples are intended to be run from the directory which also holds the SDK's folder. The examples can then be run with a command of the following form:

```bash
python -m "tygronsdk.examples.basics.users_and_domains"
```

### Credentials
When an example is run for the first time, the shell may prompt for a username and password with which to create a credentials file. This file will be stored in the current directory and will be accessed for future runs of the examples. It is recommended to have a separate account in your domain with access rights set such that the account has access to the Editor features, but not to administrate other users within the domain.

**SECURITY WARNING: The credentials file will store the credentials in plain text (albeit base64--encoded), which is not a secure form. Be aware of the implications of storing the username and password in a plain-text file, do not place it in shared folders, and do not share it with other users unless explicitly intended.**

### Available examples
The following examples are available

#### Basics
These examples are excellent starting points for developers just starting out with the Tygron Platform, the SDK, or both.

##### Users, domain, and license information:
Demonstrates obtaining information about the current user, the domain the user belongs to, and the available allowances in the domain's license.

```bash
python -m "tygronsdk.examples.basics.users_and_domains"
```

##### Starting, accessing, and stopping a session:
Demonstrates obtaining information about a Project, starting it as a Session, reading information, and closing it.
```bash
python -m "tygronsdk.examples.basics.project_session"
```

#### Advanced

##### Running the built-in TemplateRunner implementation:
Demonstrates setting up the automated TemplateRunner to apply the "demo heat stress" Project on a different location in The Hague, and exporting calculation results to "./tygron_example_outputs".
*Note: As provided, running this example will create 1 additonal Project, which will count against your daily limit.*
```bash
python -m "tygronsdk.examples.automations.template_runner"
```

##### Running the built-in TemplateRunner Orchestrator:
Demonstrates using the TemplateOrchestrator to perform fully-automated calculations. This example will set up a workspace to manage the required files for individual runs, use the TemplateRunnerInputGenerator to create run files based on a single template file, and then use the automated TemplateRunnerOrchestrator to sequentially use the TemplateRunner to create all required Projects, run the calculations, and write the results to an output folder.
*Note: As provided, running this example will create 3 additonal Projects, which will count against your daily limit. It will pause if your daily usage has reached or exceeded 50% of what the license allows.*
```bash
python -m "tygronsdk.examples.automations.template_runner_orchestrator"
```

#### Triggers

##### Demonstrating principles of a Trigger
Demonstrates the principles of a Trigger without the additional functionality of the Trigger interface. This example will connect to a running session, perform a few basic operations, and generate a response which would be valid for a Trigger.
*Note: Running this example requires an active session, and a known API token. An API token can be added to the credentials file manually, with the key "api_token"*
```bash
python -m "tygronsdk.examples.basics_trigger_structure_human_building_counter"
```

##### Running a Trigger built on the Trigger interface
Demonstrates how to use the Trigger interface to implement and call a functional Trigger. The examples will take accept arguments indicating the Trigger to run, the host, the API token, and optionally and arguments the Trigger requires.

These examples work via the trigger_caller example, which takes arguments including host and API token as command-line arguments, to more closely simulate the kind of call which would be appropriate in a server-like environment where a Trigger would be functional.

A number of Trigger implementations exist which are also live and available for public use. These server as the best demonstrations of how Triggers can be structured in a live environment.

```bash
python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.implementations.triggers.trigger_generate_sewer_areas engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30"
python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.implementations.triggers.trigger_geotiff_from_geoshare engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30 {\"bbp-value\":\"tygron/testfiles/bbp-zero.tiff\"}"
python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.implementations.triggers.trigger_overlay_active_by_parent engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30"
```

In addition, a few examples of Triggers exist which have been created in the past, but are not used in live environments anymore. However, they still serve as practical examples in regards to structure and potential applications.

```bash
python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.examples.triggers.trigger_implementation_human_building_counter engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30"
python -m "tygronsdk.examples.triggers.trigger_caller tygronsdk.examples.triggers.trigger_implementation_geotiff_from_geoshare_via_stream engine.tygron.com 14654848IaBWfOYqGxd2BhSimG8d0S30 {\"bbp-value\":\"tygron/testfiles/bbp-zero.tiff\"}"
```