const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

let pythonBot;

function createWindow() {
    const win = new BrowserWindow({
        width: 900,
        height: 600,
        icon: path.join(__dirname, 'icon.ico'),  // your anime icon
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    });

    win.loadFile('renderer/index.html');

    // Start Python backend with unbuffered output
    pythonBot = spawn('python', ['-u', 'python_backend/discord_username.py']);

    pythonBot.stdout.on('data', (data) => {
        const output = data.toString();
        console.log(`PYTHON: ${output}`);
        win.webContents.send('python-log', output);
    });

    pythonBot.stderr.on('data', (data) => {
        const error = data.toString();
        console.error(`PYTHON ERROR: ${error}`);
        win.webContents.send('python-log', `ERROR: ${error}`);
    });

    pythonBot.on('close', (code) => {
        console.log(`Python bot stopped with code ${code}`);
    });

    pythonBot.on('error', (err) => {
        console.error('Failed to start Python process:', err);
    });
}

app.whenReady().then(() => {
    createWindow();
});
