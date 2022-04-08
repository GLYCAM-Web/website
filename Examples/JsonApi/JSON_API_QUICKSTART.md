# USAGE

## Quick Start

##### Verify glycam.org is up:

```bash
$ bash api-https.bash marco.json glycam.org
```

##### Evaluate a sequence; determine if it can be built and what options are possible:

```bash
$ bash api-https.bash evaluate-sequence.json glycam.org
```

##### Submit the request to the API:

```bash
$ bash api-https.bash build-sequence.json glycam.org
```

##### Poll for status via cURL:

Find the pUUID and conformerID from the build submission response; curl for build status:
```bash
$ curl https://glycam.org/json/build_status/<pUUID>/<conformerID>/ --output status.json
```

For example:
```bash
$ curl https://glycam.org/json/build_status/323c6eda-eb49-4d15-a77b-5434fd61aec9/1ogg/ --output status.json
```

##### Download via cURL:

Find the pUUID and conformerID from the build submission response; curl for build status:
```bash
$ curl https://glycam.org/json/download/sequence/<app>/<pUUID>/<conformerID> --output protein.pdb
```

For example:
```bash
$ curl https://glycam.org/json/download/sequence/cb/323c6eda-eb49-4d15-a77b-5434fd61aec9/1ogg/ --output protein.pdb
```
