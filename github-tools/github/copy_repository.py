"""Recursively copy files using a specific language's whitelist"""

import re
import shutil

from pathlib import Path

WHITELIST_FILENAME = "github.whitelist"

def ensure_dir(path):
    try:
        path.mkdir(parents=True)
    except OSError:
        pass


def get_whitelist_pattern(src):
    path = src + "/" + WHITELIST_FILENAME
    with open(path, "r") as f:
        patterns = [line.strip() for line in f.readlines()]
        # drop empty lines
        patterns = [p for p in patterns if p]
    print("Using patterns: {!r}".format(patterns))
    return re.compile("|".join(patterns))


def copy(src, dest, dry_run=True):
    whitelist = get_whitelist_pattern(src)

    dst_root = Path(dest)
    if not dry_run:
        ensure_dir(dst_root)

    src_root = Path(src)
    for src_file in list(src_root.glob('**/*')):
        # include all intermediate directories
        src_name = src_file.relative_to(src_root)

        # Skip directories to prevent creating empty directories
        if src_file.is_dir():
            continue

        if whitelist.match(str(src_name)):
            dst_file = dst_root / src_name
            print('ALLOW: {} >> {}'.format(src_file, dst_file))

            if not dry_run:
                # Make sure parent directory exists
                ensure_dir(dst_file.parent)
                shutil.copyfile(str(src_file), str(dst_file))
                shutil.copymode(str(src_file), str(dst_file))
        else:
            print('DENY - {}'.format(src_file))
