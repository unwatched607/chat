def generate_website_content():
    headline = "Empowering Rural Healthcare in India"

    points = [
        "1. Overview of Rural Healthcare",
        "2. Challenges Faced in Rural Areas",
        "3. Initiatives and Programs",
        "4. Impact on Community Health",
        "5. Future Prospects and Improvements"
    ]

    chatbot_script = """
    <script src="https://cdn.botpress.cloud/webchat/v1/inject.js"></script>
    <script>
      window.botpressWebChat.init({
          "composerPlaceholder": "Chat with bot",
          "botConversationDescription": "This chatbot was built surprisingly fast with Botpress",
          "botId": "dae79a81-8043-49ee-aa5b-888c088b75db",
          "hostUrl": "https://cdn.botpress.cloud/webchat/v1",
          "messagingUrl": "https://messaging.botpress.cloud",
          "clientId": "dae79a81-8043-49ee-aa5b-888c088b75db",
          "webhookId": "ef05ae7e-fae1-47fe-b9fc-10b6b7073c16",
          "lazySocket": true,
          "themeName": "prism",
          "frontendVersion": "v1",
          "showPoweredBy": true,
          "theme": "prism",
          "themeColor": "#2563eb"
      });
    </script>
    """

    content = f"<h1>{headline}</h1>\n\n"
    content += "<ul>\n"
    for point in points:
        content += f"  <li>{point}</li>\n"
    content += "</ul>\n\n"
    content += chatbot_script

    return content

if __name__ == "__main__":
    website_content = generate_website_content()

    with open("index.html", "w") as file:
        file.write(website_content)

    print("Website content generated successfully. Check 'index.html'")
