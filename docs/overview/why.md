# Why?

Testing is a crucial aspect of modern software engineering and therefore it is 
important in Network Automation. FakeNOS solves the problem of testing scripts
in a lightweight and easy to use manner. It allows to create a test environment
with multiple devices running different Network Operating Systems (NOS) in a
matter of minutes.

## Problem with integration testing
A crucial aspect of writing applications or scripts  for Network Automation is 
testing. Often testing is done using physical or virtual instances of network
appliances running certain version of Network Operating System (NOS). That
approach, while gives best integration results, in many cases carries a lot
of overhead to setup, run and tear down as well as putting significant burden
on compute and storage resource utilization.

As well, many times it happens that the vendor does not give access to the 
device for testing purposes or that you do not have the image to run in a 
virtual environment. In such cases, it is very difficult to test the application
or script that you have written.

As well, in case that we want to create a test environment with multiple devices
running different NOS, it is very difficult to setup and run such environment. Even 
though tools like [GNS3](https://www.gns3.com/) or [EVE-NG](https://www.eve-ng.net/)
exist, they are not always the best solution for testing purposes.

## Problem with Unit testing
Another approach is to mock underlying libraries methods to fool applications
under testing into believing that it is getting output from real devices. That
approach works very well for unit testing, but fails to simulate such aspects
as connection establishment and handling.

Also, the main problem with such approach is that you need to specify the output
for each command that you want to test. This is very time consuming and not always
the best solution.

## Our approach
FakeNOS positions itself somewhere in the middle between full integration testing
and testing that mocks device interactions. FakeNOS allows to create NOS plugins
to produce pre-defined output to test applications behavior while running servers 
to establish connections with.

It does so in a lightweight and easy to use manner. You can create a test environment
with multiple devices running different NOS in a matter of minutes. It is simply
a python library which spin up SSH server and fakes the output of the commands that
you specify.

!!! note

    In the current approach, the output is predefined and will always be the same
    and replies to the same exact command. There is on going effort to infer the
    commands (similar to ntc-templates) and make the output dynamic (using Jinja2).