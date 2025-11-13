content="""
# {}

## Description

A brief description of your project. What problem does it solve? Who is this project for?

## Getting Started

### Dependencies

List any dependencies or prerequisites that must be installed before using the project.

### Installing

Provide step-by-step instructions on how to install and set up your project locally. Include code examples if necessary.

### Executing program

Explain how to run the project, including any command-line arguments or configuration settings that may be required.

## Help

If you need help with this project, please open an issue on GitHub or contact us directly at [your email address].

## Authors

List the authors of the project and their GitHub usernames if applicable.

## Version History

* 0.0.0
    * Initial Release
"""

import os 
makedirs = os.makedirs
sep = os.path.sep

def export_readme(destination, name="Project Title"):
    try:
        os.path.makedirs(destination)
    except:
        pass

    with open(destination+sep+"README.md", 'w') as fout:
        fout.write(
            content.format(name)
        )