class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
  
        max_y = len(matrix)-1
        max_x = len(matrix[0])-1
        min_y = 0
        min_x = 0

        lst1 = ((0,1),(1,0),(0,-1),(-1,0))
        houkou = 0

        index_y =0
        index_x =0

        output = []

        if max_y==0 or max_x==0:
            return sum(matrix,[])

        for i in range(len(matrix[0])*len(matrix)):
            
            print(f" = {matrix[index_y][index_x]}")
            output.append(matrix[index_y][index_x])

            index_y += lst1[houkou][0]
            index_x += lst1[houkou][1]
            next_y = index_y + lst1[houkou][0]
            next_x = index_x + lst1[houkou][1]

            if next_x < min_x or max_x < next_x or next_y < min_y or max_y < next_y :
                print("次曲がる")
                if houkou == 0:
                    houkou += 1
                    min_y +=1
                elif houkou == 1:
                    houkou += 1
                    max_x -=1
                elif houkou == 2:
                    houkou += 1
                    max_y -=1
                else:
                    houkou = 0
                    min_x +=1
            
        return output


hoge=Solution()

#print(hoge.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
#print(hoge.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(hoge.spiralOrder([[3],[2]]))

"""
1 2 3
4 5 6
7 8 9
  ↓
時計回りの渦巻順に読んで
[1,2,3,6,9,8,7,4,5]
を返す

2:15

"""