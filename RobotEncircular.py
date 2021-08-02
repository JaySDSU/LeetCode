# Intialize the direction and then traverse instructions and update dir and x,y as per instructions

N = 0
E = 1
S = 2
W = 3

class Solution(object):

    def encircular(self,instructions: str) -> bool:
        instructions = instructions*4
        x,y = 0,0
        dir = N
        for ins in instructions:
            if ins == 'L':
                dir = (4 + dir - 1)% 4
            if ins == 'R':
                dir = (dir + 1)%4
            else:
                if dir == N:
                    y += 1
                elif dir == E:
                    x -= 1
                elif dir == S:
                    y -= 1
                else:
                    x += 1
        return (x==0 and y==0)
        
obj = Solution()
s1 = "GGLLGG"
s2 = "GG"
s3 = "GL"

print(obj.encircular(s1))
print(obj.encircular(s2))
print(obj.encircular(s3))
            
