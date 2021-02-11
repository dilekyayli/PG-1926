<?php
error_reporting(0);
 
if(isset($_POST)) 
{ 
$num1 = $_POST['sayi1'];
$num2 = $_POST['sayi2'];
 
 
for($i=$num1; $i<=$num2;$i++)
{ 
   $toplam=0;
   for($j=1; $j<$i-1; $j++)
  {
         if($i%$j==0)
        {
             $toplam+=$j;
        }
   }
   if($toplam==$i)
   echo $i."<br>";
 
 }
 
} //isset
 
 
if(!($_POST)) 
{ 
 
?>
 
 
<!DOCTYPE html>
<html>
<head>
<title>Mükemmel Sayı Kontrolü</title>
</head>
<body>
 
<form method="POST" action="<?= $_SERVER['PHP_SELF']?>" >
<table align="center" border="0">
<tr>
<td colspan="2" align="center">
<h3>Mükemmel Sayıları Bul</h3>
</td>
</tr>

<tr>
<td>Sayı 1:</td>
<td><input type="number" name="sayi1"></td>
</tr>

<tr>
<td>Sayı 2:</td>
<td><input type="number" name="sayi2"></td>
</tr>

<tr>
<td colspan="2" align="center">
<input type="submit" name="Mükemmel Sayıları Bul">

</td>
</tr>
</table>
</form>
</body>
</html>