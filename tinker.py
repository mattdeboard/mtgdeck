#!/usr/bin/env python3
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import ipdb

def main():
  cards = Card.where(page=1).where(pageSize=5).all()
  return cards


if __name__ == "__main__":
  main()