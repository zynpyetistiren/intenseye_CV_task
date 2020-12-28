# intenseye
intenseye CV task




Main Algoritma:

  1. Soldan sağa tüm pixelleri tara
  2. Beyaz bir pixel bulunursa (köşe noktası):
   - Çember olup olmadığına bak. Çember ise o şekli boya ve bir sonraki pixele geç
   - Eğer çember değilse, ilk siyah pixeli bulana kadar yukarı doğru tara
   - İlk siyah pixeli bulana kadar aşağı doğru tara
   - Üstteki ilk siyah pixel, alttaki ilk siyah pixel ve bulunan ilk beyaz pixel arasındaki açıyı bul
   - Açıya göre şekli boya ve şeklin count sayısını arttır(çember dışındakileri)
  3. Şekil sayılarını yazdır ve şyeni boyanmış şekli göster
  
  
detectShape:
  1. Verilen açıya göre çember dışındaki şekilleri boyar ve sayılarını arttırır
  
  
isCircle: 
  1. Verilen beyaz noktanın doğrultusu boyunca en sağdaki beyaz noktayı bul
  2. En sağdaki nokta ile en soldaki noktanın arasındaki uzaklığın yarısını hesaplayarak çemberin yarıçapını bul
  3. Merkez noktadan yarıçap kadar uzaklıktaki sağ, sol ,üst ve alttaki noktaların beyaz olup olmadığına bakılır. Beyaz değil ise sekil cember değildir
  4. Merkez noktanın yarıçap kadar uzaklıktaki sağ üst, sol üst, sağ alt ve sol alt köşe noktalarının beyaz olup olmadığına bakılır
  5. Eğer tüm noktalar beyaz ise çemberdir
  
colorShape: 
  1. Verilen beyaz nokta verilen renge boyanır
  2. Verilen beyaz noktadan başlayarak sağ, üst ve alttaki noktaların beyaz olup olmadığına bakılır
  3.Beyaz ise o nokta için de aynı işlem uygulanır
  
  
calculateAngel: (burdaki hesaplamalar için math kütüphanesi kullanılmıştır)
  1. Verilen üç nokta arasındaki uzaklıklar hesaplanır
  2. Bu uzunluklara göre açılar hesaplanır
