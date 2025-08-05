import os
import binascii

from gitclone.utils.hash import hash_object

def write_tree(entries: list):
    tree_entries = []

    for file_path, blob_hash in entries:
        mode = "100644"  # regular file
        path_bytes = file_path.encode()
        mode_bytes = mode.encode()

        # Convert hex hash to raw binary (20 bytes)
        sha_bytes = binascii.unhexlify(blob_hash)

        tree_entry = mode_bytes + b" " + path_bytes + b"\x00" + sha_bytes
        tree_entries.append(tree_entry)

    tree_data = b"".join(tree_entries)
    tree_hash = hash_object(tree_data, obj_type="tree", write=True)

    return tree_hash
