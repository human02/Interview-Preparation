"""


  Write a function that takes in a "special" array and returns its product sum.

  A "special" array is a non-empty array that contains either integers or other
  "special" arrays. The product sum of a "special" array is the sum of its
  elements, where "special" arrays inside it are summed themselves and then
  multiplied by their level of depth.


  The depth of a "special" array is how far nested it is. For instance, the
  depth of [] is 1; the depth of the inner array in [[]] is 2; ; the depth of the innermost array in
  [[[]]] is 3. 
  Therefore, the product sum of [x, [y, [z]]] is x + 2 * (y + 3z)

  Input:
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
  Output:
    12
  

"""
# O(N) time (where in sample N is 12 and not 9)| O(D) space where D is the max depth of the string


def productSum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier
