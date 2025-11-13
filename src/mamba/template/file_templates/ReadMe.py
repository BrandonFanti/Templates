from .format_strings import ReadMeFormatStrings

from os import makedirs, path
sep = path.sep

from enum import Enum
class ReadMeType(Enum):
    PythonPackage = 0
    PythonProject = 1
    PythonApp = 2

def export_file(destination,content):
    try:
        makedirs(sep.join(destination.split(sep)[:-1]))
    except FileExistsError:
        pass
    except:
        print("Failed to create directory (permissions or space?)")
        raise 

    with open(destination, 'w') as fout:
        fout.write(content)

def export_readme(destination, name="Project Title", template_type=ReadMeType.PythonProject):
    rel_path_list = []

    destination += sep

    match template_type:
        case ReadMeType.PythonProject:

            rel_export_path = "README.md"
            rel_path_list.append(rel_export_path)
            export_file(
                destination+rel_export_path,
                ReadMeFormatStrings.project.format(name)
            )


            rel_export_path = "docs"+sep+"package_summary.md"
            rel_path_list.append(rel_export_path)
            export_file(
                destination+rel_export_path,
                ReadMeFormatStrings.package_summary.format(name)
            )

        case ReadMeType.PythonPackage:
            rel_export_path = "README.md"
            export_file(
                destination+rel_export_path,
                ReadMeFormatStrings.package.format(name)
            )
            rel_path_list.append(export_path)
        
        case ReadMeType.PythonApp:
            rel_export_path = "README.md"
            export_file(
                destination+rel_export_path,
                ReadMeFormatStrings.app.format(name)
            )
            rel_path_list.append(export_path)

    return rel_path_list
