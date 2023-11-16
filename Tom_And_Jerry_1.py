def can_reach_jerry(a, b, c, d, k):
    # Calculate Manhattan distance
    distance = abs(a - c) + abs(b - d)
    
    # Check if Tom can make it in exactly K steps
    if distance > k or (k - distance) % 2 != 0:
        return "NO"
    else:
        return "YES"
        
t=int(input())
for i in range(t):
    a,b,c,d,K=map(int,input().split())
    print(can_reach_jerry(a,b,c,d,K))
