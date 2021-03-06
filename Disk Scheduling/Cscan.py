if __name__ == "__main__":
    process = [98,183,37,122,14,124,65,67]
    head = 53
    disk_size = 200
    queue = process.copy()
    queue.append(0)
    queue.append(disk_size-1)

    smaller_operations = []
    larger_operations = []
    for operation in queue:
        if operation < head:
            smaller_operations.append(operation)
        else:
            larger_operations.append(operation)

    smaller_operations.sort()
    larger_operations.sort()

    sequence = []
    seek_count = 0

    for operation in larger_operations:
        cur_track = operation
        sequence.append(operation)
        absolute_distance = abs(operation - head)
        seek_count += absolute_distance
        head = cur_track

    absolute_distance = abs(0 - head)
    seek_count += absolute_distance
    head = 0

    for operation in smaller_operations:
        cur_track = operation
        sequence.append(operation)
        absolute_distance = abs(cur_track - head)
        seek_count += absolute_distance
        head = cur_track
    print("The Seek Sequence is : ",sequence)
    print("The distance travelled is ",seek_count)
