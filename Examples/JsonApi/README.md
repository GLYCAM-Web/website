# USAGE

## Overview
The JSON API provides an interface to the services made available by GEMS and GMML.

We make html requests to the API's urls, often providing json-formatted input. GEMS
then interprets requests, determines which service(s) are appropriate to provide,
and the api returns json-formatted responses.

A typical pattern might involve:
1. Evaluate some sequence to determine if it can be built, and if any options are
    available for that sequence.
2. Request the build status of either the default build, or one of the builds listed
    in the evaluate response.
3. When the desired file exists, request the file as an attachment in a response.

An in-depth walkthrough of one way this might happen is provided in the
[Appendix: Walkthrough](#walkthrough)


Armed with a response to the original request it is possible to:
* Poll for the status of the default PDB file.
* Submit a new request for up to 64 variations of this structures
* Each requested structure can then be polled for and downloaded as well.

## Submitting Requests To The API

	`bash api-https.bash <json-input-file> <website-url>`

### Example:

	`bash api-https.bash build-sequence.json dev.glycam.org`

### Sample input files

* [marco.json](marco.json)
* [evaluate-sequence.json](evaluate-sequence.json)
* [build-sequence.json](build-sequence.json)

# Sequence Services
## Marco
marco.json is for testing the connection. If you receive a response that says
"polo", you are good.

## Evaluate
The Evaluate service returns information about options that are available for a
requested structure. If you just want to know if we can build a sequence, this might
be the service you prefer.

## Build3DStructure
The Build3DStructure service returns very similar information. These requests can
optionally define build options, if desired. If the default structure is desirable,
build options can be ignored completely.

Requests to build a PDB file generate responses with two features:

* A download url for a PDB describing the requested structure, with default options.
* Information about options available for this structure.
* Values needed to poll the status of any files you plan to download.

### Sample output json:

* [Example-OUTPUT.marco.json.Response.json](Example-OUTPUT.marco.json.Response.json)
* [Example-OUTPUT.evaluate-sequence.json.git-ignore-me_response.json](Example-OUTPUT.evaluate-sequence.json.git-ignore-me_response.json)
* [Example-OUTPUT.build-sequence.json.git-ignore-me_response.json](Example-OUTPUT.build-sequence.json.git-ignore-me_response.json)

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
* [Example-OUTPUT.evaluate-sequence.Response.json](Example-OUTPUT.evaluate-sequence.Response.json)

### Build3DStructure service output
If you need to download a pdb file for a sequence, you will probably want to start
with Build3DStructure. The Build3DStructure service can be used both with and
without build options defined. In the case where no options are provided in the
request, responses will provide:
* a full evaluation,
* structureBuildInfo for accessing PDB files for specific conformations.

#### Build without setting options
The provided example request in build-sequence.json does not set any options.
The example response provided includes the same evaluation data present in the
evaluate request, but also provides downloadUrlPath values for downloading the
structures available for that sequence.

For a detailed example of a build request with no user options, see:
* [build-sequence.json](build-sequence.json)
* [Example-OUTPUT.build-sequence.Response.json](Example-OUTPUT.build-sequence.Response.json)

#### Build with options
One can set many options, and request up to 64 variations of a structure.
This involves:
1. Submitting an original request to retrieve the possible options
for your sequence, (as demonstrated, evaluate, or build requests suffice for this)
2. Submitting a second request, with options set, following the patterns in the
build response,
3. Polling the Build_Status url for the status of your builds,
4. Downloading some or all via the downloadUrl provided in the response.

For a detailed example of a build request with user options specified, see:
* build-sequence-with-options.json
* Example-OUTPUT.build-sequence-with-options.Response.json

## Polling for the status of a specific build
Given a project ID and a conformer ID, we can check the status of a specific build.
Using the following url:
```
http://dev.glycam.org/cb/build_status/<ProjectID>/<ConformerID>/
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
    "incomingSequence": "DManpa1-6DManpa1-OH",
    "indexOrderedSequence": "DManpa1-6DManpa1-OH",
    "seqID": "8f89c814-df0f-5867-a9d4-fc393bfea61b",
    "individualBuildDetails": [{
        "date": "2021-06-07T10:09:05.908645",
        "status": "new",
        "payload": "",
        "pUUID": "3c368bf2-ad73-43f3-a18d-d7d2dc11cf28",
        "entity_id": "sequence",
        "service_id": "cb",
        "incomingSequence": "",
        "indexOrderedSequence": "DManpa1-6DManpa1-OH",
        "seqID": "",
        "conformerID": "1ogg",
        "conformerLabel": "1ogg",
        "sequenceConformation": ["1", "o", "gg"],
        "isDefaultStructure": true,
        "isNewBuild": false,
        "structureDirectoryName": "1ogg",
        "filesystem_path": "/website/userdata/",
        "host_url_base_path": "https://test.glycam.org",
        "conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Requested_Builds/1ogg",
        "absolute_conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Existing_Builds/1ogg",
        "downloadUrlPath": "https://test.glycam.org/json/download/sequence/cb/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/1ogg/",
        "forceField": "See Build Directory Files"
    }, `

The downloadUrl above is used in the following example.


### Curl Example
#### Using curl on the command line

To save a file with filename molecule.pdb, set by the website, use:

`curl -L -o molecule.pdb [URL]`

for example:

`curl -L -o molecule.pdb http://dev.glycam.org/json/download/cb/6076423-23e1-41e5-b494-62de85d817c5/6ht_ogg_8ogg`

Do be certain that there is not already a file with the same name in your directory.


#Appendix

## Walkthrough
# Default Structure
Key concept: Default structure is a value we use. If you are unconcerned with which
conformation your file represents, ANY conformerID found in a response is good.


1. Create a folder to work in somewhere. I will use:
`
 test/
`

2. Create a new file. You can name it what you like. It will be the command we run to
start our process. I will call mine

`
testTheAPI.sh.
`

3. Copy the contents of this [script](api-https.sh) into your test script.

If you run the script with no arguments, you will get a helpful usage message.

The script you just created accepts an argument for JSON input, and a host. We have
sample json files that demonstrate the format needed for for requests. Feel free
to grab these and edit the input as needed.

This walkthrough will demonstrate using [build-sequence.json](build-sequence.json),
which requests DManpa1-6DManpa1-OH. You can simply replace the sequence and this
file is valid to request the default structure for any valid sequence.

4. In the same folder as your test script, create a new file. Mine is named
`
build-sequence.json.
`

5. Copy the contents of this [build-sequence.json](build-sequence.json) into your new
file.

Run the following command to submit your request. Because the script and its
input are in the same path, I can leave paths out. If youneed to add paths, and
if you use different file names, remember to edit the following to reflect your
needs:

```bash
$ bash testTheApi.sh build-sequence.json dev.glycam.org
```

If all goes well, you get some chatty logs on your console, followed by a printout
of your response object. This is also written to file, by the test script we just
called in the command above. You can edit that if you want different filenames or
output locations.

There is a lot in the output. These responses serve more purposes than ours, but
that means we are only interested in two pieces of data:

* pUUID - A key to find the project that your request created. Needed for
    polling file status.
* download_url_path for the project -  A URL we can call to download the default structure.

Both of these live in the json object's project. For example:
```python
myProject = responseDict['project']['pUUID']
myDownloadUrl = responseDict['project']['download_url_path']
```

6. Poll for the status of the default structure's project files.
Currently, a conformer ID is required to check build statuses. We find the conformer ID
of the default structure in the response to our Build3DStructure request.

Note: There is nothing special about the default structure. If you don't care
which structure, grabbing the first conformerID you find is appropriate.

## Conformer ID Lookup Example:
Regardless of whether you are looking for the default structure, or have less
specific needs, examining the output of a build response shows structureBuildInfo
which contains a list of individual build details. Here, the reasonable values for
conformerIDs can be found, as well as a boolean to determine the default structure.


```"structureBuildInfo": {
    "incomingSequence": "DManpa1-6DManpa1-OH",
    "indexOrderedSequence": "DManpa1-6DManpa1-OH",
    "seqID": "8f89c814-df0f-5867-a9d4-fc393bfea61b",
    "individualBuildDetails": [{
        "date": "2021-06-07T10:09:05.908645",
        "status": "new",
        "payload": "",
        "pUUID": "3c368bf2-ad73-43f3-a18d-d7d2dc11cf28",
        "entity_id": "sequence",
        "service_id": "cb",
        "incomingSequence": "",
        "indexOrderedSequence": "DManpa1-6DManpa1-OH",
        "seqID": "",
        "conformerID": "1ogg",
        "conformerLabel": "1ogg",
        "sequenceConformation": ["1", "o", "gg"],
        "isDefaultStructure": true,
        "isNewBuild": false,
        "structureDirectoryName": "1ogg",
        "filesystem_path": "/website/userdata/",
        "host_url_base_path": "https://dev.glycam.org",
        "conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Requested_Builds/1ogg",
        "absolute_conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Existing_Builds/1ogg",
        "downloadUrlPath": "https://dev.glycam.org/json/download/sequence/cb/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/1ogg/",
        "forceField": "See Build Directory Files"
    },
```
The above snippet shows how responses offer conformerIDs, downloadUrlPath, pUUID

We provide a sample script that you can use to poll for the status of the file you requested.
7. Create a new file, mine is named,
`
checkStatus.sh
`
8. Copy the content of [checkStatus.sh](checkStatus.sh) into your new script.

9. In the response to your original request, find the pUUID for your project, and
grab an appropriate conformerID.

10. Run the script with your selected args. The script will echo out the status
response, and also writes it out to file. Feel free to customize.


```bash
$ bash checkStatus.sh <pUUID> <conformerID>
```
My example would be:

```bash
$ bash checkStatus.sh a997768f-6097-4aa6-9789-c756252358df 1ogg
```

11. Examine the response to find the status.
This status indicates all is complete. If you are wanting verification that it has
been minimized, minExists will return true when minimization is finished.

## Example Status Response
```
{
	"minExists": true,
	"tip3pExists": true,
	"tip5pExists": true,
	"conformerID": "1ogg",
	"status": "All complete"
}
```

12. Download the default structure (Or whichever structure you choose)
Just as the checkStatus script is simply a curl request sent to the appropriate url,
downloads are the same. We can make curl requests, or place the download url in
a browser, etc... The thing you need is the: downloadUrlPath from a Build3DStructure response.

An example curl request made from the command line was provided earlier in this doc:
[sample curl download](#curl-example)

A request made to https://dev.glycam.org/json/download/sequence/cb/<pUUID>/<conformerID>/
will return a minimized PDB file for that structure if it exists. The values in
responses' downloadUrlPath all follow this pattern, and may be all you need.
