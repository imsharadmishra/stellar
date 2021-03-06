
### Create a Python 3.8 virtual environment with the following command:
```python3.8 -m venv dev```

### Replace my_env with any name you like. Activate your virtual environment like this:
```source dev/bin/activate```

### In your activated virtual environment, install the packages in requirements_dev.txt with the following command:
```pip install -r requirement_dev.txt```

### Then run the following command to create your package files:
```python setup.py sdist bdist_wheel```

### Use Twine to securely publish your package to TestPyPI. Enter the following command 
```twine upload --repository-url https://test.pypi.org/legacy/ dist/*```

### You can tell pip to download packages from TestPyPI instead of PyPI by specifying the — index-url flag
```pip install -i https://test.pypi.org/simple/ stellar```


### Docker image with novus-hadoop configuration and python 3.8
```docker run --rm -ti sharadmishra/hadoop-2.7.3-centos-python38:1e  /bin/bash```

### Mount current project directory into docker
```docker run --rm -ti -v $(pwd):/stellar sharadmishra/hadoop-2.7.3-centos-python38:1e  /bin/bash```

### Fixes
```export CLASSPATH="$HADOOP_HOME/bin/hdfs classpath --glob"```

