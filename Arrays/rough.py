def areDistinct(stri):
    result = 0

    for i in range(len(stri)):
        mid = ''
        mid = mid + stri[i]
        count = 1
        # print("mid", mid)

        for j in range(i + 1, len(stri)):
            if stri[j] not in mid:
                # print(stri[j])
                mid = mid + stri[j]
                # print("mid", mid)
                count += 1
            else:
                    break
            
            if count > result:
                    result = count
    return result
    
                    


stri = 'GEEKSFORGEEKS'
print(areDistinct(stri))
