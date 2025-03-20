# WebTool How-To For Scientists

This document describes the work needed before code produced by a scientist can be integrated into 
the GLYCAM-Web online tools.

The basic steps are:

1. Ensure that your code is portable.
2. Generate a list of systems requirements (software with versions, specific hardware, etc.)
3. Generate scripts or other executables or information so that the website can perform:
    * Validation of the environment and inputs.
    * Evaluation of the options available to the user and of the suitability of the inputs.
    * Execution of the scientific code.
    * Assessment of the statusof the code execution.
4. Make user-friendly descriptions of the inputs and outputs. From these, the API for your tool
   will be constructed.

**Keep the science in your code!** It is important that the website and GEMS only rarely be required 
to make scientific decisions or actions. 

## Ensure Portability

If you are like the rest of us, the first complete version of your code will probably only run when 
started by your user and in the environment that you use. You will need to make it portable, that is, 
usable by others and in other environments.

Here are some ways to find the changes needed to make your code portable, in the desired order:

1. Run your code on a different computer from the one you usually use.
2. Hand the code to a colleague, preferably a colleague who uses different computing systems.
3. Give your code to the website team.

Things that reduce portability:

* Use of hard-coded paths that are specific to your system.
* Reliance on specific versions of other software.
* Use of environment variables that are not explicitly referenced in your code.

## Validation 

Validation: ensuring that the correct inputs and environment are present and usable.

Validation just makes sure that everything is present. It makes no judgments about suitability.

There are two main ways to handle validation. Your strategy can be a mix of these or something else.

1. Give the website developers a description of a complete set of inputs, environment settings, etc.
2. Write your own validation script. Experienced tool developers might prefer this one because they 
   might have already written code to validate the system when running the code themselves. 

## Evaluation

Evaluation: determining what actions are possible, or required, based on the nature of the inputs.

Evaluation figures out if the inputs are good and asks what can be done with them.  If there are options
to be offered to the webtool user, this is the step that determines what options are available. Even if
the options are always the same, we generally offer them after ensuring that the inputs are usable.

Example evaluation tasks:

* Count the number of conformers expected based on a carbohydrate sequence.
* Determine the locations of glycosylation sites.
* Ensuring that input files can undergo preliminary data processing.

You must produce a script, executable, or set of instructions for performing the evaluation. 

## Execution

This is often called "Run" or "Build". This is the part of the process that performs the scientific
work. This step assumes that all the necessary inputs and environments are present and correct.

You must produce a script, executable, or set of instructions for this step. 

## Assessment

The website needs to know how to determine when your code has finished its tasks and the extent to 
which the tasks were successful. This is usually called 'status checking'.

There are multiple ways to do this. Here are a few:

* Check for the existence of certain output files.
* Ensure that certain words or phrases exist in certain files.
* Write a running log of the process.
* Write a script or executable that will return a status. This is preferred.

## API

Chances are that the inputs and outputs for your scientific tool are not easily interpreted by others.
The API should wrap your inputs and outputs in a way that is easy for others to understand.

For example, when you run your code, it might look like this:

    run_program 5 file.txt 7 acid 06j

This might mean that your code requires a number of replicas (5), an output file (file.txt), a spatial
cutoff in Angstroms (7), the protonation state of carboxylates (acid, ion) and the name of the force 
field to use for the carbohydrate (`GLYCAM_06-j`). The purpose of the API is to translate between your
terse command-line abbreviations and terms that are friendlier for others.
