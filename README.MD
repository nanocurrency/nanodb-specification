# Overview

This repository contains a Kaitai Struct specification for the format of keys and values in the **Nano ledger database**, as well as a Python sample that uses the generated parser.

The wallet database is out of scope for this specification.

Please consider filing a ticket if you discover an issue with the specification or the generated code.

# Diagram

![Alt text](nanodb.png?raw=true "Nano")

# Python example

`read.py` is a sample Python script to demonstrate the generated Kaitai parser and help validate its coverage.

Install dependencies through `pip3 install -r requirements.txt`

The generated parser is included in the repository for convenience, but you can generate it yourself with `kaitai-struct-compiler -t python --outdir sample nanodb.ksy`

The example assumes *lmdb*, but should be easy to adapt to RocksDB as they share the key/value content format.

## Usage

**Only run this script on a database that is not currently in use by other processes**

Get help:

`python3 read.py -h`

Read 5 entries from every table, using data.ldb in the current directory

`python3 read.py --count 5`

Read from a specific data.ldb file, and only the vote table:

`python3 read.py --filename /my/nano/data.ldb --count 5 --table vote`

Lookup a state block with a specific hash using --key

`python3 read.py --count 1 --table state_blocks --key 57265474B5C38ED312259DC2E18DADE5C8C45763ECE51C274E2717E2FD688F8D`

## Sample output

A few examples:

`python3 read.py --count 1 --table accounts`

```
  head block     : AB957D79C4777B574647BDA3460D7D7A855F4F607F07EAFF6318FAFFC27A21EC
  open block     : 44F6918529FB5DC4C638512C4D81482D2121CAF142BED39FB6D44F6AB4AB244F
  balance        : 60523806000000000000000000000000
  block count    : 5
  last modified  : 2018-12-17 08:11:09
  representative : xrb_1stofnrxuz3cai7ze75o174bpm7scwj9jn3nxsn8ntzg784jf1gzn1jjdkou
```

Note that the sample script skips accounts with zero balance.

`python3 read.py --count 1 --table vote`
```
vote account      : xrb_13hhh1mukd8kywseuxhiiq5hwronoqbjqu5o4pneouxadtfig8tuw6hbt1f5
  signature       : E1B4FCF6234C9F171B18EEEA5E7A99EF40C1F5543BA33BA9AC6799458F9F889AC9244B1A5D29B05B29586AD57C88951DF3FD01CAAD0411DDAE4B7007FB8B310F
  sequence        : 38330158
  block type      : state
  account         : xrb_3owqgr1i6iqtot63yg1rhd3jgrmpz5bwz3348azbcxottjaeqacxpf9wtmqj
  representative  : xrb_3pczxuorp48td8645bs3m6c3xotxd3idskrenmi65rbrga5zmkemzhwkaznh
  previous        : A02AAFD01A6A7FE4D2212186066BBA20CCD4A57772ABD81E9C0E89584E052F48
  balance         : 2343000000000000000000000000000000
  link            : 234B680321669312851CBC45490BAA73251668F1897F8B873214D23BB97AA7CF
  link as account : xrb_1atdf13k4snm4c4jsh47b67tnws74snh54dzjg5m678k9gwqobyhbf43mbm6
  signature       : 8FD94851311E33CCE59341D2D62F39290337421C56AD2F1952D3E934DDDE4F35514D29764C3C822A1576E35DDDC40C5E7652F1F6E5043D1FD41F720ADF783E0A
  work            : 0x961ca14f47fcf532
```

Which is a vote for block https://nanocrawler.cc/explorer/block/9EBCD3A15832AA701E9832B2CC1DD96446B499F9C82548A6F5324FE556143D3E

`python3 read.py --count 1 --table pending`

```
key account       : 0000000000000000000000000000000000000000000000000000000000000000
key hash          : 00002E43956C771A6120EA21D7917F7349FD8BE9F5B01D2BDB89ACA3D5B220F0
  source          : nano_1hmqzugsmsn4jxtzo5yrm4rsysftkh9343363hctgrjch1984d8ey9zoyqex
  amount          : 2
  epoch           : epoch_1
```

`python3 read.py --count 1 --table state_blocks`

```
hash              : 0000026BF6EF2FAC78C9105CABA1E44FAF866548248E5D0926C6B6E0E5BFCDBA
  account         : nano_1gjku9ph9dtcfhs3x4xi9exxktdof14e8rwbk4qkztemjqbpfb6xheqknbp8
  representative  : nano_3dmtrrws3pocycmbqwawk6xs7446qxa36fcncush4s1pejk16ksbmakis78m
  previous        : 33DD2660E8AC2E0E283AB9162FC5AD88853EB26DF64439B1E7E92D1A0952C1C4
  balance         : 1671360722739128456642786434
  link            : 7180E432F07ABB020136631E029F88675346408A2C0803D16B78146701E62300
  link as account : nano_1we1wish1you1a1merry1christmas1and1a1happy1new1year14awbdw9b
  signature       : 37EED28CAF1169894D015340524B85299154C9A6B41A02D352B2B9662F0F1E2E7C340732E7B2F43C59AA000ED3690C99D3F63C0E628DDD20D759B02DEFF2EE0C
  work            : 0xe16c3225e275f088
  sideband:
    successor     : EC1D4FF78B272F97BF1B3FA0E3D6DE700FE30502475E0F7F24CA57D53909E217
    height        : 584542
    timestamp     : 2019-12-23 18:01:03
    epoch         : epoch_1
```

`python3 read.py --count 4 --table peers`

```
address     : ::ffff:5b79:7713
ipv4 mapped : 91.121.119.19
port        : 7075

address     : ::ffff:5e10:72eb
ipv4 mapped : 94.16.114.235
port        : 7075

address     : ::ffff:5e10:7a33
ipv4 mapped : 94.16.122.51
port        : 7075

address     : ::ffff:5eed:3920
ipv4 mapped : 94.237.57.32
port        : 7075
```

`python3 read.py --count 4 --table online_weight`

```
timestamp      : 2020-01-02 14:39:36.078484
online weight  : 96426874920614605364417680260758071281

timestamp      : 2020-01-02 14:44:37.230748
online weight  : 96812388601760176820534532978385899934

timestamp      : 2020-01-02 14:49:48.346698
online weight  : 96427874270863686929012362506644761248

timestamp      : 2020-01-05 04:21:51.079236
online weight  : 97683094289936149573532425682751217817
```

`python3 read.py --count 4 --table meta`

```
Database version:  16
```
