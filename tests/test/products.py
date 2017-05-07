from tools import req
# from tools import db
import json

rq = req.req()

def create_product():
    input_data = {
		"name": "BA Test Product 2",
		"type": "simple",
		"regular_price": "10.99",
		"description": "BA Test Product 2 - Description",
		"short_description": "BA Test Product 2 - Short description"
	}

    info = rq.post('products', input_data)
    print json.dumps(info[1], indent=4)

create_product()