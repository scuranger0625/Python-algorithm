def sliding_window(s, k):
    left = 0
    window = {}
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        # 當窗口超過限制時收縮
        while right - left + 1 > k:
            window[s[left]] -= 1
            left += 1
        # 在這裡處理窗口 [left, right]
