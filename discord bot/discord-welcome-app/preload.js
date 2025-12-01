const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld("electronAPI", {
    onPythonLog: (callback) => ipcRenderer.on('python-log', callback)
});


