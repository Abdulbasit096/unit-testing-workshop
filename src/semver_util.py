


def break_into_parts(version):
    if version:
        parts = str.split(version, sep='.')
        if len(parts) < 3:
            raise Exception('Invalid version')
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
    major, minor, micro, release_type = break_into_parts(version)
    if (major is None) or (minor is None) or (micro is None):
        return False
    else:
        return True



def increase_major(version):
    major, minor, micro, release_type = break_into_parts(version)
    major += 1
    version = f"{major}.{0}.{0}"
    if release_type:
        version += f'-{release_type}'
    return version


def increase_minor(version):
    major, minor, micro, release_type = break_into_parts(version)
    minor += 1
    version = f"{major}.{minor}.{0}"
    if release_type:
        version += f'-{release_type}'
    return version


def increase_micro(version):
    major, minor, micro, release_type = break_into_parts(version)
    micro += 1
    version = f"{major}.{minor}.{micro}"
    if release_type:
        version += f'-{release_type}'
    return version


def is_alpha(version):
    _, _, _, release_type = break_into_parts(version)
    if release_type == 'alpha':
        return True
    else:
        return False


def is_beta(version):
    _, _, _, release_type = break_into_parts(version)
    if release_type == 'beta':
        return True
    else:
        return False


def is_release(version):
    _, _, _, release_type = break_into_parts(version)
    if release_type is None:
        return True
    else:
        return False

