<html>
<head><title>Form Example</title></head>
<body>
<?php
if ($_SERVER['REQUEST_METHOD'] == "GET") {
    $items = explode("=",$_SERVER['QUERY_STRING']);
    $message = $items[1];
}
if ($_SERVER['REQUEST_METHOD'] == "POST") {
    $message = $_POST['message'];
}
print(strtoupper($message));
?>
</body>
</html>

