from typing import Iterable, Iterator, List, TypeVar
import heapq
import random

T = TypeVar("T")


def merge_k_lists(lists: Iterable[Iterable[T]]) -> List[T]:
    """Merge k sorted iterables into a single sorted list.

    Uses a min-heap to repeatedly take the smallest head element among the
    active iterators. Input iterables must be sorted in ascending order.

    Args:
        lists: An iterable of sorted iterables (e.g. lists, tuples, generators).

    Returns:
        A new list containing all elements from the inputs in ascending order.

    Notes:
        - Empty iterables are ignored.
        - If input iterables are not sorted, the result will not be globally
          sorted; ensure inputs are sorted before calling.
    """
    heap: list = []
    # Build iterators and push first element of each (if any) to the heap.
    for idx, seq in enumerate(lists):
        
        it = iter(sorted(seq))
        try:
            first = next(it)
        except StopIteration:
            # skip empty iterables
            continue
        # Push tuple (value, source_index, iterator) so ties are broken by index
        heapq.heappush(heap, (first, idx, it))

    merged: List[T] = []
    while heap:
        value, src_idx, it = heapq.heappop(heap)
        merged.append(value)
        try:
            nxt = next(it)
        except StopIteration:
            continue
        heapq.heappush(heap, (nxt, src_idx, it))

    return merged


# Generate list with random integer values in interval [min, max)
def rand_list(n, min=0, max=100):
    return [random.randint(min, max) for _ in range(n)]

if __name__ == "__main__":
    # # Quick demonstration
    # a = [1, 4, 9, 10]
    # b = [2, 3, 7]
    # c = [0, 5, 8, 11, 20]

    # print("Input lists:")
    # for i, lst in enumerate((a, b, c), 1):
    #     print(f"  list {i}: {lst}")

    # merged = merge_k_lists((a, b, c))
    # print("\nMerged:")
    # print(merged)

    # Example Usage
    lists = [rand_list(10), rand_list(8), rand_list(6)]

    print("Початкові списки:", lists)
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)