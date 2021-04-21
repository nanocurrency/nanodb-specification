# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Nanodb(KaitaiStruct):

    class EnumBlocktype(Enum):
        invalid = 0
        not_a_block = 1
        send = 2
        receive = 3
        open = 4
        change = 5
        state = 6

    class MetaKey(Enum):
        version = 1

    class DatabaseVersion(Enum):
        value = 17

    class EnumEpoch(Enum):
        invalid = 0
        unspecified = 1
        epoch_0 = 2
        epoch_1 = 3
        epoch_2 = 4

    class EnumSignatureVerification(Enum):
        unknown = 0
        invalid = 1
        valid = 2
        valid_epoch = 3
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        pass

    class StateBlockSideband(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.successor = self._io.read_bytes(32)
            self.height = self._io.read_u8be()
            self.timestamp = self._io.read_u8be()
            self.is_send = self._io.read_bits_int(1) != 0
            self.is_receive = self._io.read_bits_int(1) != 0
            self.is_epoch = self._io.read_bits_int(1) != 0
            self.epoch = self._root.EnumEpoch(self._io.read_bits_int(5))


    class ReceiveKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hash = self._io.read_bytes(32)


    class BlockSend(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.previous = self._io.read_bytes(32)
            self.destination = self._io.read_bytes(32)
            self.balance = self._io.read_bytes(16)
            self.signature = self._io.read_bytes(64)
            self.work = self._io.read_u8le()


    class Unchecked(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.UncheckedKey(self._io, self, self._root)
            self.value = self._root.UncheckedValue(self._io, self, self._root)


    class StateBlocksKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hash = self._io.read_bytes(32)


    class MetaVersion(KaitaiStruct):
        """Value of key meta_key#version."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.database_version = self._io.read_bytes(32)


    class OpenKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hash = self._io.read_bytes(32)


    class VoteValue(KaitaiStruct):
        """Vote and block(s)."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.account = self._io.read_bytes(32)
            self.signature = self._io.read_bytes(64)
            self.sequence = self._io.read_u8le()
            self.block_type = self._root.EnumBlocktype(self._io.read_u1())
            if self.block_type == self._root.EnumBlocktype.not_a_block:
                self.votebyhash = self._root.VoteByHash(self._io, self, self._root)

            if self.block_type != self._root.EnumBlocktype.not_a_block:
                self.block = self._root.BlockSelector(self.block_type.value, self._io, self, self._root)



    class FrontiersKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hash = self._io.read_bytes(32)


    class BlockSelector(KaitaiStruct):
        """Selects a block based on the argument."""
        def __init__(self, arg_block_type, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.arg_block_type = arg_block_type
            self._read()

        def _read(self):
            _on = self.arg_block_type
            if _on == self._root.EnumBlocktype.open.value:
                self.block = self._root.BlockOpen(self._io, self, self._root)
            elif _on == self._root.EnumBlocktype.state.value:
                self.block = self._root.BlockState(self._io, self, self._root)
            elif _on == self._root.EnumBlocktype.receive.value:
                self.block = self._root.BlockReceive(self._io, self, self._root)
            elif _on == self._root.EnumBlocktype.send.value:
                self.block = self._root.BlockSend(self._io, self, self._root)
            elif _on == self._root.EnumBlocktype.change.value:
                self.block = self._root.BlockChange(self._io, self, self._root)
            else:
                self.block = self._root.IgnoreUntilEof(self._io, self, self._root)


    class BlockReceive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.previous = self._io.read_bytes(32)
            self.source = self._io.read_bytes(32)
            self.signature = self._io.read_bytes(64)
            self.work = self._io.read_u8le()


    class MetaKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._io.read_bytes(32)


    class BlockChange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.previous = self._io.read_bytes(32)
            self.representative = self._io.read_bytes(32)
            self.signature = self._io.read_bytes(64)
            self.work = self._io.read_u8le()


    class PendingKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.account = self._io.read_bytes(32)
            self.hash = self._io.read_bytes(32)


    class ChangeKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hash = self._io.read_bytes(32)


    class PendingValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.source = self._io.read_bytes(32)
            self.amount = self._io.read_bytes(16)
            self.epoch = self._root.EnumEpoch(self._io.read_u1())


    class VoteKey(KaitaiStruct):
        """Key of the vote table."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.account = self._io.read_bytes(32)


    class Receive(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.ReceiveKey(self._io, self, self._root)
            self.value = self._root.ReceiveValue(self._io, self, self._root)


    class AccountsKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.account = self._io.read_bytes(32)


    class Frontiers(KaitaiStruct):
        """Mapping from block hash to account. This is not used after epoch 1."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.FrontiersKey(self._io, self, self._root)
            self.value = self._root.FrontiersValue(self._io, self, self._root)


    class AccountsValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.head = self._io.read_bytes(32)
            self.representative = self._io.read_bytes(32)
            self.open_block = self._io.read_bytes(32)
            self.balance = self._io.read_bytes(16)
            self.modified = self._io.read_u8le()
            self.block_count = self._io.read_u8le()


    class OnlineWeightValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.amount = self._io.read_bytes(16)


    class FrontiersValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.account = self._io.read_bytes(32)


    class ReceiveValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block = self._root.BlockReceive(self._io, self, self._root)
            self.sideband = self._root.ReceiveSideband(self._io, self, self._root)


    class Open(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.OpenKey(self._io, self, self._root)
            self.value = self._root.OpenValue(self._io, self, self._root)


    class StateBlocksValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block = self._root.BlockState(self._io, self, self._root)
            self.sideband = self._root.StateBlockSideband(self._io, self, self._root)


    class VoteByHashEntry(KaitaiStruct):
        """The serialized hash in VBH is prepended by not_a_block."""
        def __init__(self, idx, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.idx = idx
            self._read()

        def _read(self):
            if self.idx > 0:
                self.block_type = self._root.EnumBlocktype(self._io.read_u1())

            self.block_hash = self._io.read_bytes(32)


    class BlockOpen(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.source = self._io.read_bytes(32)
            self.representative = self._io.read_bytes(32)
            self.account = self._io.read_bytes(32)
            self.signature = self._io.read_bytes(64)
            self.work = self._io.read_u8le()


    class IgnoreUntilEof(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if not (self._io.is_eof()):
                self.empty = []
                i = 0
                while True:
                    _ = self._io.read_u1()
                    self.empty.append(_)
                    if self._io.is_eof():
                        break
                    i += 1



    class Change(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.ChangeKey(self._io, self, self._root)
            self.value = self._root.ChangeValue(self._io, self, self._root)


    class StateBlocks(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.StateBlocksKey(self._io, self, self._root)
            self.value = self._root.StateBlocksValue(self._io, self, self._root)


    class SendValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block = self._root.BlockSend(self._io, self, self._root)
            self.sideband = self._root.SendSideband(self._io, self, self._root)


    class UncheckedKey(KaitaiStruct):
        """Key of the unchecked table."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.previous = self._io.read_bytes(32)
            self.hash = self._io.read_bytes(32)


    class OnlineWeightKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.timestamp = self._io.read_u8be()


    class ConfirmationHeight(KaitaiStruct):
        """Confirmed height per account."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.ConfirmationHeightKey(self._io, self, self._root)
            self.value = self._root.ConfirmationHeightValue(self._io, self, self._root)


    class ChangeSideband(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.successor = self._io.read_bytes(32)
            self.account = self._io.read_bytes(32)
            self.height = self._io.read_u8be()
            self.balance = self._io.read_bytes(16)
            self.timestamp = self._io.read_u8be()


    class OpenSideband(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.successor = self._io.read_bytes(32)
            self.balance = self._io.read_bytes(16)
            self.timestamp = self._io.read_u8be()


    class ConfirmationHeightKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.account = self._io.read_bytes(32)


    class ConfirmationHeightValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.height = self._io.read_u8le()
            self.frontier = self._io.read_bytes(32)


    class SendSideband(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.successor = self._io.read_bytes(32)
            self.account = self._io.read_bytes(32)
            self.height = self._io.read_u8be()
            self.timestamp = self._io.read_u8be()


    class BlockState(KaitaiStruct):
        """State block."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.account = self._io.read_bytes(32)
            self.previous = self._io.read_bytes(32)
            self.representative = self._io.read_bytes(32)
            self.balance = self._io.read_bytes(16)
            self.link = self._io.read_bytes(32)
            self.signature = self._io.read_bytes(64)
            self.work = self._io.read_u8be()


    class OpenValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block = self._root.BlockOpen(self._io, self, self._root)
            self.sideband = self._root.OpenSideband(self._io, self, self._root)


    class ReceiveSideband(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.successor = self._io.read_bytes(32)
            self.account = self._io.read_bytes(32)
            self.height = self._io.read_u8be()
            self.balance = self._io.read_bytes(16)
            self.timestamp = self._io.read_u8be()


    class ChangeValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block = self._root.BlockChange(self._io, self, self._root)
            self.sideband = self._root.ChangeSideband(self._io, self, self._root)


    class VoteByHash(KaitaiStruct):
        """A sequence of up to 12 hashes, terminated by EOF."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if not (self._io.is_eof()):
                self.hashes = []
                i = 0
                while True:
                    _ = self._root.VoteByHashEntry(i, self._io, self, self._root)
                    self.hashes.append(_)
                    if  ((i == 12) or (self._io.is_eof())) :
                        break
                    i += 1



    class Peers(KaitaiStruct):
        """Peer cache table. All data is stored in the key."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.address = self._io.read_bytes(16)
            self.port = self._io.read_u2be()


    class Vote(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.VoteKey(self._io, self, self._root)
            self.value = self._root.VoteValue(self._io, self, self._root)


    class Pending(KaitaiStruct):
        """Pending table."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.PendingKey(self._io, self, self._root)
            self.value = self._root.PendingValue(self._io, self, self._root)


    class SendKey(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hash = self._io.read_bytes(32)


    class Accounts(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.AccountsKey(self._io, self, self._root)
            self.value = self._root.AccountsValue(self._io, self, self._root)


    class UncheckedValue(KaitaiStruct):
        """Information about an unchecked block."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.block_type = self._root.EnumBlocktype(self._io.read_u1())
            self.block = self._root.BlockSelector(self.block_type.value, self._io, self, self._root)
            self.account = self._io.read_bytes(32)
            self.modified = self._io.read_u8le()
            self.verified = self._root.EnumSignatureVerification(self._io.read_u1())


    class OnlineWeight(KaitaiStruct):
        """Stores online weight trended over time."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.OnlineWeightKey(self._io, self, self._root)
            self.value = self._root.OnlineWeightValue(self._io, self, self._root)


    class Send(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key = self._root.SendKey(self._io, self, self._root)
            self.value = self._root.SendValue(self._io, self, self._root)
