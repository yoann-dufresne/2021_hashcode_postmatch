#!/usr/bin/env python3

import sys

from Problem import Problem


def parse_problem():
	pb = Problem()
	pb.parse_from_stream(sys.stdin)


def main():
	pb = parse_problem()



if __name__ == "__main__":
	main()
