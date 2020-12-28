#Zeynep Yetistiren
#intenseye cv task
from PIL import Image
from math import acos, degrees,sqrt



#maini duzenle


def colorShape(x,y,img,color):#en sol pixeli verilen şekli verilen renge boyamak için

    if img[x,y] == (255,255,255):#her beyaz pixel icin
        img[x,y] = color # beyaz pixeli istenilen renge boya

        if img[x+1,y] == (255,255,255) : img = colorShape(x+1,y,img,color) #sagındaki pixel beyazsa ona da aynı islemi uygula
        if img[x,y+1] == (255,255,255) : img = colorShape(x,y+1,img,color) #ustteki pixel beyazsa ona da aynı islemi uygula
        if img[x,y-1] == (255,255,255) :img = colorShape(x,y-1,img,color) #alttaki pixel beyazsa ona da aynı islemi uygula
        return img


def calculateAngle(x,y,z): # verilen 3 nokta(pixel) ile, 1.noktanın diğer iki noktayla olusturdugu açıyı hesaplama

    (x1,y1) = x
    (x2,y2) = y
    (x3,y3) = z

    length1 = sqrt((abs(x1-x2))**2 + (abs(y1-y2))**2) # 1. nokta ile 2. noktanın arasındaki uzaklık
    length2 = sqrt((abs(x2-x3))**2 + (abs(y2-y3))**2) # 2. nokta ile 3. noktanın arasındaki uzaklık
    length3 = sqrt((abs(x1-x3))**2 + (abs(y1-y3))**2) # 1. nokta ile 3. noktanın arasındaki uzaklık
    return degrees(acos((length1 ** 2 + length3** 2 - length2 **2)/(2 * length1 * length3)))#uzaklıklara baglı acıyı hesaplamak icin denklem



def isCircle(leftX,centerY,img):#bir seklin en soldaki noktasından cember olup olmadıgını anlama

    currentX = leftX #en soldaki noktanın x değeri (sutun)

    while img[currentX,centerY] == (255,255,255):#en soldaki nokta ile aynı satır boyunca en sagdaki beyaz nokta
        currentX = currentX + 1#en sagdaki beyaz noktanın x değeri

    r = ((currentX - leftX) / 2.0)#en soldaki nokta ile en sagdakini çıkararak yarıcapı bulma
    centerX = currentX - r #cemberin merkezinin x değeri

    isCircle = 1
    root = r / (sqrt(2))

    #alt-ust-sag-sol pixellerinde kayma olabildiğinden alttaki değerlere +4 -4 farklar ekledim ki birkaç pixel farkı tolere etsin

    if(img[centerX + r -4, centerY] != (255,255,255)): isCircle = 0 #merkezin yarıcap kadar sagındaki noktanın beyaz olup olmadığı kontrol edilir
    if(img[centerX - r +4, centerY ] != (255,255,255)): isCircle = 0#merkezin yarıcap kadar soldaki noktanın beyaz olup olmadığı kontrol edilir
    if(img[centerX , centerY + r -4] != (255,255,255)): isCircle = 0#merkezin yarıcap kadar alttaki noktanın beyaz olup olmadığı kontrol edilir
    if(img[centerX, centerY - r +4] != (255,255,255)): isCircle = 0#merkezin yarıcap kadar ustteki noktanın beyaz olup olmadığı kontrol edilir


    #merkezin yarıcap + 3 pixel kadar uzaktaki koselerinin siyah olup olmadığı kontrol edilir
    if(img[centerX - root-3, centerY - root-3] != (0,0,0)): # sol-ustteki nokta
        isCircle = 0 # left upper pixel
    if(img[centerX - root-3, centerY + root + 3] != (0,0,0)):#sol-alttaki nokta
        isCircle = 0 #right upper pixel
    if(img[centerX + root + 3, centerY - root - 3] != (0,0,0)):#sag-ustteki nokta
        isCircle = 0 #bottom left
    if(img[centerX + root + 3, centerY + root + 3 ] != (0,0,0)):#sag-alttaki nokta
        isCircle = 0#bottom right


    return isCircle


