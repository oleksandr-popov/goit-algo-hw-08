import heapq

def min_cost_to_connect_cables(cable_lengths):
    """
    Calculates the minimum cost to connect all cables into a single cable.
    The cost of connecting two cables is the sum of their lengths.
    """

    # Initialize the list as a min-heap
    # The heap property is essential for efficiently finding the two shortest cables.
    heapq.heapify(cable_lengths)

    # Define the total cost tracker
    total_cost = 0

    # Continue merging until only one cable (the final merged one) remains in the heap
    while len(cable_lengths) > 1:
        # Pop the two smallest cables from the heap
        # This is an O(log n) operation.
        first_shortest = heapq.heappop(cable_lengths)
        second_shortest = heapq.heappop(cable_lengths)

        # Calculate the cost of the merge (sum of their lengths)
        merge_cost = first_shortest + second_shortest

        # Add the merge cost to the running total
        total_cost += merge_cost

        # Push the newly merged cable's length back onto the heap
        # This represents the new cable that can be merged in the next steps.
        heapq.heappush(cable_lengths, merge_cost)

        # Print intermediate results for tracing the process
        print(
            f"Об'єднання кабелів {first_shortest} та {second_shortest} буде коштувати {merge_cost}. Загалом: {total_cost}"
        )
        print(f"Поточна дліна кабелів: {cable_lengths}")

    # The final result is the total cost accumulated
    return total_cost


if __name__ == "__main__":
    # Example cable lengths
    initial_lengths = [7, 1, 6, 4]

    # Variant to use randomize values for cable lengths
    # import random
    # initial_lengths = [random.randint(1, 25) for _ in range(6)]
    print(f"Initial cable lengths: {initial_lengths}")
    print("-" * 50)

    # Run the function
    min_cost = min_cost_to_connect_cables(initial_lengths)

    print("-" * 50)
    print("Мінімальни витрати для об'єднання усіх кабелів:", min_cost)