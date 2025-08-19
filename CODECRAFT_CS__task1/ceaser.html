<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Caesar Cipher Tool</title>
    <style>
        body {
            font-family: 'Courier New', Courier, monospace;
            background-color: #0d1117;
            color: #c9d1d9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background-color: #161b22;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
            width: 450px;
            text-align: center;
            border: 1px solid #30363d;
        }

        h1 {
            color: #58a6ff;
        }

        label {
            font-weight: bold;
            display: block;
            text-align: left;
            margin: 10px 0 5px;
        }

        input[type="text"],
        input[type="number"],
        select {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #30363d;
            border-radius: 4px;
            background-color: #0d1117;
            color: #c9d1d9;
        }

        button {
            background-color: #238636;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }

        button:hover {
            background-color: #2ea043;
        }

        .result {
            margin-top: 20px;
            font-weight: bold;
            color: #58a6ff;
        }

        footer {
            margin-top: 20px;
            font-size: 0.8em;
            color: #8b949e;
        }

        .highlight {
            color: #f85149;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Caesar Cipher Tool</h1>

    <label for="mode">Mode:</label>
    <select id="mode">
        <option value="encrypt">Encrypt (Plaintext → Ciphertext)</option>
        <option value="decrypt">Decrypt (Ciphertext → Plaintext)</option>
    </select>

    <label for="textInput">Enter Text:</label>
    <input type="text" id="textInput" placeholder="Enter your message..." />

    <label for="shiftKey">Shift Key (1–25):</label>
    <input type="number" id="shiftKey" placeholder="e.g. 3" min="1" max="25" />

    <button onclick="processCipher()">Run Caesar Cipher</button>

    <div class="result" id="resultOutput"></div>

    <footer>
        <p>Master Caesar Cipher Encryption & Decryption.</p>
    </footer>
</div>

<script>
    function caesarShift(text, shift, encrypt = true) {
        if (!encrypt) shift = -shift;
        let result = '';

        for (let i = 0; i < text.length; i++) {
            let char = text[i];

            if (char >= 'A' && char <= 'Z') {
                let code = char.charCodeAt(0);
                result += String.fromCharCode(((code - 65 + shift + 26) % 26) + 65);
            } else if (char >= 'a' && char <= 'z') {
                let code = char.charCodeAt(0);
                result += String.fromCharCode(((code - 97 + shift + 26) % 26) + 97);
            } else {
                result += char; // Keep punctuation, spaces, etc.
            }
        }

        return result;
    }

    function processCipher() {
        const mode = document.getElementById('mode').value;
        const inputText = document.getElementById('textInput').value;
        const shiftKey = parseInt(document.getElementById('shiftKey').value);
        const resultOutput = document.getElementById('resultOutput');

        if (!inputText || isNaN(shiftKey) || shiftKey < 1 || shiftKey > 25) {
            resultOutput.textContent = '⚠️ Please enter valid text and a shift key (1–25).';
            return;
        }

        const isEncrypting = mode === 'encrypt';
        const result = caesarShift(inputText, shiftKey, isEncrypting);

        resultOutput.textContent = isEncrypting
            ? `🔐 Encrypted Text: ${result}`
            : `🔓 Decrypted Text: ${result}`;
    }
</script>

</body>
</html>
