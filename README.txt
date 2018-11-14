BRL_CAD Ray Trace Addon for Blender
-----------------------------------

Using BRL-CAD library rt to provide mathematically accurate images, hoping
to create a CAD engine within Blender for it's ease of use.

Engineers, after they graduate, may face a problem of expensive tools
to do their job, in terms of cost of machines and software(s). Being honest,
without computers we are as effective as if we were in the 1900s.
Thereby, a lightweight package that can help an engineer is greatly
appreciated.

BRL-CAD claim to be a CAD software used in the 1980s to provide analysis of
different machines. However, knowing the computation constrains back then, it
was well optimized. So using modern computers may work even as the old
workstation.
It dose suffer, in my opinion, ease of use. The interface is not acceptable
in today's standers. Tcl/Tk and X display systems are classic, thou developed
for CAD use.. I could not get my head through it. Instead of continuing
developing BRL-CAD's UI, why not integrate it into an existing package?

Blender is an artist tool, though, being open-source, you can make it do
what you want, if you have the life time. So I decided to make a renderer
for Blender to use it, POV-ray acts similar to what we are trying to achieve
and Lux Render have a great way to port it.

Wish me luck in finishing my milestone!

Installation Instructions:
--------------------------

Copy the 'BRLRays' folder into Blender scripts/addons directory and
then enable BRLRays addon on 'Addons > Render' section of Blender
'User Preferences' panel.

After enabling the addon, configure the 'Path to BRL-CAD Installation'
setting that appears under BRLRays addon on the same 'User Preferences'
panel by selecting the folder where BRL-CAD binary is installed (usually at
/usr/brlcad/bin).
