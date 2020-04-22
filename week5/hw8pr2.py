''' List 2 Questions #missing 2'''

def count_evens(nums):
  count=0
  for i in nums:
    if i %2 == 0:
      count +=1
  return count


def big_diff(nums):

    return max(nums)-min(nums)


def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)


def sum13(nums):
    '''skip 'only' the 'first' number after 13
        not skipping all the numbers after 13.'''
    s = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 1
        else:
            s += nums[i]

        i += 1

    return s



def sum67(nums):
    '''Assisted by prof: set 6 as a switch of the loop, when not trigger 6 == False
            when there is 6, trigger the switch and make it to True
            when True, skip until there is a 7 because when there is a 7, it will turn the switch back to False
            so the loop can keep adding it.'''
    sum = 0
    seen6 = False

    for i in range(len(nums)):

        if nums[i] == 6:
            seen6 = True

        if seen6 == True:
            pass
        else:
            sum += nums[i]

        if nums[i] == 7:
            seen6 = False
    return sum





def has22(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False


'''String 2 Questions'''


def count_code(str):
    if str[0:4] == 'code':
        return 1 + count_code(str[1:])

    else:
        if len(str) < 4:
            return 0
        elif str[:2] == 'co' and str[3] == 'e':
            return 1 + count_code(str[1:])
    return count_code(str[1:])


def double_char(str):
    result = ''
    for i in str:
        result += i * 2
    return result

def count_hi(str):
    if str[0:2] == 'hi':
        return 1 + count_hi(str[1:])

    else:
        if len(str) < 2:
            return 0
    return count_hi(str[1:])


def end_other(a, b):
    a = a.lower()
    b = b.lower()

    return a.endswith(b) or b.endswith(a)


def xyz_there(str):
    for i in range(len(str)):
        if str[i] != '.' and str[i+1:i+4] == 'xyz':
            return True
    if str[0:3] == 'xyz':
        return True
    return False


def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)):
    if str[i:i+3] == 'cat':
      cat +=1
    if str[i:i+3] == 'dog':
      dog +=1
  return cat == dog

