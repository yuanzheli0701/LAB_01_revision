class Post:
    def __init__(self, id, likes, comments, shares):
        self.id = id
        # engagement_score = likes*1 + comments*2 + shares*3
        self.score = likes * 1 + comments * 2 + shares * 3

def max_eng(p, l, r):
    if l == r: return p[l]
    mid = (l + r) // 2
    L = max_eng(p, l, mid)
    R = max_eng(p, mid + 1, r)
    return L if L.score > R.score else R

def sum_eng(p, l, r):
    if l == r: return p[l].score
    mid = (l + r) // 2
    return sum_eng(p, l, mid) + sum_eng(p, mid + 1, r)

def avg_eng(p, l, r):
    return sum_eng(p, l, r) / (r - l + 1)

def count_thr(p, l, r, t):
    if l == r: return 1 if p[l].score > t else 0
    mid = (l + r) // 2
    return count_thr(p, l, mid, t) + count_thr(p, mid + 1, r, t)

def m_sort(p, l, r):
    if l < r:
        mid = (l + r) // 2
        m_sort(p, l, mid)
        m_sort(p, mid + 1, r)
        left_half = p[l:mid + 1]
        right_half = p[mid + 1:r + 1]
        i = j = 0
        k = l
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i].score >= right_half[j].score:
                p[k] = left_half[i]
                i += 1
            else:
                p[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            p[k] = left_half[i]
            i += 1; k += 1
            
        while j < len(right_half):
            p[k] = right_half[j]
            j += 1; k += 1

def find_peak(likes, l, r):
    if l == r: return l
    mid = (l + r) // 2
    if likes[mid] < likes[mid + 1]:
        return find_peak(likes, mid + 1, r)
    else:
        return find_peak(likes, l, mid)
