import xbmc
xbmc.executebuiltin('RunPlugin("plugin.program.Skodi/?action=hk2AH2")')
xbmc.sleep(100)
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"lookandfeel.skin","value":"skin.estuary"}}')
xbmc.sleep(100)
xbmc.executebuiltin('SendClick(11)')
xbmc.sleep(100)
xbmc.executebuiltin('System.Logoff()')
xbmc.sleep(100)
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"lookandfeel.skin","value":"skin.arctic.horizon.2"}}')
xbmc.sleep(100)
xbmc.executebuiltin('SendClick(11)')