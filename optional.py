import heapq
import random


def merge_k_lists(lists):
    """
    Merges k sorted lists into a single sorted list using a min-heap.

    The heap stores a tuple for each element:
    (value, list_index, element_index_in_list)
    """

    # Initialize the min-heap
    min_heap = []

    # Populate the heap with the first element from each input list
    # The heap is initialized with tuples containing the value, the list index (i),
    # and the element index within that list (0).
    for i in range(len(lists)):
        # Check if the list is not empty
        if lists[i]:
            # The tuple is (value, list_index, element_index)
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    # Initialize the final merged list
    merged_list = []

    # Extract minimum elements and add next elements to the heap
    # Loop continues as long as there are elements in the heap
    while min_heap:
        # Get the smallest element available from all lists
        value, list_idx, element_idx = heapq.heappop(min_heap)

        # Add the smallest value to the result list
        merged_list.append(value)

        # Check if there is a next element in the list the value came from
        next_element_idx = element_idx + 1

        if next_element_idx < len(lists[list_idx]):
            # Get the next value from that list
            next_value = lists[list_idx][next_element_idx]

            # Create the tuple for the next element and push it onto the heap
            next_tuple = (next_value, list_idx, next_element_idx)
            heapq.heappush(min_heap, next_tuple)

    # Return merged and sorted list
    return merged_list


# Generate list with random integer values in interval [min, max)
def rand_list(n, min=0, max=100):
    return [random.randint(min, max) for _ in range(n)]


# Example Usage
lists = [rand_list(5), rand_list(6), rand_list(2)]

print("Початкові списки:", lists)
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
