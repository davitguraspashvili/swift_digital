def biggerIsGreater(w):

    i = 0
    for _ in range(len(w)-1):
        i -= 1
        if w[i] > w[i-1]: 

            w = list(w)
            saved = w[i-1] 
        
            min_to_find = w[i:]
            min_value = min(min_to_find)
            while min_value <= saved:
                if len(min_to_find) == 1:
                    break
                min_to_find.remove(min_value)
                min_value = min(min_to_find)

            w[i + w[i:].index(min_value)] = saved
            w[i-1] = min_value
        
            left_part = w[:i]
            right_part = w[i:]
            right_part.sort()
            answer = left_part + right_part
            
            return "".join(answer)

    return "no answer"

print(biggerIsGreater("fedcbabcd"))
