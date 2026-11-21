import sys

def Solution(segmentSize , missingData):
    # Implement your solution here
    
    hmap = {}
    low  , high = 1 , 0
    print("Segment size: " , segmentSize , "Missing data: " , missingData)
    for i in range(len(missingData)):
        hmap[missingData[i]] = hmap.get(missingData[i], 0) + 1
        high = max(high , hmap[missingData[i]])
    
    if len(hmap) > segmentSize:
        return "This is not possible"
    
    best = high
    while low <= high:
        mid = low + (high - low) // 2
        requriedSegments = 0
        
        
        for count in hmap.values():
            requriedSegments += (count + mid - 1) // mid
            
        if requriedSegments <= segmentSize:
            best = mid
            high = mid -1
        else:
            low = mid + 1
            
    used_length = 0
    char_count = {}
    print("hamp" , hmap , "Best: " , best)
    for ch , count in hmap.items():
            
        needed =  (count + best -1)//best 
        char_count[ch] = needed
        used_length += needed
    print("Used length: " , used_length
              , "Char count: " , char_count)
            
    if used_length < segmentSize:
        char_count['a'] = char_count.get('a' , 0) + (segmentSize - used_length)
            
    res = []
        
    for ch in sorted(char_count.keys()):
        res.append(ch * char_count[ch])
            
    return ''.join(res)
    
    
    


if __name__ == "__main__":
    
    tokens = iter(sys.stdin.read().split())
    
    segmentSize = int(next(tokens))
    
    missingData = next(tokens).strip('"\'')
    
    print(Solution(segmentSize , missingData))
    
    