# What not?

FakeNOS is a simulator. It does not emulate any network control, data, or management planes; it takes commands as input and responds with predefined output. Although there are plans to add some dynamic output, there are no plans to emulate the underlying protocol behavior.

In case you are looking for a network emulator which do emulate the underlying protocols like BGP, LLDP, etc here are some which you may find interesting:

-  [GNS3](https://www.gns3.com/)
-  [EVE-NG](https://www.eve-ng.net/)
-  [Cisco Packet Tracer](https://www.netacad.com/es/courses/packet-tracer)

The idea of this library is that it can be embedded in automated software that interact with network equipment, emulating the behavior in a high level.
