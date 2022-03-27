# Teradata converter
This script converts teradata sql to [bigquery].
The following functionality are included:
* convert most datatypes
* convert comparison operator
* convert median and sel



## Usage
* ```pip install -r requirements.txt```
* ```python src/main.py --script_path 'path/to/the/script.sql'```
* Converted sql script will be in the same directory as the original script with the name "converted.sql"


## Development
* ```pip install -r requirements_dev.txt```
* ```pre-commit install```
* ```pytest tests/```
