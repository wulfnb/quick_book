$json = file_get_contents('php://input');
$someObject = json_decode($json);

echo gettype($someObject);
foreach($someObject as $key=>$value){
    echo $key;
    echo gettype($value);
    print("<pre>" . print_r($value, true) . "</pre>");

}