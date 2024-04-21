'''車牌+找文字框'''
import cv2

binary_threshold = 100 #閥值
spacing = 0.95 #間距

img = cv2.imread('car2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,ret = cv2.threshold(gray, binary_threshold, 255, 1) #1=>cv2.THRESH_BINARY_INV(反二值)

white = []
black = []
height = img.shape[0]
width = img.shape[1]

print(f'寬:高 = {width}:{height}')
white_max = 0
black_max = 0
count = 0

#以寬的方式去掃 
for w in range(width): 
    w_count = 0
    b_count = 0
    #再以高的方式去掃
    for h in range(height):
        # 把所有黑白點計算出來
        if ret[h][w] == 255:
            w_count += 1
        else:
            b_count += 1
    white_max = max(white_max,w_count) #白色最大
    black_max = max(black_max,b_count) #黑色最大
    white.append(w_count)
    black.append(b_count)
print('whitemax=',white_max)
print('blackmax=',black_max)

arg = black_max > white_max #黑底白字或白底黑字 T or F


def find_end(start_): #找出結論 黑多還是白多
    end_ = start_ + 1
    for m in range(start_ +1, width -1):
        # 字典表達式 if arg成立=> black[m] , if arg 不成立=> white[m]
        # 字典表達式 if arg成立=>spacing*black_max, if arg不成立=> spacing*white_max
        # 表達 黑底白字多 還是白底黑字多
        if (black[m] if arg else white[m]) > (spacing * black_max if arg else spacing * white_max) :
            end_ = m
            break
    return end_


n = 1
start = 1
end = 2
# 
while n < width -1 :
    n+=1
    # if arg成立=> white[n], if arg不成立=> black[n]
    # if arg成立=> (1-spacing)*white_max, if arg不成立=> (1-spacing)*black_max)
    if (white[n] if arg else black[n]) > ((1-spacing)*white_max if arg else (1-spacing)*black_max):
        start = n
        end = find_end(start)
        n = end
        if end - start > 12 : #
            w+=1
            print(start,end)
            cm = img[1:height,start-10:end+10] # start-10:end+10 給一些空間給文字空間，不然會裁到字體
            cv2.imwrite(str(w)+'.jpg',cm) #把全部的圖存起來




cv2.imshow('img', ret)


cv2.waitKey()
cv2.destroyAllWindows()

