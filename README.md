# Description
Simple python module (unofficial) allowing you to access data from rapiddns.io. You can also use it as an library.

As mentioned on the rapiddns.io:

*Rapiddns currently has more than 3 billion DNS resolution data, supporting A, CNAME, AAAA, MX types. A records 2.1 billion, CNAME records 250 million, AAAA records 103 million and MX records 510 million. Can query the domain name of the same IP website (support IPv6). You can also query subdomain information.*

![example](./screenshots/example1.png)

# Installation
```
git clone https://github.com/nullt3r/rapiddns
cd rapiddns
pip3 install .
```

If you can't run the rapiddns directly from command line you should check if $HOME/.local/bin is in your path.

Add the following line to your `~/.zshrc` or `~/.bashrc`:

```
export PATH="$HOME/.local/bin:$PATH"
```

# Usage
To extract subdomains:
```
rapiddns --subdomains twitter.com
```
To extract domains from IP or CIDR:
```
rapiddns --ip 8.8.8.8/24
```
You can also combine both options.

To display full output, use option --full.

# License
Read file LICENSE.

# Disclaimer
I am not responsible for any damages. You are responsible for your own
actions. Attacking targets without prior mutual consent is illegal.*