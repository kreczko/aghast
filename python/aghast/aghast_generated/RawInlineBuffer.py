# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers

class RawInlineBuffer(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRawInlineBuffer(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RawInlineBuffer()
        x.Init(buf, n + offset)
        return x

    # RawInlineBuffer
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RawInlineBuffer
    def Buffer(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # RawInlineBuffer
    def BufferAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # RawInlineBuffer
    def BufferLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def RawInlineBufferStart(builder): builder.StartObject(1)
def RawInlineBufferAddBuffer(builder, buffer): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(buffer), 0)
def RawInlineBufferStartBufferVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def RawInlineBufferEnd(builder): return builder.EndObject()
