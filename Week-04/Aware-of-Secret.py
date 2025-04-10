# 2327. Number of People Aware of a Secret

def peopleAwareOfSecret(n, delay, forget):
    MOD = 10**9 + 7
    
    dp = [0] * (n + 1)
    dp[1] = 1 
    
    sharing = 0
    
    for day in range(2, n + 1):
        
        if day - delay >= 1:
            sharing = (sharing + dp[day - delay]) % MOD
    
        if day - forget >= 1:
            sharing = (sharing - dp[day - forget] + MOD) % MOD
                
        dp[day] = sharing
    
    total = 0
    for day in range(max(1, n - forget + 1), n + 1):
        total = (total + dp[day]) % MOD
        
    return total

# no class Solution this time
print(peopleAwareOfSecret(6, 2, 4))
