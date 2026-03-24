<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>游禎友簡介</title>
	<style type="text/css">
		* { font-family:"標楷體"; margin-left:auto; margin-right:auto;}
		h1 {color:blue; font-size:60px;}
		h2 {color:#33ff33; font-size:40px;}
	</style>
	<script>
		function change1() {
  			document.getElementById("pic").src = "mountain.jpg";
  			document.getElementById("h2text").innerText = "靜宜資管";
		}

		function change2() {
  			document.getElementById("pic").src = "cliff.jpg";
  			document.getElementById("h2text").innerText = "Yu Chen Yu";
		}
	</script>
</head>
<body>
    <?php echo date("Y-m-d") ?>
    <table width="70%">
        <tr>
            <td>
                <img src="cliff.jpg" width="110%" id="pic" onmouseover="change1()" onmouseout="change2()">
            </td>

            <td>
                <h1>游禎友</h1>
                <h2 id="h2text">Yu Chen Yu</h2>
            </td>
        </tr>
    </table>
    <table width="70%" border="1">
        <tr>
            <td>
                IG：
                <a href="https://www.instagram.com/zhenyou_0712" target="_blank">
                    https://www.instagram.com/zhenyou_0712
                </a><br>

                Tel：
                <a href="tel:0972180192">0972-180-192</a><br>

                E-Mail：
                <a href="mailto:s1131634@o365st.pu.edu.tw">
                    s1131634@o365st.pu.edu.tw
                </a><br>
            </td>

            <td>
                大象席地而坐電影配樂<br>
                <audio controls>
                    <source src="elephant.mp3" type="audio/mpeg">
                </audio><br>
            </td>

            <td>
                不要去臺灣<br>
                <iframe width="300" height="200"
                    src="https://www.youtube.com/embed/pW88QFpHXa8"
                    allowfullscreen>
                </iframe>
            </td>
        </tr>
    </table>
</body>
</html>