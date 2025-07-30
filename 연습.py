def solution(polynomial):
    x = 0
    num = 0
    poly_l = polynomial.split(' ')
    for i in range(len(poly_l)):
        if 'x' in poly_l[i]:
            if poly_l[i] == 'x':
                x += 1 
            else:
                x += int(poly_l[ : -1])
        elif poly_l[i].isnumeric() == True:
            num += int(poly_l[i])
    if x == 0:
        return str(num)
    if num == 0:
        return f'{x}x'
    return f'{x}x + {num}'

print (solution("3x + 7 + x"))


#####################


def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            
            f_r = -1
            t_r = 1
            f_c = -1
            t_c = 1
            
            if board[i][j] % 2 == 1:        # 지뢰 있는 곳
                if i == 0:
                    f_r = 0
                    t_r = 1
                elif i == n-1:
                    f_r = -1
                    t_r = 0
                if j == 0:
                    f_c = 0
                    t_c = 1
                elif j == n-1:
                    f_c = -1
                    t_c = 0             
    
                for r in range(i+f_r, i+t_r+1):
                    for c in range(j+f_c, j+t_c+1):
                        board[r][c] += 2
            
                    
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    
    return answer



######################################



def solution(board):
    n = len(board)
    answer = 0
    for i in range(n):
        for j in range(n):
            f_r = -1
            t_r = 1
            f_c = -1
            t_c = 1
            if i == 0:
                f_r = 0
                t_r = 1
            elif i == n-1:
                f_r = -1
                t_r = 0
            if j == 0:
                f_c = 0
                t_c = 1
            elif j == n-1:
                f_c = -1
                t_c = 0
                
            isSafe = True    
            for r in range(i+f_r, i+t_r+1):
                if isSafe == False:
                    break
                for c in range(j+f_c, j+t_c+1):
                    if board[r][c] == 1:
                        isSafe = False
                        break
        
            if isSafe == True:
                answer += 1
    
    return answer







def solution(board):
    n = len(board)
    answer = 0
    for i in range(n):
        for j in range(n):
                
            f_r = 0 if i == 0 else -1
            t_r = 0 if i == n-1 else 1
            f_c = 0 if j == 0 else -1
            t_c = 0 if j == n-1 else 1
                
            isSafe = True    
            for r in range(i+f_r, i+t_r+1):
                if isSafe == False:
                    break
                for c in range(j+f_c, j+t_c+1):
                    if board[r][c] == 1:
                        isSafe = False
                        break
        
            if isSafe == True:
                answer += 1
    
    return answer