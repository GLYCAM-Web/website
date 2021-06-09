# USAGE

## Overview
The JSON API provides an interface to the services made available by GEMS and GMML.

We make html requests to the API's urls, often providing json-formatted input. GEMS
then interprets requests, determines which service(s) are appropriate to provide,
and the api returns json-formatted responses.

A typical pattern might involve:
1. Evaluate some sequence to determine if it can be built, and if any options are
    available for that sequence.
2. Request that a 3D structure be generated for a sequence, possibly with options for which conformers (shapes) to generate.
3. Request the build status of either a default shape for the 3D structure, or one of the conformers.
4. When the desired 3D structure file exists, request the file as an attachment in a response.

An in-depth walkthrough of one way this might happen is provided in the
[Appendix: Walkthrough](#walkthrough)

## Submitting requests to the API
The sample script we provide, [api-https.bash](api-https.bash), makes a curl request
for you, attaching the json input file that you indicate and submitting that to the
json api.

	`bash api-https.bash <json-input-file> <website-url>`

### Example:

	`bash api-https.bash build-sequence.json dev.glycam.org`

### Sample input files
Our sample input files demonstrate the json input format for making requests to
services that GEMS provides:

* [marco.json](marco.json)
* [evaluate-sequence.json](evaluate-sequence.json)
* [build-sequence.json](build-sequence.json)

# Sequence Services
## Marco
marco.json is for testing the connection. If you receive a response that says
"polo", you are good.

## Evaluate
The Evaluate service returns json-formatted information about options that are available for a
requested structure. If you just want to know if we can build a sequence, this might
be the service you prefer.

## Build3DStructure
The Build3DStructure service returns very similar information. These requests can
optionally define build options, if desired. If you only wish to retrieve a "default" 3D structure,
you can ignore the build options.

Requests to build a PDB file generate responses with these features:
* A download url for a project.
* IDs for each available conformer in that project.
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
If you need to download a pdb file for a sequence, start with Build3DStructure.
The Build3DStructure service can be used both with and without build options
defined. In the case where no options are provided in the request, responses
will provide:
* a full evaluation,
* structureBuildInfo for accessing PDB files for specific conformations.

#### Build without setting options
The example json-formatted request in [build-sequence.json](build-sequence.json) does not set any options.
The example response in [Example-OUTPUT.build-sequence.Response.json](Example-OUTPUT.build-sequence.Response.json) includes the same evaluation data present in the
evaluate request, but also provides downloadUrlPath values for downloading the
structures available for that sequence.

For a detailed example of a build request with no user options, see:
* [build-sequence.json](build-sequence.json)
* [Example-OUTPUT.build-sequence.Response.json](Example-OUTPUT.build-sequence.Response.json)

#### Note about default structures
We do assign a default conformer for each sequence. There is nothing special about
the conformer we select to be the default, we just give one conformer a value of
isDefaultStructure : true in the response's individualBuildDetails.

This means:
* If you don't care which conformer you use, grabbing any is valid, it need not
be the default structure to be consistent, just continue using the same conformer ID.
* If you desire to specifically find the default structure, it is found by examining
response output. In the list of individualBuildDetails, each object has a field
"isDefaultStructure". Only the default structure will have a value of true.

#### Build with options
One can set many options, and request up to 64 conformers (shapes) of a structure.
This involves:
1. Submitting an original request to retrieve the possible options
for your sequence, (as demonstrated, evaluate, or build requests suffice for this)
2. Submitting a second request, with options set, following the patterns in the
build response,
3. Polling the Build_Status url for the status of your builds,
4. Downloading some or all via the downloadUrl provided in the response.

For a detailed example of a build request with user options specified, see:
* [build-sequence-with-options.json](build-sequence-with-options.json)
* [Example-OUTPUT.build-sequence-with-options.Response.json](Example-OUTPUT.build-sequence-with-options.Response.json)

## Polling for the status of a specific build
Given a project ID and a conformer ID, we can check the status of a specific build.
Using the following url:
```
http://dev.glycam.org/cb/build_status/<ProjectID>/<ConformerID>/
```
We can receive a json object like the following:
```python
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

Look in the file containing [sample output from build-sequence-with-options.json.](Example-OUTPUT.build-sequence-with-options.Response.json)  Inside,
you will find a section like this:

```
{
    "structureBuildInfo": {
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
        },
        ...  
```

The downloadUrlPath above is used in the following example.


### Curl Example
In all this talk about requests and responses, it can be easy to get confused.
Under the hood, our sample scripts are making url calls to send requests to the
JSON API, and receiving json formatted responses. You don't need

#### Using curl on the command line

To save a file with filename molecule.pdb, set by the website, use:

`curl -L -o molecule.pdb [URL]`

for example:

`curl -L -o molecule.pdb https://test.glycam.org/json/download/sequence/cb/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/1ogg/`

Do be certain that there is not already a file with the same name in your directory.


# Appendix

## Walkthrough
### Default Structure
*Key concept:* Default structure is a value we use to ensure we always show the same
file when no specific conformer is needed. If you are unconcerned with which
conformation you want, ANY conformerID found in a response is good. As long as you
consistently use the same conformerID for a given structure, GEMS consistently
returns the same structure.


1. Create a folder to work in somewhere. We will use this, for example:
`
 test/
`
2. Create a new file. You can name it what you like. It will be the command we run to
start our process. We will use this, for example:
`
testTheAPI.sh.
`
3. Copy the contents of this [script](api-https.sh) into your test script. If you run the script with no arguments, you will get a helpful usage message.

> The script you just created accepts an argument for JSON input, and a host. We have
sample json files that demonstrate the format needed for for requests. Feel free
to use these and edit the input as needed.

> This walkthrough will demonstrate using [build-sequence.json](build-sequence.json),
which requests DManpa1-6DManpa1-OH. You can simply replace the sequence and this
file can be used as input to request the default structure for any valid sequence.

4. In the same folder as your test script, create a new file to contain the json
input. We will use this, for example:
`
build-sequence.json.
`
5. Copy the contents of this [build-sequence.json](build-sequence.json) into your new
file. Because the script and its input are in the same path in our example, we
just use the filename with no path. If you need to add paths, and if you use
different file names, remember to edit the following to reflect your needs. Run
the following command to submit your request:
```bash
$ bash testTheApi.sh build-sequence.json dev.glycam.org
```
> You can expect some chatty logs on your console, followed by a printout
of your response object. This is also written to file, by the test script we just
called in the command above. You can edit that if you want different filenames or
output locations.
There is a lot in the output. These responses serve more purposes than ours, but
that means we are only interested in two pieces of data:
* pUUID - A key to find the project that your request created. Needed for
    polling file status.
* download_url_path for the project -  A base for the URL we can call to
download the default structure. Both of these live in the json object's project.
For example:
```python
myProject = responseDict['project']['pUUID']
myDownloadUrl = responseDict['project']['download_url_path']
```

6. Poll for the status of the default structure's project files.
Currently, a conformer ID is required to check build statuses. We find the conformer ID
of the default structure in the response to our Build3DStructure request.
>Note: There is nothing special about the default structure. If you don't care
which structure, grabbing the first conformerID you find is appropriate.

#### Conformer ID Lookup Example:
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
>>>>>>>>"conformerID": "1ogg",
        "conformerLabel": "1ogg",
        "sequenceConformation": ["1", "o", "gg"],
>>>>>>>>"isDefaultStructure": true,
        "isNewBuild": false,
        "structureDirectoryName": "1ogg",
        "filesystem_path": "/website/userdata/",
        "host_url_base_path": "https://dev.glycam.org",
        "conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Requested_Builds/1ogg",
        "absolute_conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Existing_Builds/1ogg",
>>>>>>>>"downloadUrlPath": "https://dev.glycam.org/json/download/sequence/cb/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/1ogg/",
        "forceField": "See Build Directory Files"
    },
```
The above snippet shows how responses offer conformerIDs, downloadUrlPath,
and pUUID, each indicated by '>>>>>>>>'.

7. We provide a sample script that you can use to poll for the status of the
file you requested. Create a new file. We will use this, for example:
`
checkStatus.sh
`
8. Copy the content of [checkStatus.sh](checkStatus.sh) into your new script.
9. In the response to your original request, find the pUUID for your project, and
grab an appropriate conformerID. (Remember any are valid, but only default has
'isDefaultStructure' : true)
10. Run the script with your selected args. The example script will echo out the status
response, and also writes it out to file.
```bash
$ bash checkStatus.sh <pUUID> <conformerID>
```
Our example would be:
```bash
$ bash checkStatus.sh a997768f-6097-4aa6-9789-c756252358df 1ogg
```
11. Examine the response to find the status. This example status response
indicates that all files are complete. If you need verification that it has
been minimized, 'minExists' will only return true when minimization is finished.
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
12. Download the default structure (Or any structure you choose.)
Just as the checkStatus script is simply a curl request sent to the appropriate url,
downloads are the same. We can make curl requests, or place the download url in
a browser, etc... The thing you need is the: downloadUrlPath from a Build3DStructure response.

An example curl request made from the command line was provided earlier in this doc:
[sample curl download](#curl-example)

A request made to https://dev.glycam.org/json/download/sequence/cb/<pUUID>/<conformerID>/
will return a minimized PDB file for that structure if it exists. The values in
responses' downloadUrlPath all follow this pattern, and may be all you need.
