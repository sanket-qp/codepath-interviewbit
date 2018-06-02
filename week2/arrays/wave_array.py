"""
https://www.interviewbit.com/problems/wave-array/
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example:
Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]

NOTE : If there are multiple answers possible, return the one thats lexicographically smallest. 
So, in example case, you will return [2, 1, 4, 3] 
"""
def wave_array(array):
    if len(array) <= 1:
        return array
    array.sort()
    i, j = 0, 1
    while i < len(array)-1:
        if array[j] == array[i]:
            i += 2
        elif array[j] != array[i]:
            array[i], array[j] = array[j], array[i]
            i += 2
        j = i+1
    return array

def main():
    array = [1, 5, 3, 4, 2, 6]
    array = [1,2,3,4]
    wave = wave_array(array)
    assert wave == [2,1,4,3]
    
    array = [1, 2, 2]
    wave = wave_array(array)
    assert wave == [2,1,2]

    array = [1,1,1,2,2,3,3,5]
    wave = wave_array(array)
    assert wave == [1,1,2,1,3,2,5,3]

    array = [1,1,1,1,2,2,3,3,5]
    wave = wave_array(array)
    assert wave == [1,1,1,1,2,2,3,3,5]

    array = [1,1,1,2,1,2,1,1]
    wave = wave_array(array)
    assert wave == [1,1,1,1,1,1,2,2]

if __name__ == "__main__":
    main()
