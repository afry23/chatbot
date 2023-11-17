# CSS-Definition
css = """
/* Grundlegende Styling-Einstellungen */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 10px;
    background-color: #f0f0f0;
}

/* Stil für Chat-Nachrichten */
.message {
    max-width: 60%;
    margin-bottom: 10px;
    padding: 8px;
    border-radius: 15px;
    color: white;
}

/* Stil für Benutzer-Nachrichten */
.user {
    background-color: #007bff;
    align-self: flex-start;
    border-bottom-left-radius: 0;
}

/* Stil für Bot-Nachrichten */
.bot {
    background-color: #28a745;
    align-self: flex-end;
    border-bottom-right-radius: 0;
    text-align: right;
}

/* Flex-Container für Nachrichten */
.container {
    display: flex;
    flex-direction: column;
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