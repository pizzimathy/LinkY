#!/usr/bin/env python3

import os
import os.path
import site
import stat


def _retrieve_path(var):
    """Returns the first path in the specified environment variable"""

    ps = os.getenv(var, default=None)

    if ps:
        return os.getenv(var).split(":")[0]
    else:
        return None


def load_command(command, file, src):
    """Generates a symlink for the specified file in the first env variable path"""

    # creates a source and dest path
    command_path = _retrieve_path("PATH")
    src_path = os.path.join(src, file)
    dest_path = os.path.join(command_path, command)

    # symlink
    os.symlink(src_path, dest_path)

    # changes file permissions
    st = os.stat(dest_path)
    os.chmod(dest_path, st.st_mode | stat.S_IEXEC)

    return {
        "src": src_path,
        "dest": dest_path
    }


def load_package(package_name, src):
    """Generates symlink for the specified package in the default site packages folder"""

    site_packages = site.getsitepackages()[0]
    src_path = os.path.join(src, package_name)
    dest_path = os.path.join(site_packages, package_name)
    os.symlink(src_path, dest_path, target_is_directory=True)

    return {
        "src": src_path,
        "dest": dest_path
    }
