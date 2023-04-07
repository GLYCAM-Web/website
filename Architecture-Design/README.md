# Architecture and Design Docs for GLYCAM-Web

These docs span the entire GLYCAM-Web enterprise.  They contain information regarding all aspects of software and systems that are required for the website to function.

## Enterprise Architecture Documents

These diagrams provide views of all aspects of the production of GLYCAM-Web.  You will find information about the software here, but you will also find information about hardware and people and all the other factors that go into making the website work.   To better understand the docs, it will help if you learn at least a little about the [Archimate Specification](https://pubs.opengroup.org/architecture/archimate32-doc/) for enterprise architecture.   However, you can probably get an overall gist without knowing the meanings of all the arrows, symbols and colors.

These docs are mostly maintained by Lachele Foley.  They began as design docs for a refactor of GEMS, but quickly expanded to include all aspects of the functioning of GLYCAM-Web.  If you have questions, [open an issue](https://github.com/GLYCAM-Web/website/issues) and she, or someone, will try to answer.   

### Viewing

The main way to view the docs is with the [Archi software](https://www.archimatetool.com/).  But, an html report of the docs is also available. 

#### Using a web browser to view the html

This is the easiest way for most folks.  

On the command line:
- Navigate to `website/Architecture-Design/Archimate/html`
- Enter the command to load `index.html` into your browser.  For example, if you are using Firefox, you might enter `firefox index.html` .

From a browser window:
- In the URL bar, type three forward slashes (`///`) and hit enter.  This should allow  you to browse your filesystem.
- Browse to this repository, then down to  `website/Architecture-Design/Archimate/html`
- Click on `index.html`

Once you have the docs open, expand the "Views" in the "Model Tree" pane.

#### Using Archi to view the archimate file

You might need to read some docs or watch some videos before you can really use this method, but it is the most flexible.  Resources for learning to use Archi are available on the software website.

- Download and install the [Archi software](https://www.archimatetool.com/) 
- Open the file `website/Architecture-Design/Archimate/GLYCAM-Web.archimate`

### Naming conventions used herein

Names of views are prefixed with the overall portion of the GLYCAM-Web enterprise that they concern.

- ENTERPRISE:  These views concern at least some portions of systems and software.  They might concern people, motivational factors, etc., as well.
- GEMS, GMML, MD_Utils:  These views concern these specific code bases.
- SOFTWARE: These views concern software that we write that is directly related to the business goals of GLYCAM-Web.  
- SYSTEMS: These views concern software, that might be written by us or by others, and hardware, that are used to support the functions of the business-goal software.