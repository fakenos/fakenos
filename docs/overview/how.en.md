# How?

Send input and get the output - this is how we interact with many Network Operating Systems, FakeNOS allows to pre-define the output to sent in response to certain input commands, making it ideal for isolated feature testing.

FakeNOS is a micro-kernel framework that has already a lot of network operating systems like Cisco IOS, Alcatel AOS or Huawei SmartAX and it can be extended using plugins. The core is kept small and optimized while most of the functionality offloaded to plugins.

!!! info
    If you want to see all the available platforms currently, look [here](../platforms.md).


!!! note
    This part below will be moved in the future.

Currently, FakeNOS has these pluggable systems:

- **NOS plugins:** plugins to simulate Network Operating System commands. This is where the commands and their responses are kept.
- **Server Plugins:** plugins responsible for running various servers to connect with. At the moment, it supports only `paramiko`.
- **Shell Plugins:** plugins to simulate command line interface shell. It parses and process the commands. It is the middleware between the server and the NOS.

``` mermaid
sequenceDiagram
Client->>Server: "show clock"
Server->>Shell: get "show clock"
Shell->>NOS: get "show clock"
NOS->>Shell: "show clock" response
Shell->>Server: "show clock" response
Server->>Client: "14:38:11.292 PST Tue Feb 10 2009"
```
