<?php
     
     $url = 'https://www.peridomicilio.com/frescos/congelados/tortas-congeladas/tortas-pollo-kimby-8und.html';
     $content = file_get_contents($url);

     print("<textarea>".$content."</textarea>");

     while(strpos($content, "http")){
         $posible_url = substr($content, strpos($content, "http"));

         $pos_final = strpos($posible_url, '"');
     }
?>