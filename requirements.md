## Sharing Code Dependencies
Most programs written for Project Polaris will be written in Python due to the massive amount of libraries available.  
In order to share your code, you need to create either a "requirements.txt" or "\<environment-name\>.yml" file.
The following document includes instructions on how to create, share, and use these configuration files.

### Anaconda Instructions
#### Create a conda environment
```python
  conda create --name <environment-name> python=<version:2.7/3.5> #Create blank env
  conda create --name <env_name> --file <.txt file> #Install from txt file
```

#### To create a requirements.txt file:
```python
  conda list #Gives you list of packages used for the environment
  conda list -e > requirements.txt #Save all the info about packages to your folder
```
  
#### List Conda environments
```python
conda env list
```

#### To export environment file
```python
activate <environment-name>
conda env export > <environment-name>.yml
```

#### To import the environment
```python
conda env create -f <environment-name>.yml
```
  
#### Remove conda environments
```python
conda env remove -n <env_name>
```

#### Duplicate conda environments
```python
conda create --name <clone_name> --clone <env_name>
```

### Other Environments
If you are working in a PyCharm IDE, a _requirements.txt_ file can be created for you. Make sure to upload that to your repository. 
If you are using a different environment, IDE, or program to edit your code, you can generate the file yourself:
```python
  pip3 freeze > requirements.txt  # Python3
  pip freeze > requirements.txt   # Python2
```
The following command will install the packages according to the configuration file:
```python
  pip install -r requirements.txt
```
