import numpy as np
from PIL import Image

def asc_chr(num):
    num = int(num)
    if num < 8:
        answer = chr(num+65)
    elif num == 8:
        answer = 'K'
    elif num == 11:
        answer = 'P'
    elif num == 12:
        answer = 'R'
    elif num > 12:
        answer = chr(num+71)
    else:
        answer = chr(num+68)
    return answer


def asc_num(char):
    if char < 'I':
        answer = ord(char)-65
    elif char == 'K':
        answer = 8
    elif char == 'P':
        answer = 11
    elif char == 'R':
        answer = 12
    elif char > 'S':
        answer = ord(char) - 71
    else:
        answer = ord(char) - 68
    return answer

def get_data(pic):
    results = {}
    raw_img = Image.open(pic)
    img = raw_img.convert('1')
    x_size, y_size = img.size
    for x in xrange(x_size):
        results.setdefault(x, 0)
        for y in xrange(y_size):
            pixel = img.getpixel((x, y))
            if pixel == 0:
                results[x] += 1
    begin = end = -1
    for i in range(150):
        if results[i] > 0:
            begin = i
            break
    threshold_list = []
    for i in range(131, 134):
        threshold_list.append(results[i])
    threshold = max(threshold_list)
    i = 150
    stop = False
    while not stop:
        i -= 1
        if i == -1:
            begin, end = 10, 135
            break
        v = results[i]
        if v >= max((3.5, 2 * threshold)):
            stop = True
            tmp_value = v
            while True:
                i += 1
                if results[i] <= tmp_value:
                    if results[i] <= threshold:
                        end = i
                        break
                    else:
                        tmp_value = results[i]
                else:
                    end = i - 1
    centers = [((2 * i + 1) * end + (9 - 2 * i) * begin) / 10 for i in range(5)]
    data = np.empty((5, 3, 40, 40), dtype="float32")
    for index, center in enumerate(centers):
        a = center - 19
        b = center + 21
        img = raw_img.crop((a, 0, b, y_size))
        arr = np.asarray(img, dtype="float32") / 255.0
        data[index, :, :, :] = np.rollaxis(arr, 2)
    return data
