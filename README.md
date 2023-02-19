# Picen

<u>Pic</u>ture <u>en</u>cryption and decryption program, written in python.

## Algorithms

This program uses block ciphers to encrypt and decrypt images.<br>
The main algorithm is the OFB mode and AES-128 is used as the PRP.

## Setup

Install `pipenv`
```
$ pip install pipenv
```
Install dependencies
```
$ pipenv install
```
You can now run and use the program

## Usage

Here are the list of commands and their usages:

| Command | Usage                 | Description                       |
|:-------:|-----------------------|-----------------------------------|
|   gen   | gen \[options]        | generates a new random key        |
|   enc   | enc \<src> \[options] | encrypts the image at `src`       |
|   dec   | dec \<src> \[options] | decrypts the cipher text at `src` |
|   key   | key \[options]        | changes the global keys           |
