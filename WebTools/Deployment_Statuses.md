# Deployment Statuses for New GLYCAM-Web Tools

**Legend**

* New  -  The code is usable only by the scientist.
* Portable  -  The code can be used by others in other environments.
* Prototype  -  A prototype of this part of the web-tool has been generated.
* API  -  The API has been generated.
* DevEnv  -  The tool can be deployed and tested in the development platform.
* Test  -  The tool is being tested and refined in an online production-like environment.
* Actual  -  The tool is deployed to Actual (glycam.org).
* System - The underlying system dependencies needed for functionality in production.


| Tool                       | Validate  | Evaluate  | Build     | Status    | Remaining Work |
| -------------------------- | --------- | --------- | --------- | --------- | -------------- |
| Automated Antibody Docking | Test      | Test      | Test      | Prototype | DevEnv         |
| Glycomimetics              | Test      | API       | API       | API       | DevEnv         |
| Emails from Web Tools      | n/a       | n/a       | Prototype | New       | System         |
| Glycoprotein Builder       | Portable  | Portable  | API       | Portable  | API, DevEnv    |
| GlySpec                    | Prototype | Prototype | Prototype | Prototype | Rewrite        |
| DrawGlycan                 | n/a       | n/a       | Portable  | n/a       | API, DevEnv    |
| PDB Preprocessor           |           |           | Portable  |           | API, DevEnv    |


Notes: 

* Automated Antibody Docking cannot be deployed yet to our DevEnv despite being available in live sites.
