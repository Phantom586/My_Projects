<?php

$cipher_txt = $_POST['cipher'];

if (!empty($cipher_txt)) {
    $host = "localhost";
    $dbUsername = "root";
    $dbPassword = "";
    $dbname = "ciphers";

    // Create Connection
    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);

    if (mysqli_connect_error()) {
        die('Connect Error('.mysqli_connect_errno().')'. mysqli_connect_error());
    }
    else {
        $SELECT = "SELECT entry FROM previous_cipher";
        $INSERT = "INSERT Into previous_cipher (entry) values(?)";
        //Prepare the statements
        $stmt = $conn->prepare($SELECT);
        $stmt->bind_param('s', $cipher_txt);
        $stmt->execute();
        $rnum = $stmt->num_rows;
        if ($rnum==0) {
            $stmt->close();
            $stmt = $conn->prepare($INSERT);
            $stmt->bind_param("s", $cipher_txt);
            $stmt->execute();
            echo "New record inserted sucessfully";
        }
        else {
            echo "Unable to Store the Cipher";
        }
        $stmt->close();
        $conn->close();
    }
}
else {
    echo "All Fields are required";
    die();
}
?>