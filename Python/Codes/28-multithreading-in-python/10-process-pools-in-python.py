# ProcessPoolExecutor class in Python :
import concurrent.futures


def square(num):
    return num * num


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        numbers = [1, 2, 3, 4, 5]
        results = executor.map(square, numbers)

    for result in results:
        print(result)