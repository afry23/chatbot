# CSS-Definition
css = """
body {
    font-family: Arial, sans-serif;
    font-size: 14px;
    color: black;
    line-height: 1.5;
    margin: 0;
    padding: 10px;
    background-color: #827e7e;
}

/* Stil für Chat-Nachrichten */
.message {
    max-width: 90%;
    margin-bottom: 10px;
    padding: 8px;
    border-radius: 15px;
    color: black;
}

/* Stil für Benutzer-Nachrichten */
.user {
    background-color: #dcf8c6;
    align-self: flex-start;
    border-bottom-left-radius: 0;
}

/* Stil für Bot-Nachrichten */
.bot {
    background-color: #ffffff;
    align-self: flex-end;
    border-bottom-right-radius: 0;
    text-align: right;
}
.avatar {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 10px;
}

/* Flex-Container für Nachrichten */
.container {
    display: flex;
    flex-direction: column;
    background-color: #f7f7f7;
}
"""

# HTML-Struktur
html_content = f"""
<html>
<head>
    <style>
    {css}
    </style>
</head>
<body>
    <div class='container'>
        <!-- Messages go here -->
    </div>
</body>
</html>
"""