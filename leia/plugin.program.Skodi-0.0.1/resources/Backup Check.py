<<<<<<< HEAD
#kick off the Kodi backup
Kodi.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Addons.ExecuteAddon","params":{"addonid":"script.xbmcbackup","params":{"mode":"backup"}}, "id": 1 }')

#sleep for a few seconds to give it time to kick off
Kodi.sleep(10000)

window = Kodigui.Window(10000)

while (window.getProperty('script.xbmcbackup.running') == 'true'):
     #do something here, probably just sleep for a few seconds
     Kodi.sleep(5000)

=======
#kick off the Kodi backup
Kodi.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Addons.ExecuteAddon","params":{"addonid":"script.xbmcbackup","params":{"mode":"backup"}}, "id": 1 }')

#sleep for a few seconds to give it time to kick off
Kodi.sleep(10000)

window = Kodigui.Window(10000)

while (window.getProperty('script.xbmcbackup.running') == 'true'):
     #do something here, probably just sleep for a few seconds
     Kodi.sleep(5000)

>>>>>>> ae015f14fa26bfbc816a3b195d7f8308e35e6511
#backup is now done, continue with script