<html>
  <head>
  <title>Asal Sayı Kontrolü</title>
  </head>
  <body>
  <form action="asalsayi.php" method="post">
  Sayınız:<input type="text"name="sayi"><br><br>
  <input type="submit" value="Gönder">
    </form>
<br><br>
<?php
 $kontrol=0;
$sayi= $_POST['sayi'];
 for ($a=2; $a<($sayi/2) ; $a++)
   {
   if($sayi%$a==0)
   {
     $kontrol=1;
     echo "Sayınız Asal Sayı değildir. Çünkü $a ' e tam bölünmektedir.";
     break;
   }
   }
    if($kontrol==0)
   {
    echo " Sayınız Asal Sayıdır.";
    }
?>
</body>
</html>