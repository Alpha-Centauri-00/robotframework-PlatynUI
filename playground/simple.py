import time

from PlatynUI.ui.runtime.core import dotnet_interface

print(dotnet_interface.DotNetInterface.finder().FindSingleNode(None, "/*", True))

dotnet_interface.DotNetInterface.mouse_device().Move(1,2)
pos = dotnet_interface.DotNetInterface.mouse_device().GetPosition()
print(pos)

print(dotnet_interface.DotNetInterface.display_device().GetBoundingRectangle())
dotnet_interface.DotNetInterface.display_device().HighlightRect(0,0,100,100)

time.sleep(5)