def detectShape(point, angle,counts,img):

    (triangleCount, squareCount, pentagonCount, hexagonCount) = counts

    (x,y) = point


    #seklin bir kosesindeki açı sayesinde sekli bul
    if 118 <= angle: #eger bulunan acı 118den buyukse altıgendir
        hexagonCount = hexagonCount + 1
        img = colorShape(x,y,img,(215,100,10))#altıgen ise turuncuya boya

    elif 95 <= angle <= 118:#seklin acısı 95 ile 118 arası ise besgendir
        pentagonCount = pentagonCount + 1
        img = colorShape(x,y,img,(255,20,140))# besgen ise pembeye boya

    elif angle < 70 :#70den kucuk acılar ucgendir
        triangleCount = triangleCount + 1
        img = colorShape(x,y,img,(255,255,100)) # ucgen ise sarıya boya

    elif 70< angle < 100 : # 70 ile 100 arasındaki acılar karedir
        squareCount = squareCount + 1
        img = colorShape(x,y,img,(30,160,230))#kare ise maviye boya


    return (triangleCount, squareCount, pentagonCount, hexagonCount)


def main():


    photo = Image.open("shapes.bmp")  # resmi acma
    img = photo.load()#resmi yukleme

    width, height = photo.size #resim boyutları


    circleCount = 0

    counts = (0,0,0,0)#tum sekillerin sayıları sıfırdan baslıyor

    #resimdeki her pixel icin
    #soldan saga dogru tarıyor

    for i in range(width):
        for t in range(height):

            color = img[i,t]
            if color == (255,255,255):#eger beyaz pixele rastlanırsa

                if (isCircle(i,t,img) == 1):#once cember olup olmadıgı kontrol edilir
                    img = colorShape(i,t,img,(0,255,0))#eger cember ise yesile boyanır
                    circleCount = circleCount + 1


                else:#cember değilse
                    LeftX = i +10 #seklin en solundaki beyaz noktanın x değeri (+10 değeri seklin mukemmel olmaması durumundaki kaymaları engellemek icin)
                    down_LeftY = t#seklin en solundaki beyaz noktanın y değeri

                    bottom_left_pixel = img[LeftX, down_LeftY]# en soldaki beyaz noktanın oldugu sutundaki en alttaki beyaz nokta

                    while (bottom_left_pixel == (255,255,255)):#en soldaki beyaz noktadan siyah bulana kadar asagı doğru kayma
                        down_LeftY = down_LeftY +1

                        if img[LeftX, down_LeftY] == (255,255,255):#noktalar beyaz oldugu surece alta kay
                            bottom_left_pixel = img [LeftX,down_LeftY]#en alt-sol noktasını guncelle
                        else:#en alttaki ve soldaki beyaz nokta bulundu
                            break


                    up_leftY = t
                    #en ust ve soldaki beyaz nokta bulunmaya calısılır
                    up_left_pixel = img[LeftX,up_leftY]

                    while (up_left_pixel == (255,255,255)):#noktalar beyaz oldugu surece
                        up_leftY = up_leftY - 1#yukarı dogru kay

                        if img[LeftX, up_leftY] == (255,255,255):
                            up_left_pixel = img [LeftX,up_leftY]#en ust-sol noktasını guncelle

                        else:#en ust-soldaki beyaz nokta bulundu
                            break

                    #en soldaki nokta en sol ustteki nokta ve en sol alttaki nokta ile seklin bi kosesindeki açıyı bul
                    angle = calculateAngle((i,t), (LeftX,down_LeftY), (LeftX,up_leftY))

                    counts = detectShape((i,t), angle, counts, img)


    (triangleCount, squareCount, pentagonCount, hexagonCount) = counts

    #sekillerin sayıları
    print("Number of circles: ", circleCount)
    print("Number of triangles: ", triangleCount)
    print("Number of sqaures: ", squareCount)
    print("Number of pentagons: ", pentagonCount)
    print("Number of hexagons: ", hexagonCount)


    pixels = list(photo.getdata())#resmin pixel değerleri
    image_out = Image.new(photo.mode,photo.size) #yeni resim olusturma
    image_out.putdata(pixels)#yeni resme pixel değerlerini koyma
    image_out.show()#resmi goster



if __name__ == "__main__":
    main()
