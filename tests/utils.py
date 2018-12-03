import os
from glob import glob
from typing import Callable


def compare_file_tree(path1: str, path2: str, callback: Callable[[str, str], None]) -> None:
    for file in glob("%s/**" % path1):
        relative_path = file[len(path1):]
        if os.path.isdir(path1):
            if not os.path.isdir(path2):
                raise Exception("%s not exists" % path2)
        else:
            with open(path2+relative_path) as f1:
                with open(file) as f2:
                    callback(f1.read(), f2.read())
