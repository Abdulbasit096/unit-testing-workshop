# Semantic Versioning utility
# Author: owais.hussain@esquaredsystems.com


def break_into_parts(version):
    if version:
        parts = str.split(version, sep='.')
        major = parts[0]
        minor = parts[1]
        micro = parts[2]
        release_type = None
        subparts = str.split(micro, sep='-')
        if len(subparts) > 1:
            micro = subparts[0]
            release_type = subparts[1]
            if release_type not in ['alpha', 'beta']:
                raise Exception("Invalid release type!")
        return int(major), int(minor), int(micro), release_type


def is_version_valid(version):
    pass


def increase_major(version):
    major, minor, micro, _ = break_into_parts(version)
    major += 1
    version = f"{major}.{0}.{0}"
    return version


def increase_minor(version):
    pass


def increase_micro(version):
    pass


def is_alpha(version):
    pass


def is_beta(version):
    pass


def is_release(version):
    pass

