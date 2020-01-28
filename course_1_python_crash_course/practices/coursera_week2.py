#!/usr/bin/env python3
'''
If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the storage size needed for a given filesize?
'''
test_case = [1, 111, 409, 4095, 4096, 4097, 8192, 8193]


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block = filesize % block_size
    # Depending on whether there's a remainder or not, return the right number.
    print(f'This is full_blocks for file size - {filesize}: {full_blocks}')
    print(
        f'This is partial_blocks for file size - {filesize}: {partial_block}')
    if partial_block > 0:
        return block_size * (full_blocks + 1)
    return block_size


for number in test_case:
    print(f'The result for test case {number}: {calculate_storage(number)}')
    print(f'')
