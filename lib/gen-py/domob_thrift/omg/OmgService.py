# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface(object):
  def test(self, id):
    """
    Parameters:
     - id: 测试
    """
    pass

  def generatePoem(self, title, tags, description):
    """
    根据用户输入生成诗词

    Parameters:
     - title: 生成诗词标题
     - tags: 图片标签
     - description: 图片描述
    """
    pass

  def searchCreativeTexts(self, tags, description):
    """
    根据用户输入检索文案

    Parameters:
     - tags: 图片标签
     - description: 图片描述
    """
    pass

  def analyzeImage(self, data_type, image_data, language):
    """
    根据输入的图片url/data/文件目录，对图片进行解析并返回tags和descriptions

    Parameters:
     - data_type: 图片数据类型
     - image_data: 图片数据
     - language
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot != None:
      self._oprot = oprot
    self._seqid = 0

  def test(self, id):
    """
    Parameters:
     - id: 测试
    """
    self.send_test(id)
    return self.recv_test()

  def send_test(self, id):
    self._oprot.writeMessageBegin('test', TMessageType.CALL, self._seqid)
    args = test_args()
    args.id = id
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_test(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = test_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success != None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "test failed: unknown result");

  def generatePoem(self, title, tags, description):
    """
    根据用户输入生成诗词

    Parameters:
     - title: 生成诗词标题
     - tags: 图片标签
     - description: 图片描述
    """
    self.send_generatePoem(title, tags, description)
    return self.recv_generatePoem()

  def send_generatePoem(self, title, tags, description):
    self._oprot.writeMessageBegin('generatePoem', TMessageType.CALL, self._seqid)
    args = generatePoem_args()
    args.title = title
    args.tags = tags
    args.description = description
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_generatePoem(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = generatePoem_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success != None:
      return result.success
    if result.e != None:
      raise result.e
    raise TApplicationException(TApplicationException.MISSING_RESULT, "generatePoem failed: unknown result");

  def searchCreativeTexts(self, tags, description):
    """
    根据用户输入检索文案

    Parameters:
     - tags: 图片标签
     - description: 图片描述
    """
    self.send_searchCreativeTexts(tags, description)
    return self.recv_searchCreativeTexts()

  def send_searchCreativeTexts(self, tags, description):
    self._oprot.writeMessageBegin('searchCreativeTexts', TMessageType.CALL, self._seqid)
    args = searchCreativeTexts_args()
    args.tags = tags
    args.description = description
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_searchCreativeTexts(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = searchCreativeTexts_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success != None:
      return result.success
    if result.e != None:
      raise result.e
    raise TApplicationException(TApplicationException.MISSING_RESULT, "searchCreativeTexts failed: unknown result");

  def analyzeImage(self, data_type, image_data, language):
    """
    根据输入的图片url/data/文件目录，对图片进行解析并返回tags和descriptions

    Parameters:
     - data_type: 图片数据类型
     - image_data: 图片数据
     - language
    """
    self.send_analyzeImage(data_type, image_data, language)
    return self.recv_analyzeImage()

  def send_analyzeImage(self, data_type, image_data, language):
    self._oprot.writeMessageBegin('analyzeImage', TMessageType.CALL, self._seqid)
    args = analyzeImage_args()
    args.data_type = data_type
    args.image_data = image_data
    args.language = language
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_analyzeImage(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = analyzeImage_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success != None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "analyzeImage failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["test"] = Processor.process_test
    self._processMap["generatePoem"] = Processor.process_generatePoem
    self._processMap["searchCreativeTexts"] = Processor.process_searchCreativeTexts
    self._processMap["analyzeImage"] = Processor.process_analyzeImage

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_test(self, seqid, iprot, oprot):
    args = test_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = test_result()
    result.success = self._handler.test(args.id)
    oprot.writeMessageBegin("test", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_generatePoem(self, seqid, iprot, oprot):
    args = generatePoem_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = generatePoem_result()
    try:
      result.success = self._handler.generatePoem(args.title, args.tags, args.description)
    except domob_thrift.omg_common.ttypes.OmgException, e:
      result.e = e
    oprot.writeMessageBegin("generatePoem", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_searchCreativeTexts(self, seqid, iprot, oprot):
    args = searchCreativeTexts_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = searchCreativeTexts_result()
    try:
      result.success = self._handler.searchCreativeTexts(args.tags, args.description)
    except domob_thrift.omg_common.ttypes.OmgException, e:
      result.e = e
    oprot.writeMessageBegin("searchCreativeTexts", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_analyzeImage(self, seqid, iprot, oprot):
    args = analyzeImage_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = analyzeImage_result()
    result.success = self._handler.analyzeImage(args.data_type, args.image_data, args.language)
    oprot.writeMessageBegin("analyzeImage", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class test_args(object):
  """
  Attributes:
   - id: 测试
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
  )

  def __init__(self, id=None,):
    self.id = id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.id = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('test_args')
    if self.id != None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class test_result(object):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (domob_thrift.omg_types.ttypes.Test, domob_thrift.omg_types.ttypes.Test.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = domob_thrift.omg_types.ttypes.Test()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('test_result')
    if self.success != None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class generatePoem_args(object):
  """
  Attributes:
   - title: 生成诗词标题
   - tags: 图片标签
   - description: 图片描述
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'title', None, None, ), # 1
    (2, TType.LIST, 'tags', (TType.STRUCT,(domob_thrift.omg_types.ttypes.ImageTag, domob_thrift.omg_types.ttypes.ImageTag.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'description', (TType.STRING,None), None, ), # 3
  )

  def __init__(self, title=None, tags=None, description=None,):
    self.title = title
    self.tags = tags
    self.description = description

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.title = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.tags = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = domob_thrift.omg_types.ttypes.ImageTag()
            _elem5.read(iprot)
            self.tags.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.description = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readString();
            self.description.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('generatePoem_args')
    if self.title != None:
      oprot.writeFieldBegin('title', TType.STRING, 1)
      oprot.writeString(self.title)
      oprot.writeFieldEnd()
    if self.tags != None:
      oprot.writeFieldBegin('tags', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.tags))
      for iter12 in self.tags:
        iter12.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.description != None:
      oprot.writeFieldBegin('description', TType.LIST, 3)
      oprot.writeListBegin(TType.STRING, len(self.description))
      for iter13 in self.description:
        oprot.writeString(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class generatePoem_result(object):
  """
  Attributes:
   - success
   - e
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
    (1, TType.STRUCT, 'e', (domob_thrift.omg_common.ttypes.OmgException, domob_thrift.omg_common.ttypes.OmgException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, e=None,):
    self.success = success
    self.e = e

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = domob_thrift.omg_common.ttypes.OmgException()
          self.e.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('generatePoem_result')
    if self.success != None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    if self.e != None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class searchCreativeTexts_args(object):
  """
  Attributes:
   - tags: 图片标签
   - description: 图片描述
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'tags', (TType.STRING,None), None, ), # 1
    (2, TType.LIST, 'description', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, tags=None, description=None,):
    self.tags = tags
    self.description = description

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.tags = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = iprot.readString();
            self.tags.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.description = []
          (_etype23, _size20) = iprot.readListBegin()
          for _i24 in xrange(_size20):
            _elem25 = iprot.readString();
            self.description.append(_elem25)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('searchCreativeTexts_args')
    if self.tags != None:
      oprot.writeFieldBegin('tags', TType.LIST, 1)
      oprot.writeListBegin(TType.STRING, len(self.tags))
      for iter26 in self.tags:
        oprot.writeString(iter26)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.description != None:
      oprot.writeFieldBegin('description', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.description))
      for iter27 in self.description:
        oprot.writeString(iter27)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class searchCreativeTexts_result(object):
  """
  Attributes:
   - success
   - e
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING,None), None, ), # 0
    (1, TType.STRUCT, 'e', (domob_thrift.omg_common.ttypes.OmgException, domob_thrift.omg_common.ttypes.OmgException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, e=None,):
    self.success = success
    self.e = e

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype31, _size28) = iprot.readListBegin()
          for _i32 in xrange(_size28):
            _elem33 = iprot.readString();
            self.success.append(_elem33)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.e = domob_thrift.omg_common.ttypes.OmgException()
          self.e.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('searchCreativeTexts_result')
    if self.success != None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRING, len(self.success))
      for iter34 in self.success:
        oprot.writeString(iter34)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.e != None:
      oprot.writeFieldBegin('e', TType.STRUCT, 1)
      self.e.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class analyzeImage_args(object):
  """
  Attributes:
   - data_type: 图片数据类型
   - image_data: 图片数据
   - language
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'data_type', None, None, ), # 1
    (2, TType.STRUCT, 'image_data', (domob_thrift.omg_types.ttypes.ImageData, domob_thrift.omg_types.ttypes.ImageData.thrift_spec), None, ), # 2
    (3, TType.I32, 'language', None, None, ), # 3
  )

  def __init__(self, data_type=None, image_data=None, language=None,):
    self.data_type = data_type
    self.image_data = image_data
    self.language = language

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.data_type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.image_data = domob_thrift.omg_types.ttypes.ImageData()
          self.image_data.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.language = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('analyzeImage_args')
    if self.data_type != None:
      oprot.writeFieldBegin('data_type', TType.I32, 1)
      oprot.writeI32(self.data_type)
      oprot.writeFieldEnd()
    if self.image_data != None:
      oprot.writeFieldBegin('image_data', TType.STRUCT, 2)
      self.image_data.write(oprot)
      oprot.writeFieldEnd()
    if self.language != None:
      oprot.writeFieldBegin('language', TType.I32, 3)
      oprot.writeI32(self.language)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class analyzeImage_result(object):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (domob_thrift.omg_types.ttypes.ImageAnalyzeResult, domob_thrift.omg_types.ttypes.ImageAnalyzeResult.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = domob_thrift.omg_types.ttypes.ImageAnalyzeResult()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('analyzeImage_result')
    if self.success != None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
