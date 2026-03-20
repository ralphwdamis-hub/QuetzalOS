const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('electronAPI', {
  sendCommand: (cmd) => ipcRenderer.send('terminal-command', cmd),
  onOutput: (callback) => ipcRenderer.on('terminal-output', (event, data) => callback(data)),
})
