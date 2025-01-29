
papers = ["A", "B", "C", "D", "E", "F"]
citations = [1, 3, 4, 5, 5, 5]


def get_hindex(papers, citations):

    # h-index is calculated as: 
    # the most number of papers which are cited the same amout. So here it would be 3.

    hindex = 0

    for i in range(1, len(papers)):

        # check if there are at least i numbers bigger than i
        nums_bigger = [num for num in citations if num >= i]
        if len(nums_bigger) >= i:
            hindex = i
            continue
        else:
            break
    print(hindex)


def get_hindex2(citations):

    # h-index is calculated as: 
    # the most number of papers which are cited the same amout. So here it would be 3.

    hindex = 0
    citations = sorted(citations)
    
    # [1, 3, 4, 5, 5, 5] n = 6

    n = len(citations)
    for i, c in enumerate(citations):

        if c >= n-i:
            print(n-i)
            break

    #print(hindex)

#get_hindex(papers, citations)
get_hindex2(citations)