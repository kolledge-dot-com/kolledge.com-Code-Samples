# How to use Multiprocessing in Python :
import multiprocessing


def calc_square(numbers):
    for n in numbers:
        print('Square:', n * n)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    p = multiprocessing.Process(target=calc_square, args=(numbers,))
    p.start()
    p.join()




# Python Multiprocessing Practical Example
import multiprocessing
import PyPDF2


def count_pages(filename):
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        return pdf_reader.getNumPages()


if __name__ == '__main__':
    filenames = ['file1.pdf', 'file2.pdf', 'file3.pdf']

    with multiprocessing.Pool() as pool:
        results = pool.map(count_pages, filenames)

    for filename, pages in zip(filenames, results):
        print(f'{filename}: {pages} pages')
