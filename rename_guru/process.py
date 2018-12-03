import re
import os
from glob import glob
import stringcase


def generate_variations(name):
    return [
        # stringcase.snakecase(name),
        stringcase.camelcase(name),
        stringcase.uppercase(stringcase.snakecase(name)),
        stringcase.capitalcase(name),
    ]

def process(input_file, rename, to, parameters):
    files = glob(input_file + "/*")
    for file_name in files:
        new_path = process_file(file_name, rename, to, parameters)
        if os.path.isdir(new_path):
            process(new_path, rename, to, parameters)

def process_file(file_name, rename, to, parameters):

        new_name = replace(file_name, rename, to, parameters._replace(verbose=False))

        if parameters.verbose:
            print("\nProcessing \"%s\"" % (file_name,))

            if file_name != new_name:
                print("\trename file \"%s\" -> \"%s\"" % (file_name, new_name,))

        if not os.path.isdir(file_name):
            with open(file_name, "r") as f:
                content = f.read()

            new_content = replace(content, rename, to, parameters)

            if parameters.real:
                with open(file_name, "w") as f:
                    f.write(new_content)

        if parameters.real:
            os.rename(file_name, new_name)

        return new_name


def replace(content, rename, to, parameters):
    to_variations = generate_variations(to)

    to_replaces = []

    for rename_index, rename_variation in enumerate(generate_variations(rename)):
        for match in re.finditer(rename_variation, content):
            to_replace = (match[0], to_variations[rename_index])
            to_replaces.append(to_replace)
            if parameters.verbose:
                print("\t%s -> %s" % to_replace)

    replaced_content = content

    for to_replace in to_replaces:
        replaced_content = replaced_content.replace(to_replace[0], to_replace[1])

    return replaced_content