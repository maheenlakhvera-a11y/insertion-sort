import random
import time


# All array sizes given in the lab manual
n_values = [100, 1000, 5000, 10000, 20000, 30000,
            40000, 50000, 60000, 100000, 500000, 1000000]


# Print the heading
print("n\tInsertion Sort Time (seconds)")
print("-" * 45)


# Test every array size one by one
for n in n_values:

    # Create an empty array
    array = []

    # Add n random numbers to the array
    for i in range(n):
        number = random.randint(1, 1000000)
        array.append(number)


    # Start the timer
    start_time = time.time()


    # Insertion Sort
    # Start from the second element
    for i in range(1, n):

        # Save the current number
        key = array[i]

        # Check the number before key
        j = i - 1

        # Move bigger numbers to the right
        while j >= 0 and array[j] > key:

            array[j + 1] = array[j]

            j = j - 1

        # Put key in its correct position
        array[j + 1] = key


    # Stop the timer
    end_time = time.time()


    # Calculate sorting time
    running_time = end_time - start_time


    # Display the result
    print(n, "\t", running_time)
