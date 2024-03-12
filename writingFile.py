import cv2
img=cv2.imread("cion2.jpeg")
cv2.imshow("python programmer",img)

k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
    print("all windows destroyed")
elif k==ord("a"):
    cv2.imwrite("newcoin.png",img)
    cv2.destroyAllWindows()