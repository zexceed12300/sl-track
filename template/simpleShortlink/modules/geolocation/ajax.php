<?php
header('Content-Type: text/html');{
    $lat = $_POST['Lat'];
    $long = $_POST['Long'];
    $acc = $_POST['Acc'];

    $f = fopen('../../../../tmp/latlong.txt', 'w+');
    fwrite($f, $lat);
    fwrite($f, "\r\n");
    fwrite($f, $long);
    fwrite($f, "\r\n");
    fwrite($f, $acc);
    fclose($f);
}
?>