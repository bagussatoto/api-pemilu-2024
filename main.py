from lib.requestHelper import requestHelper
import json

request = requestHelper()
data = request.get_count()
print(json.dumps(data, indent=4))
