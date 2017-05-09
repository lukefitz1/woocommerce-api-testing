from tools import req
from tools import db
import json

rq = req.req()
db = db.db()

x = "14"
prod_name = "BA Test Product " + x
prod_price = "30"
prod_desc = "BA Test Product " + x + " - Description"
prod_short_desc = "BA Test Product " + x + " - Short description"
prod_sku = "batest-simple" + x
prod_id = ''

def create_product():
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

    assert response_code == 201, "Response code is not as expected. Expected: 201, Actual: {act}".format(act=status_code)

    rs_title = response_body["name"]
    rs_price = response_body["regular_price"]
    prod_id = response_body["id"]

    assert rs_title == prod_name, "The title in the response is not the same as the product created"
    assert rs_price == prod_price, "The price is correct"

    # print out response
    # print json.dumps(info[1], indent=4)

    # print out id
    print "ID: {}".format(prod_id)

def test_verify_product_created_in_db():
	# get info from db
	# sql = '''SELECT wp_posts.ID, wp_posts.post_title, wp_posts.post_type, wp_postmeta.meta_key, wp_postmeta.meta_value 
	# 			FROM wp_posts 
	# 			INNER JOIN wp_postmeta 
	# 			ON wp_posts.ID=wp_postmeta.post_id 
	# 			WHERE wp_posts.ID={}
	# '''.format(prod_id)

	# sql = ' '.join((
	# 		"SELECT wp_posts.ID, wp_posts.post_title, wp_posts.post_type, wp_postmeta.meta_key, wp_postmeta.meta_value",
	# 		"FROM wp_posts",
	# 		"INNER JOIN wp_postmeta",
	# 		"ON wp_posts.ID=wp_postmeta.post_id",
	# 		"WHERE wp_posts.ID={}",
	# 	)).format(prod_id)

	sql = "SELECT wp_posts.ID, wp_posts.post_title, wp_posts.post_type, wp_postmeta.meta_key, wp_postmeta.meta_value FROM wp_posts INNER JOIN wp_postmeta ON wp_posts.ID=wp_postmeta.post_id WHERE wp_posts.ID=21"
	qrs = db.select('wordpress', sql)

	print qrs

create_product()
test_verify_product_created_in_db()