# convert python to json
import json
python_d={
    'name':"neha",
    'qualification':'bpl',
    'city.bpl':False,
    'active':None
}
print(json.dumps(python_d))
print(type(json.dumps(python_d))) #str ---string