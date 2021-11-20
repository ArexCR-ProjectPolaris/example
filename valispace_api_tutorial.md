## Getting Started
This is a tutorial on how to pull valis from Valispace programmatically. This has numerous benefits; whenver one vali changes values, 
the simulation code does not need to be manually edited to reflect the updated values: it need only be run again.

## Keyring
It is very unsafe to upload code that has unredacted login information on it. However, to access Valispace, you need to provide your login information within the API function call.
To work around this, the use of the keyring library is required.

### Initial Setup
Make sure ```keyring``` is installed in your environment.

Then, run the below code in your Python environment:
```python
import keyring
keyring.set_password("valispace", "your_username", "your_password")
```
This stores your password in your system and allows you to retrieve it as a function call. This way, the plain text of your password is not visible.
Now you are ready to make calls to the Valispace API!

## Initializing the Valispace API

Run the below code to initialize the Valispace API object. Notice the use of the keyring library to fetch the password that corresponds to your username.
When uploading code, leave your username blank so that others can fill in their information.

```python
import valispace as v
import keyring

username = "your_username"

valispace_API = v.API(url = 'https://polarisproject.valispace.com', username=username,password=keyring.get_password("valispace", "your_username"))
```
```valispace_API``` is now initialized! 

## Using Valispace
There are many things that you can do with Valispace. Check out [https://github.com/valispace/ValispacePythonAPI](https://github.com/valispace/ValispacePythonAPI) to get documentation on how to pull valis and use other Valispace functionality.

Here are a few examples:

### GET

A dict of Valis:

```python
valis = valispace_API.get_vali_list()
```

**All Vali** ids and names:

```python
all_vali_names = valispace_API.get_vali_names()
```

A **Vali** with all properties:
List of **Valis** with the specified arguments:

Argument | Example
------------- | -------------
workspace_id | `valispace_API.get_vali_list(workspace_id=1)`
workspace_name | `valispace_API.get_vali_list(workspace_name='Default Workspace')`
project_id | `valispace_API.get_vali_list(project_id=1)`
project_name | `valispace_API.get_vali_list(project_name='Saturn_V')`
parent_id | `valispace_API.get_vali_list(parent_id=1)`
parent_name | `valispace_API.get_vali_list(parent_name='Fan')`
tag_id | `valispace_API.get_vali_list(tag_id=10)`
tag_name | `valispace_API.get_vali_list(tag_id='example_tag')`
vali_marked_as_impacted | `valispace_API.get_vali_list(vali_marked_as_impacted='10')`

List of **Components** with the specified arguments:

Argument | Example
------------- | -------------
workspace_id | `valispace_API.get_component_list(workspace_id=1)`
workspace_name | `valispace_API.get_component_list(workspace_name='Default Workspace')`
project_id | `valispace_API.get_component_list(project_id=1)`
project_name | `valispace_API.get_component_list(project_name='Fan')`
parent_id | `valispace_API.get_component_list(parent_id=1)`
parent_name | `valispace_API.get_component_list(parent_name='Fan')`
tag_id | `valispace_API.get_component_list(tag_id=10)`
tag_name | `valispace_API.get_component_list(tag_name='example_tag')`

There are a lot more things you can do with Valispace that is listed in the documentation website.



