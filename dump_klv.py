#!/usr/bin/env python
import argparse
import klvdata

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--source", type=str, required=True, help="source video file or stream")
	args = parser.parse_args()

	with open(args.source, 'rb') as f:
		for packet in klvdata.StreamParser(f):
			packet.structure()
