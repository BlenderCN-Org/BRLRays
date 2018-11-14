--------------------------------------------
BRLRays: BRL-CAD Ray Trace Addon for Blender
--------------------------------------------


Aim
---
Using BRL-CAD library rt to provide mathematically accurate images, hoping
to create a CAD engine within Blender for ease of use.

Background
----------
A lightweight package that can help an engineer is greatly
appreciated.

BRL-CAD dose suffer, in my opinion, ease of use. The interface is not acceptable
in today's standers. Tcl/Tk and X display systems are classic. Instead of
continuing developing BRL-CAD's UI, why not integrate it into an existing package?

Blender is an artist tool, though, being open-source, you can make it do
what you want, if you have the life time. So I decided to make a renderer
for Blender to use it, POV-ray acts similar to what we are trying to achieve
and Lux Render have a great way to port it.

Wish me luck in finishing my milestone!

Current work:
-------------
Porting Mitsuba (mtsblend) -like project to act for BRL-CAD.

Installation Instructions:
--------------------------

Copy the 'BRLRays' folder into Blender scripts/addons directory and
then enable BRLRays addon on 'Addons > Render' section of Blender
'User Preferences' panel.

After enabling the addon, configure the 'Path to BRL-CAD Installation'
setting that appears under BRLRays addon on the same 'User Preferences'
panel by selecting the folder where BRL-CAD binary is installed (usually at
/usr/brlcad/bin).
