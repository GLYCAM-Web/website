
* build-sequence.json
* marco.json
* sequence.json

Sample output json:

* Example-OUTPUT.build-sequence.json.Response.json
* Example-OUTPUT.marco.json.Response.json
* Example-OUTPUT.sequence.json.Response.json

# Using the output

Look in the file containing sample output from build-sequence.json.  Inside, 
you will find a section like this:


`      "Build3DStructure": {
        "payload": "132acfa6-2518-4b0a-b7fa-80f3bebb1881",
        "downloadUrl": "http://dev.glycam.org/json/download/cb/132acfa6-2518-4b0a-b7fa-80f3bebb1881"
      }`

To retrieve your file(s), you can:

* Enter the downloadUrl into a browser window.
* Use wget or curl or some other command line tool.

## Example:  using curl on the command line

To save a file with the filename set by the website, use:

`curl -J -O [URL]`

for example:

`curl -J -O http://dev.glycam.org/json/download/cb/132acfa6-2518-4b0a-b7fa-80f3bebb1881`

Do be certain that there is not already a file with the same name in your directory.

