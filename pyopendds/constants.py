import enum

class SampleState(enum.IntFlag):
  READ = 0x0001
  NOT_READ = 0x0010
  ANY = 0xFFFF

class ViewState(enum.IntFlag):
  NEW = 0x0001
  NOT_NEW = 0x0010
  ANY = 0xFFFF

class InstanceState(enum.IntFlag):
  ALIVE = 0x0001
  NOT_ALIVE_DISPOSED = 0x0010
  NOT_ALIVE_NO_WRITERS = 0x0100
  NOT_ALIVE = 0x0006
  ANY = 0xFFFF

class ReturnCode(enum.IntEnum):
  OK = 0
  ERROR = 1
  UNSUPPORTED = 2
  BAD_PARAMETER = 3
  PRECONDITION_NOT_MET = 4
  OUT_OF_RESOURCES = 5
  NOT_ENABLED = 6
  IMMUTABLE_POLICY = 7
  INCONSISTENT_POLICY = 8
  ALREADY_DELETED = 9
  TIMEOUT = 10
  NO_DATA = 11
  ILLEGAL_OPERATION = 12

class StatusKind(enum.IntFlag):
  INCONSISTENT_TOPIC = 1
  OFFERED_DEADLINE_MISSED = 2
  REQUESTED_DEADLINE_MISSED = 4
  OFFERED_INCOMPATIBLE_QOS = 32
  REQUESTED_INCOMPATIBLE_QOS = 64
  SAMPLE_LOST = 128
  SAMPLE_REJECTED = 256
  DATA_ON_READERS = 512
  DATA_AVAILABLE = 1024
  LIVELINESS_LOST = 2048
  LIVELINESS_CHANGED = 4096
  PUBLICATION_MATCHED = 8192
  SUBSCRIPTION_MATCHED = 16384
