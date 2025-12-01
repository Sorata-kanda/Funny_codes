<div align="center">

# 🎉 Discord Welcome Assistant

<img src="/discord bot/discord-welcome-app/anime_favicon.jpeg" alt="Discord Welcome Assistant" width="150" height="150" style="border-radius: 20px;">

### ⚡ Automate Your Discord Welcomes with OCR Magic ⚡

[![Electron](https://img.shields.io/badge/Electron-26.2.0-47848F?style=for-the-badge&logo=electron&logoColor=white)](https://www.electronjs.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tesseract](https://img.shields.io/badge/Tesseract-OCR-00599C?style=for-the-badge&logo=google&logoColor=white)](https://github.com/tesseract-ocr/tesseract)

---

</div>

## 🌟 What It Does

This powerful desktop app monitors your Discord welcome channel and helps you greet new members instantly:

- 📸 **Auto-Capture** - Takes screenshots of Discord welcome messages
- 🔍 **Smart OCR** - Extracts usernames using advanced OCR technology
- 💾 **Memory Storage** - Stores unique usernames automatically
- ⚡ **Quick Paste** - Paste all collected usernames with @ mentions in one click

<div align="center">

### 🎯 Perfect for Discord Community Managers!

</div>

## 📋 Prerequisites

Before running this app, you need to install:

### 1️⃣ Node.js (v16 or higher)
> 🔗 Download from: https://nodejs.org/

### 2️⃣ Python (v3.8 or higher)
> 🔗 Download from: https://www.python.org/downloads/
> 
> ⚠️ **Important:** Check "Add Python to PATH" during installation

### 3️⃣ Tesseract OCR
> 🔗 Download from: https://github.com/UB-Mannheim/tesseract/wiki
> 
> 📁 Install to: `C:\Program Files\Tesseract-OCR\`
> 
> 💡 Or update the path in `python_backend/discord_username.py` if you install elsewhere

### 4️⃣ Python Dependencies
```cmd
pip install pytesseract pyautogui pyperclip pillow keyboard
```

## 🚀 Installation

### Step 1: Navigate to the app folder
```cmd
cd "discord bot/discord-welcome-app"
```

### Step 2: Install Node.js dependencies
```cmd
npm install
```

<div align="center">

✅ **Installation Complete!** You're ready to go!

</div>

## 🎮 How to Use

### 🟢 Start the app:
```cmd
npm start
```

### 📱 Open Discord and navigate to your welcome channel

### ⌨️ Hotkeys

<div align="center">

| Hotkey | Action | Description |
|--------|--------|-------------|
| `ALT + C` | 📸 **Capture** | Take screenshot and extract usernames |
| `ALT + X` | 📋 **Paste** | Paste all collected usernames with @ mentions |
| `CTRL + SHIFT + Q` | 🚪 **Quit** | Exit the program |

</div>

## 🔄 Workflow Example

```mermaid
graph LR
    A[👥 New Members Join] --> B[💬 Welcome Messages Appear]
    B --> C[⌨️ Press ALT + C]
    C --> D[🔍 Usernames Extracted]
    D --> E[🔁 Repeat for More]
    E --> F[⌨️ Press ALT + X]
    F --> G[✨ All Usernames Pasted!]
```

<div align="center">

### 📝 Example Output:
`@username1 @username2 @username3 @username4`

</div>

## ✨ Features

<table>
<tr>
<td width="50%">

### 🧠 Smart Username Filtering
Ignores common false positives like "supporter", "everyone", "app"

### 📁 Screenshot Management
Automatically keeps only the last 10 screenshots

</td>
<td width="50%">

### 🚫 Duplicate Prevention
Won't add the same username twice

### 📊 Real-time Logs
See what's happening in the Electron window

</td>
</tr>
</table>

## 📸 Screenshots Location

> 📁 Screenshots are saved to: `D:\TimePass\discord bot\user_screenshots\`

💡 **Tip:** You can change this path in `python_backend/discord_username.py` (line 18)

## 🔧 Troubleshooting

<details>
<summary>❌ App won't start</summary>

- ✅ Make sure Python is installed and in your PATH
- ✅ Verify Tesseract is installed at `C:\Program Files\Tesseract-OCR\`
- ✅ Check that all Python dependencies are installed

</details>

<details>
<summary>🔍 No usernames detected</summary>

- ✅ Make sure Discord is visible on screen when pressing `ALT + C`
- ✅ Try adjusting the crop area in `discord_username.py` if your Discord layout is different
- ✅ Ensure welcome messages are clearly visible

</details>

<details>
<summary>⌨️ Hotkeys not working</summary>

- ✅ Make sure the app is running
- ✅ Try running the app as administrator
- ✅ Check if another app is using the same hotkeys

</details>

## 📦 Building Executable

To create a standalone `.exe` file:

```cmd
npm run build
```

> 📂 The executable will be in the `dist` folder.

---

## 📝 Notes

> 💡 The app captures the screen area where Discord welcome messages typically appear
> 
> 🎨 Works best with Discord in light or dark mode with default layout
> 
> 💾 Usernames are stored in memory and cleared when you restart the app

---

<div align="center">

## 🤝 Contributing

Found a bug? Have a feature request? Feel free to open an issue!

## ⭐ Show Your Support

If this project helped you, give it a ⭐️!

---

### Made with ❤️ for Discord Communities

[![Discord](https://img.shields.io/badge/Discord-Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com)

---

## 📄 License

Free to use and modify for personal projects.

**Happy Welcoming! 🎉**

</div>
