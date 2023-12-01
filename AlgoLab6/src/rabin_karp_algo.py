def rabin_karp_algo(haystack, needle):
    if not haystack or not needle:
        return []

    base_hash = 256

    q = 7
    n = len(needle)
    m = len(haystack)
    result_indices = []

    hash_needle = 0
    hash_haystack = 0
    h = 1
    for i in range(n - 1):
        h = (h * base_hash) % q

    for i in range(n):
        hash_needle = (base_hash * hash_needle + ord(needle[i])) % q
        hash_haystack = (base_hash * hash_haystack + ord(haystack[i])) % q

    for i in range(m - n + 1):
        if hash_needle == hash_haystack:
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    break
            else:
                result_indices.append(i)

        if i < m - n:
            hash_haystack = (
                base_hash * (hash_haystack - ord(haystack[i]) * h)
                + ord(haystack[i + n])
            ) % q

            hash_haystack = (hash_haystack + q) % q

    return result_indices
