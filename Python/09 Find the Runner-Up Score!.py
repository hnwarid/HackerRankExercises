if __name__ == '__main__':


    n = int(input())
    arr = map(int, input().split())    
    
scoreset = set(arr)
scoreset_list = list(scoreset)
scoreset_list.sort(reverse=True)
print(scoreset_list[1])
