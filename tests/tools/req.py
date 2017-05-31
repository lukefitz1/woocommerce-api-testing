from woocommerce import API

class req():
	def __init__(self):
		admin_consumer_key = 'ck_edce5b4a854b359de4d156e08870cbb6fc57b4ea'
		admin_consumer_secret = 'cs_fa489914fcd03ba4f806b6ff7c925f4dfcd26876'

		self.wcapi = API(
		    url="http://wp.dev/",
		    consumer_key=admin_consumer_key,
		    consumer_secret=admin_consumer_secret,
		    wp_api=True,
		    version="wc/v2")

	def test_api(self):
		print self.wcapi.get("products/8").json()

	def post(self, endpoint, data):
		result = self.wcapi.post(endpoint, data)

		res_code = result.status_code
		res_body = result.json()
		res_url = result.url

		return [res_code, res_body, res_url]

	def get(self, endpoint):
		result = self.wcapi.get(endpoint)

		res_code = result.status_code
		res_body = result.json()
		res_url = result.url

		return [res_code, res_body, res_url]
