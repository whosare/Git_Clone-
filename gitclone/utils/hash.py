import hashlib

import os, zlib

#
def hash_object(data: bytes, obj_type: str = "blob", write=False, repo_path=".gitclone") -> str:
    header = f"{obj_type} {len(data)}".encode()
    full_data = header + b'\x00' + data
    sha1 = hashlib.sha1(full_data).hexdigest()

    if not write:
        return sha1

    # Store in .gitclone/objects/ab/cdef... structure
    dir_path = f"{repo_path}/objects/{sha1[:2]}"
    file_path = f"{dir_path}/{sha1[2:]}"

    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(zlib.compress(full_data))

    return sha1
