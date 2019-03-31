# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers

class InterpretedInlineBuffer(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsInterpretedInlineBuffer(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InterpretedInlineBuffer()
        x.Init(buf, n + offset)
        return x

    # InterpretedInlineBuffer
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # InterpretedInlineBuffer
    def Buffer(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # InterpretedInlineBuffer
    def BufferAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # InterpretedInlineBuffer
    def BufferLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # InterpretedInlineBuffer
    def Filters(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # InterpretedInlineBuffer
    def FiltersAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # InterpretedInlineBuffer
    def FiltersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # InterpretedInlineBuffer
    def PostfilterSlice(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .Slice import Slice
            obj = Slice()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # InterpretedInlineBuffer
    def Dtype(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # InterpretedInlineBuffer
    def Endianness(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # InterpretedInlineBuffer
    def DimensionOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def InterpretedInlineBufferStart(builder): builder.StartObject(6)
def InterpretedInlineBufferAddBuffer(builder, buffer): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(buffer), 0)
def InterpretedInlineBufferStartBufferVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def InterpretedInlineBufferAddFilters(builder, filters): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(filters), 0)
def InterpretedInlineBufferStartFiltersVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def InterpretedInlineBufferAddPostfilterSlice(builder, postfilterSlice): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(postfilterSlice), 0)
def InterpretedInlineBufferAddDtype(builder, dtype): builder.PrependInt8Slot(3, dtype, 0)
def InterpretedInlineBufferAddEndianness(builder, endianness): builder.PrependInt8Slot(4, endianness, 0)
def InterpretedInlineBufferAddDimensionOrder(builder, dimensionOrder): builder.PrependInt8Slot(5, dimensionOrder, 0)
def InterpretedInlineBufferEnd(builder): return builder.EndObject()