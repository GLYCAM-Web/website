USAGE

For secure connections - e.g., to a live website:

	api-https.bash <website-url>  <json-input-file>

	For exmaple:

		api-https.bash  dev.glycam.org sequence.json

For insecure connections - e.g., a local dev environment:

	api-insecure.bash <ip-address>  <json-input-file>

	For exmaple:

		api-insecure.bash 192.168.46.22 sequence.json

Sample input json:

* build-sequence.json
* marco.json
* sequence.json

Sample output json:

* Example-OUTPUT.build-sequence.json.Response.json
* Example-OUTPUT.marco.json.Response.json
* Example-OUTPUT.sequence.json.Response.json
