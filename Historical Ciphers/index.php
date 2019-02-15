<?php

// make conection
$conn = new mysqli('localhost', 'root', '', 'ciphers');

$SELECT = "SELECT * FROM PREVIOUS_CIPHER ORDER BY id DESC LIMIT 1";

$result = mysqli_query($conn, $SELECT);

$data = mysqli_fetch_all($result, MYSQLI_ASSOC);

mysqli_free_result($result);

mysqli_close($conn);

?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Historical Ciphers</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="css/mystyle.css">
    <link rel="stylesheet" type="text/css" media="screen" href="css/bootstrap.css" />
    <script src="js/bootstrap.bundle.js"></script>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Historical Ciphers</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="index.html">Home<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Contact</a>
                </li>
                <div class="btns">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Register</a>
                    </li>
                </div>
                <div class="btns1">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Log In</a>
                    </li>
                </div>
        </div>
    </nav>

    <form action="connect.php" method="POST">
        <table class="Encrypt_container">

            <tr>
                <td><p>Encryption Scheme :</p></td>
                <td id="opt">
                    <select autofocus id="option" required="required">
                        <option  value="">-- Select option --</option>
                        <option  value="cs">Caesars</option>
                        <option  value="mn">Mono</option>
                        <option  value="sf">Shift</option>
                        <option  value="vg">Vigenere's</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td><p>Plaintext :</p></td>
                <td><input id="inp_1" type="text"></td>
            </tr>
            <tr>
                <td><p>Key :</p></td>
                <td><input id="inp_2" type="text"></td>
            </tr>
            <tr>
                <td>Cipher Text :</td>
                <td><input id="out" type="text" name="cipher"></td>
            </tr>
            <tr>
                <td><button id="btn1" onclick="choose_algo()">Encrypt</button></td>
            </tr>
        </table>
    </form>

    <div class="container">
            <p style="display:none;" id="txt">BruteForce Attack :</p>
            <?php foreach($data as $datas) : ?>
                <p id="txt1" style="display:none;"><?php echo $datas['entry']; ?></p>
            <?php endforeach; ?>
            <textarea style="display:none;" name="" id="t_area" cols="50" rows="20"></textarea>
        </div>

    <table class="btn12">
        <tr>
        <td><button id="btn2" onclick="retrieve()">Retrieve</button></td>
        </tr>
        <tr>
            <td><button id="btn3" onclick="BruteForce()">Brute Force Attack</button></td>
        </tr>
    </table>
    <script src="index.js"></script>
</body>
</html>