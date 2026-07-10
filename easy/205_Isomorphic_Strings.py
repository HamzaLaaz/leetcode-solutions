def isIsomorphic(s: str, t: str) -> bool:
    s_d = {}
    t_d = {}
    for i in range(len(s)):
        if s[i] in s_d and s_d[s[i]] != t[i]:
            return False
        if t[i] in t_d and t_d[t[i]] != s[i]:
            return False
        s_d[s[i]] = t[i]
        t_d[t[i]] = s[i]
    return True
