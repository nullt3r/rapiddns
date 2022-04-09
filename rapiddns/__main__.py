import argparse

from rapiddns import RapidDns

def main():
    from rapiddns import __version__

    parser = argparse.ArgumentParser(description=f"rapiddns v{__version__.__version__} - a simple python client for rapiddns.io by @nullt3r")

    parser.add_argument(
        "--subdomains",
        "-s",
        action="store",
        help="expecting a domain name",
        required=False,
    )
    parser.add_argument(
        "--ip",
        action="store",
        help="expecting an IP adress or CIDR",
        required=False,
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="full output with detailed information",
        required=False,
    )

    args = parser.parse_args()

    arg_subdomains = args.subdomains
    arg_ip = args.ip
    arg_full = args.full

    if (arg_subdomains or arg_ip) is None:
        parser.error('parameter --subdomains or --ip is required. You can specify both.')

    if arg_subdomains is not None:
        if arg_full is True:
            for line in RapidDns.subdomains(arg_subdomains):
                print(" ".join(line))
        else:
            subdomains = [resource[0] for resource in RapidDns.subdomains(arg_subdomains)]
            print("\n".join(set(subdomains)))

    if arg_ip is not None:
        if arg_full is True:
            for line in RapidDns.sameip(arg_ip):
                print(" ".join(line))
        else:
            domains = [resource[0] for resource in RapidDns.sameip(arg_ip)]
            print("\n".join(set(domains)))

if __name__ == "__main__":
    main()