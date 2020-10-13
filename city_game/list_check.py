def list_check(ci):
    if ci[-1] in ('ь', 'ъ', 'ы'):
        k = ci[-2]
        b = ci[0:-1] + k  
        return b
    else:    
        return ci