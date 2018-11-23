#!usr/bin/python3
#Has duplicate

def has_dup(A):
    N = len(A)
    for i in range(N):
        for j  in range(1 + i, N):
            if A[i] == A[j]:
                return True
    return False


print(has_dup([1,2,2,123,4,124]))      
