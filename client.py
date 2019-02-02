import json

from pprint import pprint

client_file = open("client.json").read()

json_lo = json.loads(client_file)


#second client information
second_client = json_lo["clients"][1]
pprint(second_client)
print("\n")

#second client age information
second_clinet_age = second_client["age"]
print("second clinet age is " + str(second_clinet_age))


print("\n" + "Print original Json format!\n")

#original json file
json_dumps = json.dumps(json_lo)
pprint(json_dumps)
