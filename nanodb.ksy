# ----------------------------------------------------------------------
# Nano database definition
# ----------------------------------------------------------------------
meta:
  id: nanodb
  title: Nano Ledger Database Binary Format
  license: BSD 2-Clause
  endian: le

enums:

  # The database version covered by this specification
  database_version:
    17: value

  enum_blocktype:
    0x00: invalid
    0x01: not_a_block
    0x02: send
    0x03: receive
    0x04: open
    0x05: change
    0x06: state

  enum_epoch:
    0x00: invalid
    0x01: unspecified
    0x02: epoch_0
    0x03: epoch_1
    0x04: epoch_2

  enum_signature_verification:
    0x0: unknown
    0x1: invalid
    0x2: valid
    0x3: valid_epoch

  # Keys in the meta table. Note that keys are converted to 32-byte integers by the node.
  meta_key:
    1: version

types:

  # -------------------------------------------------------------------
  # Table: confirmation_height
  # -------------------------------------------------------------------
  confirmation_height:
    doc: Confirmed height per account
    seq:
      - id: key
        type: confirmation_height_key
      - id: value
        type: confirmation_height_value
  confirmation_height_key:
    seq:
      - id: account
        size: 32
  confirmation_height_value:
    seq:
      - id: height
        type: u8be
      - id: frontier
        size: 32
        doc: Hash of frontier block

  # -------------------------------------------------------------------
  # Table: frontiers
  # -------------------------------------------------------------------
  frontiers:
    doc: Mapping from block hash to account. This is not used after epoch 1.
    seq:
      - id: key
        type: frontiers_key
      - id: value
        type: frontiers_value        
  frontiers_key:
    seq:
      - id: hash
        size: 32
  frontiers_value:
    seq:
      - id: account
        size: 32

  # -------------------------------------------------------------------
  # Table: meta
  # Structure of value may depends on key in the future, hence a 
  # separate definition for each key (currently only version is used)
  # -------------------------------------------------------------------
  meta_key:
    seq:
      - id: key
        size: 32

  meta_version:
    doc: Value of key meta_key#version
    seq:
      - id: database_version
        size: 32
        doc: 32-byte big endian integer representing the database version

  # -------------------------------------------------------------------
  # Table: online_weight
  # -------------------------------------------------------------------
  online_weight:
    doc: Stores online weight trended over time
    seq:
      - id: key
        type: online_weight_key
      - id: value
        type: online_weight_value
  online_weight_key:
    seq:
      - id: timestamp
        type: u8be
        doc: Unix epoch
  online_weight_value:
    seq:
      - id: amount
        size: 16
        doc: 128 bit amount representing online weight at timestamp

  # -------------------------------------------------------------------
  # Table: peers
  # -------------------------------------------------------------------
  peers:
    doc: Peer cache table. All data is stored in the key.
    seq:
      - id: address
        doc: IPv6 address bytes, big endian
        size: 16
      - id: port
        doc: Port number, big endian
        type: u2be

  # -------------------------------------------------------------------
  # Table: pending
  # -------------------------------------------------------------------
  pending:
    doc: Pending table
    seq:
      - id: key
        type: pending_key
      - id: value
        type: pending_value

  pending_key:
    seq:
      - id: account
        size: 32
      - id: hash
        doc: Block hash
        size: 32

  pending_value:
    seq:
      - id: source
        doc: Source account
        size: 32
      - id: amount
        size: 16
      - id: epoch
        type: u1
        enum: enum_epoch

  # -------------------------------------------------------------------
  # Table: change
  # -------------------------------------------------------------------
  change:
    seq:
      - id: key
        type: change_key
      - id: value
        type: change_value
  change_key:
    seq:
      - id: hash
        size: 32
  change_value:
    seq:
      - id: block
        type: block_change
      - id: sideband
        type: change_sideband
  change_sideband:
    seq:
      - id: successor
        size: 32
        doc: Hash of successor block, if any
      - id: account
        size: 32
        doc: Public key to identify which account chain the block belongs to
      - id: height
        type: u8be
        doc: Block height, big endian
      - id: balance
        size: 16
        doc: 128 bit balance in raw
      - id: timestamp
        type: u8be
        doc: Unix epoch

  # -------------------------------------------------------------------
  # Table: open
  # -------------------------------------------------------------------
  open:
    seq:
      - id: key
        type: open_key
      - id: value
        type: open_value
  open_key:
    seq:
      - id: hash
        size: 32
  open_value:
    seq:
      - id: block
        type: block_open
      - id: sideband
        type: open_sideband
  open_sideband:
    seq:
      - id: successor
        size: 32
        doc: Hash of successor block, if any
      - id: balance
        size: 16
        doc: 128 bit balance in raw
      - id: timestamp
        type: u8be
        doc: Unix epoch, big endian

  # -------------------------------------------------------------------
  # Table: receive
  # -------------------------------------------------------------------
  receive:
    seq:
      - id: key
        type: receive_key
      - id: value
        type: receive_value
  receive_key:
    seq:
      - id: hash
        size: 32
  receive_value:
    seq:
      - id: block
        type: block_receive
      - id: sideband
        type: receive_sideband
  receive_sideband:
    seq:
      - id: successor
        size: 32
        doc: Hash of successor block, if any
      - id: account
        size: 32
        doc: Public key to identify which account chain the block belongs to
      - id: height
        type: u8be
        doc: Block height, big endian
      - id: balance
        size: 16
        doc: 128 bit balance in raw
      - id: timestamp
        type: u8be
        doc: Unix epoch, big endian

  # -------------------------------------------------------------------
  # Table: send
  # -------------------------------------------------------------------
  send:
    seq:
      - id: key
        type: send_key
      - id: value
        type: send_value
  send_key:
    seq:
      - id: hash
        size: 32
  send_value:
    seq:
      - id: block
        type: block_send
      - id: sideband
        type: send_sideband
  send_sideband:
    seq:
      - id: successor
        size: 32
        doc: Hash of successor block, if any
      - id: account
        size: 32
        doc: Public key to identify which account chain the block belongs to
      - id: height
        type: u8be
        doc: Block height, big endian
      - id: timestamp
        type: u8be
        doc: Unix epoch, big endian
    
  # -------------------------------------------------------------------
  # Table: state_blocks
  # -------------------------------------------------------------------
  state_blocks:
    seq:
      - id: key
        type: state_blocks_key
      - id: value
        type: state_blocks_value
  state_blocks_key:
    seq:
      - id: hash
        size: 32
  state_blocks_value:
    seq:
      - id: block
        type: block_state
      - id: sideband
        type: state_block_sideband
  state_block_sideband:
    seq:
      - id: successor
        size: 32
        doc: Hash of successor block, if any
      - id: height
        type: u8be
        doc: Block height, big endian
      - id: timestamp
        type: u8be
        doc: Unix epoch, big endian
      - id: epoch
        type: u1
        enum: enum_epoch
        doc: Which ledger epoch this block belongs to

  # -------------------------------------------------------------------
  # Table: unchecked
  # -------------------------------------------------------------------
  unchecked:
    seq:
      - id: key
        type: unchecked_key
      - id: value
        type: unchecked_value
  unchecked_key:
    doc: Key of the unchecked table
    seq:
      - id: previous
        size: 32
      - id: hash
        size: 32
  unchecked_value:
    doc: Information about an unchecked block
    seq:
      - id: block_type
        type: u1
        enum: enum_blocktype
      - id: block
        type: block_selector(block_type.to_i)
      - id: account
        size: 32
      - id: modified
        type: u8le
      - id: verified
        doc: Signature verification status
        type: u1
        enum: enum_signature_verification

  # -------------------------------------------------------------------
  # Table: vote  
  # -------------------------------------------------------------------
  vote:
    seq:
      - id: key
        type: vote_key
      - id: value
        type: vote_value

  vote_key:
    doc: Key of the vote table
    seq:
      - id: account
        size: 32
        doc: Public key

  vote_value:    
    doc: Vote and block(s)
    seq:
      - id: account
        size: 32
      - id: signature
        size: 64
      - id: sequence
        type: u8le
      - id: block_type
        type: u1
        enum: enum_blocktype
      - id: votebyhash
        if: block_type == enum_blocktype::not_a_block
        type: vote_by_hash
      - id: block
        if: block_type != enum_blocktype::not_a_block
        type: block_selector(block_type.to_i)

  vote_by_hash:
    doc: A sequence of up to 12 hashes, terminated by EOF.
    seq:
      - id: hashes
        type: vote_by_hash_entry(_index)
        repeat: until
        repeat-until: _index == 12 or _io.eof
        if: not _io.eof

  vote_by_hash_entry:
    doc: The serialized hash in VBH is prepended by not_a_block
    params:
      - id: idx
        type: u4
    seq:
      - id: block_type
        doc: Always enum_blocktype::not_a_block
        type: u1
        enum: enum_blocktype
        if: idx > 0
      - id: block_hash
        size: 32
  
  # -------------------------------------------------------------------
  # Table: accounts
  # -------------------------------------------------------------------  
  accounts:
    seq:
      - id: key
        type: accounts_key
      - id: value
        type: accounts_value

  accounts_key:
    seq:
      - id: account
        size: 32
        doc: Public key

  accounts_value:
    seq:
      - id: head
        size: 32
        doc: Hash of head block
      - id: representative
        size: 32
        doc: Public key of account representative
      - id: open_block
        size: 32
        doc: Hash of the open block for this account
      - id: balance
        size: 16
        doc: 128 bit balance in raw
      - id: modified
        type: u8le
        doc: Last account modification, in seconds since unix epoch
      - id: block_count
        type: u8le
        doc: Number of blocks on the account chain

  # -------------------------------------------------------------------
  # Block definitions
  # -------------------------------------------------------------------

  block_send:
    seq:
     - id: previous
       size: 32
       doc: Hash of the previous block
     - id: destination
       size: 32
       doc: Public key of destination account
     - id: balance
       size: 16
       doc: 128-bit big endian balance
     - id: signature
       size: 64
       doc: ed25519 signature
     - id: work
       type: u8le
       doc: Proof of work

  block_receive:
    seq:
     - id: previous
       size: 32
       doc: Hash of the previous block
     - id: source
       size: 32
       doc: Hash of the source send block
     - id: signature
       size: 64
       doc: ed25519 signature
     - id: work
       type: u8le
       doc: Proof of work

  block_open:
    seq:
     - id: source
       size: 32
       doc: Hash of the source send block
     - id: representative
       size: 32
       doc: Public key of initial representative account
     - id: account
       size: 32
       doc: Public key of account being opened
     - id: signature
       size: 64
       doc: ed25519 signature
     - id: work
       type: u8le
       doc: Proof of work

  block_change:
    seq:
     - id: previous
       size: 32
       doc: Hash of the previous block
     - id: representative
       size: 32
       doc: Public key of new representative account
     - id: signature
       size: 64
       doc: ed25519 signature
     - id: work
       type: u8le
       doc: Proof of work

  block_state:
    seq:
     - id: account
       size: 32
       doc: Public key of account represented by this state block
     - id: previous
       size: 32
       doc: Hash of previous block
     - id: representative
       size: 32
       doc: Public key of the representative account
     - id: balance
       size: 16
       doc: 128-bit big endian balance
     - id: link
       size: 32
       doc: Pairing send's block hash (open/receive), 0 (change) or destination public key (send)
     - id: signature
       size: 64
       doc: ed25519 signature
     - id: work
       type: u8be
       doc: Proof of work (big endian)
    doc: State block

  # The block selector takes an integer argument representing the block type.
  # Note that enum arguments are not yet supported in kaitai, hence the to_i casts.
  block_selector:
    doc: Selects a block based on the argument
    params:
      - id: arg_block_type
        type: u1
    seq:
      - id: block
        type:
          switch-on: arg_block_type
          cases:
            'enum_blocktype::send.to_i': block_send
            'enum_blocktype::receive.to_i': block_receive
            'enum_blocktype::open.to_i': block_open
            'enum_blocktype::change.to_i': block_change
            'enum_blocktype::state.to_i': block_state
            _: ignore_until_eof
 
  # Catch-all that ignores until eof
  ignore_until_eof:
    seq:
      - id: empty
        type: u1
        repeat: until
        repeat-until: _io.eof
        if: not _io.eof
