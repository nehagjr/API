# convert json to python
import json
python_d='{"name": "neha", "qualification": "bpl", "city.bpl": false, "active": null}'
print(json.loads(python_d))
print(type(json.loads(python_d))) #dict