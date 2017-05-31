from tools import req
from tools import db
import json

rq = req.req()
db = db.db()

def create_product():
	global prod_id
	global prod_name
	global prod_price

	x = "22"
	prod_name = "BA Test Product " + x
	prod_price = "30"
	prod_desc = "BA Test Product " + x + " - Description"
	prod_short_desc = "BA Test Product " + x + " - Short description"
	prod_sku = "batest-simple" + x

	input_data = {
		"name": prod_name,
		"type": "simple",
		"regular_price": prod_price,
		"description": prod_desc,
		"short_description": prod_short_desc,
		"sku": prod_sku,
		"manage_stock": "true",
		"stock_quantity": 1000
	}

	info = rq.post('products', input_data)

	response_code = info[0]
	response_body = info[1]

	assert response_code == 201, "Response code is not as expected. Expected: 201, Actual: {act}".format(act=response_code)

	rs_title = response_body["name"]
	rs_price = response_body["regular_price"]
	prod_id = response_body["id"]

	assert rs_title == prod_name, "The title in the response is not the same as the product created. Expect: {}, Actual: {}".format(prod_name, rs_title)
	assert rs_price == prod_price, "The price is not correct. Expected: {}, Actual: {}".format(prod_price, rs_price)

	# print out response
	# print json.dumps(info[1], indent=4)

	# print out id
	# print "ID: {}".format(prod_id)

def test_verify_product_created_in_db():
	sql = "SELECT wp_posts.ID, wp_posts.post_title, wp_posts.post_type, wp_postmeta.meta_key, wp_postmeta.meta_value FROM wp_posts INNER JOIN wp_postmeta ON wp_posts.ID=wp_postmeta.post_id WHERE wp_posts.ID={}".format(prod_id)
	qrs = db.select('wordpress', sql)

	# print qrs[1][4]

	db_title = qrs[0][1] 
	db_reg_price = qrs[1][4]

	assert db_title == prod_name, "The expected and actual product names do not match"
	assert db_reg_price == prod_price, "The expected and actual product prices do not match"

	print "Verified product created in DB - PASS"

create_product()
test_verify_product_created_in_db()