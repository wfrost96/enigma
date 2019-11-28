<!DOCTYPE html>
<html>

  <head>

    <?php
      include "./template.php"
    ?>

    <title>William Frost | The Enigma machine</title>
    <link rel="stylesheet" type="text/css" href="../encryption.css"/>
  </head>

  <body>

    <div class="container">

      <section class="content">
        <h1 id="blog-title">The Enigma Machine</h1>

        <h4 class="caption">Encrypting and decrypting a message with the Enigma machine.</h4>

        <p>The Enigma machine essentially mechanised the easy and efficient encrypting and decrypting of messages according to a random one-day-use key. First, three of a possible five scramblers were set in one of 26 positions. Then, six pairs of letters were swapped with cables. This surprisingly simple set-up had almost ten quintillion combinations, making it somewhat challenging to crack.</p>

        <p>Have a play on the one below and see how easy it is to both encrypt and decrypt messages. To decrypt a message, simply set up the machine as you did for encrypting, and type in the encrypted message you wish to decrypt.</p>

        <div class="caesar-cipher">
          <form method="POST">
            <div><h4>Type the message to encrypt or decrypt.</h4></div>
              <input type="text" name="unencrypted_message">
              <br><br>
            <h4>First, position your rotors.</h4>
            <table>
              <tr>
                <td>
                  <div>What is the first rotor's position?</div>
                </td>
                <td>
                  <select name="rotor1_position">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>
                  <div>What is the second rotor's position?</div>
                </td>
                <td>
                  <select name="rotor2_position">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>
                  <div>What is the third rotor's position?</div>
                </td>
                <td>
                  <select name="rotor3_position">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
              </tr>
            </table>
            <div><h4>Now, choose up to six letter pairs to be switched.</h4></div>
            <table>
              <tr>
                <td>
                  <div>First pair:</div>
                </td>
                <td>
                  <select name="pair1_letter1">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
                <td>
                  <select name="pair1_letter2">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>
                  <div>Second pair:</div>
                </td>
                <td>
                  <select name="pair2_letter1">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
                <td>
                  <select name="pair2_letter2">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>
                  <div>Third pair:</div>
                </td>
                <td>
                  <select name="pair3_letter1">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
                <td>
                  <select name="pair3_letter2">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>
                  <div>Fourth pair:</div>
                </td>
                <td>
                  <select name="pair4_letter1">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
                <td>
                  <select name="pair4_letter2">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>
                  <div>Fifth pair:</div>
                </td>
                <td>
                  <select name="pair5_letter1">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
                <td>
                  <select name="pair5_letter2">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>
                  <div>Sixth pair:</div>
                </td>
                <td>
                  <select name="pair6_letter1">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
                <td>
                  <select name="pair6_letter2">
                    <option>a</option>
                    <option>b</option>
                    <option>c</option>
                    <option>d</option>
                    <option>e</option>
                    <option>f</option>
                    <option>g</option>
                    <option>h</option>
                    <option>i</option>
                    <option>j</option>
                    <option>k</option>
                    <option>l</option>
                    <option>m</option>
                    <option>n</option>
                    <option>o</option>
                    <option>p</option>
                    <option>q</option>
                    <option>r</option>
                    <option>s</option>
                    <option>t</option>
                    <option>u</option>
                    <option>v</option>
                    <option>w</option>
                    <option>x</option>
                    <option>y</option>
                    <option>z</option>
                  </select>
                </td>
              </tr>
            </table>
            <br><br>
            <div class="submit-button-position">
              <input type="submit" value="Submit">
            </div>
          </form>

          <h4>
            <?php
              echo "Your message is: ";
              $unencrypted_message = $_POST['unencrypted_message'];

              $rotor1_position = $_POST['rotor1_position'];
              $rotor2_position = $_POST['rotor2_position'];
              $rotor3_position = $_POST['rotor3_position'];

              $pair1_letter1 = $_POST['pair1_letter1'];
              $pair1_letter2 = $_POST['pair1_letter2'];
              $pair2_letter1 = $_POST['pair2_letter1'];
              $pair2_letter2 = $_POST['pair2_letter2'];
              $pair3_letter1 = $_POST['pair3_letter1'];
              $pair3_letter2 = $_POST['pair3_letter2'];
              $pair4_letter1 = $_POST['pair4_letter1'];
              $pair4_letter2 = $_POST['pair4_letter2'];
              $pair5_letter1 = $_POST['pair5_letter1'];
              $pair5_letter2 = $_POST['pair5_letter2'];
              $pair6_letter1 = $_POST['pair6_letter1'];
              $pair6_letter2 = $_POST['pair6_letter2'];

              $output_encrypt = exec("python enigma.py $unencrypted_message $rotor1_position $rotor2_position $rotor3_position $pair1_letter1 $pair1_letter2 $pair2_letter1 $pair2_letter2 $pair3_letter1 $pair3_letter2 $pair4_letter1 $pair4_letter2 $pair5_letter1 $pair5_letter2 $pair6_letter1 $pair6_letter2");

              //$output_encrypt = exec("python test3.py $unencrypted_message $rotor1_position $rotor2_position $rotor3_position");
              echo $output_encrypt;
            ?>
          </h4>
        </div>

      </section>

    </div>

  </body>
</html>
