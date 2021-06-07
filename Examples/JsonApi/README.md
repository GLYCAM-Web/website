# USAGE

## Overview
Initial requests to build a pdb file generate responses with two features:
* A download url for a pdb describing the requested structure, with default options.
* Information about options available for this structure.

Armed with a response to the orifinal request it is possible to:
* Poll for the status of the default pdb file.
* Submit a new request for up to 64 variations of this structures
* Each requested structure can then be polled for and downloaded as well.

## Submitting Requests To The API
### For secure connections
e.g., to a live website:

	`bash api-https.bash <json-input-file> <website-url>`

	For example:

		`bash api-https.bash sequence.json dev.glycam.org`
        or
        `bash api-https.bash sequence.json test.glycam.org`

### For insecure connections
e.g., a local dev environment:
Note that the ip address is optional. If not provided, the script assumes
a dev context and attempts to connect to a local instance of the site.

	`bash api-insecure.bash <json-input-file> <ip-address>`

	For example:

		`bash api-insecure.bash sequence.json 192.168.46.22`

#### Connecting to a Mac local dev environment:
    Really, the script is identical except it knows to look at Mac's convention
    for localhost:8000 if an ip address is not provided in the args.

        `bash mac-api-https.sh <json-input-file> <ip-address>`


### Sample input files

Sample input json:

* marco.json
* evaluate-sequence.json
* build-sequence.json

## Marco
marco.json is for testing the connection. If you receive a response that says
"polo", you are good.

## Evaluate
The Evaluate service returns information about options that are available for a
requested structure.

## Build3DStructure
The Build3DStructure service returns very similar information, along with
download urls for individual structures and/or additional files useful for
simulation.


### Sample output json:

* Example-OUTPUT.marco.json.Response.json
* Example-OUTPUT.evaluate-sequence.json.git-ignore-me_response.json
* Example-OUTPUT.build-sequence.json.git-ignore-me_response.json

## Using the output
Responses contain entities. Entities reflect the request (inputs), and provide
any responses (outputs):

### Inputs
```python
response['entity']['inputs']
```

### Outputs
```python
response['entity']['outputs']
```

### Evaluate service output
The evaluate response provides sequence evaluation, e.g. whether or not our
tools can build it (sequenceIsValid), sequence variants, buildOptions etc...

For a detailed example, see:
* Example-OUTPUT.evaluate-sequence.Response.json

### Build3DStructure service output
The Build3DStructure service can be used both with and without build options
defined. In the case where no options are provided in the request, responses
will provide a full evaluation, along with structureBuildInfo for accessing pdb
files for specific conformations.

#### Build without setting options
For example, the provided example request in build-sequence.json does not set
any options. The example response provided includes the same evaluation data
present in the evaluate request, but also provides a url for downloading the
default structure.

For a detailed example of a build request with no user options, see:
* build-sequence.json
* Example-OUTPUT.build-sequence.Response.json

#### Build with options
However, one can set many options, and request up to 64 variations of a structure.
This involves:
1. Submitting an original request to retrieve the possible options
for your sequence, (as demonstrated, evaluate, or build requests suffice for this)
2. Submitting a second request, with options,
3. Polling the Build_Status url for the status of your builds,
4. Downloading some or all via the downloadUrl provided in the response.

For a detailed example of a build request with user options specified, see:
* build-sequence-with-options.json
* Example-OUTPUT.build-sequence-with-options.Response.json

## Polling for the status of a specific build
Given a project ID and a conformer ID, we can check the status of a specific build.
Using the following url:
```
http://test.glycam.org/cb/build_status/<ProjectID>/<ConformerID>/
```
We can receive a json object like the following:
```
{
    "minExists" : True,
    "tip3pExists" : True,
    "tip5pExists" : False,
    "conformerID" : "1ogg",
    "status" : "2 of 3 complete"
}
```
The status field reflects the status of the overall work for a given conformer. These are the possible
statuses:
* queued
* minimizing
* 1 of 3 complete
* 2 of 3 complete
* All complete

Each file gives true or false to indicate whether it exists or not.

## Downloading Files
To retrieve your file(s), you can:

* Enter the downloadUrl into a browser window.
* Use wget or curl or some other command line tool.

Look in the file containing sample output from build-sequence-with-options.json.  Inside,
you will find a section like this:

`   "structureBuildInfo": {
    "incomingSequence": "DNeu5Aca2-6DGalpb1-4DGlcpNAcb1-2DManpa1-3[DGlcpNAcb1-4][DManpa1-3DManpa1-6]DManpb1-4DGlcpNAcb1-4DGlcpNAcb1-OH",
    "indexOrderedSequence": "DNeu5Aca2-6DGalpb1-4DGlcpNAcb1-2DManpa1-3[DGlcpNAcb1-4][DManpa1-3DManpa1-6]DManpb1-4DGlcpNAcb1-4DGlcpNAcb1-OH",
    "seqID": "d06e2853-bcac-5b86-9cc6-9644fa1abf3a",
    "individualBuildDetails": [{
        "date": "2021-06-03T15:26:40.212612",
        "status": "new",
        "payload": "",
        "incomingSequence": "",
        "indexOrderedSequence": "",
        "seqID": "",
        "conformerID": "6ht_ogg_8ogg",
        "conformerLabel": "6ht_ogg_8ogg",
        "sequenceConformation": ["6", "h", "t", "6", "o", "gg", "8", "o", "gg"],
        "isDefaultStructure": true,
        "structureDirectoryName": "6ht_ogg_8ogg",
        "subDirectory": "",
        "downloadUrl": "http://test.glycam.org/json/download/cb/b6076423-23e1-41e5-b494-62de85d817c5/6ht_ogg_8ogg",
        "simulationPhase": "gas_phase",
        "solvationShape": null,
        "addIons": "default",
        "energy": null,
        "forceField": "See Build Directory Files"
    },`

The downloadUrl above is used in the following example.


### Example:  using curl on the command line

To save a file with filename molecule.pdb, set by the website, use:

`curl -L -o molecule.pdb [URL]`

for example:

`curl -L -o molecule.pdb http://dev.glycam.org/json/download/cb/6076423-23e1-41e5-b494-62de85d817c5/6ht_ogg_8ogg`

Do be certain that there is not already a file with the same name in your directory.
