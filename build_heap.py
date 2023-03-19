# 221RDB323
# Danila Sinicins
# 17. grupa
import os

def build_heap(data):
    swaps = []
    dataLen=len(data)
    for i in range(dataLen//2, -1, -1):
        shift_down(data, i, swaps)
    return swaps


def shift_down(data, i, swaps):
    dataLen = len(data)
    indexMin = i
    leftChild = 2*i+1
    rightChild = 2*i+2
    if leftChild < dataLen and data[leftChild] < data[indexMin]:
        indexMin = leftChild
    if rightChild < dataLen and data[rightChild] < data[indexMin]:
        indexMin = rightChild
    if indexMin != i:
        swaps.append((i, indexMin))
        data[i], data[indexMin] = data[indexMin], data[i]
        shift_down(data, indexMin, swaps)


def main():
    
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    elif "F" in text:
        fileName = input()
        
        path = './tests/'    
        folder = os.path.join(path, fileName)           
        with open(folder, "r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    else:
        print("I/F:")
        return


if __name__ == "__main__":
    main()
