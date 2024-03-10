#QUESTION:

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
#plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]

#ALGO:

#BFS in graph / 2D matrix

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #bfs
        que=[(sr,sc)]
        visited=set()
        row=len(image)
        col=len(image[0])

        dir=[(-1,0),(1,0),(0,1),(0,-1)]
        while que:
            #length= len(que)
            #for _ in range(length):
            r,c=que.pop(0)
            visited.add((r,c))
            for rd,cd in dir:
                r1=r+rd
                c1=c+cd
                if (r1 in range(row)) and (c1 in range(col)) \
                and (r1,c1) not in visited and image[r1][c1]==image[sr][sc]:
                    image[r1][c1]=color
                    visited.add((r1,c1))
                    que.append((r1,c1))
        image[sr][sc]=color
        return image
        
