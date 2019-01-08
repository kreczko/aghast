#!/usr/bin/env python

# Copyright (c) 2018, DIANA-HEP
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest

import numpy

from stagg import *

class Test(unittest.TestCase):
    def runTest(self):
        pass

    def test_binning_IntegerBinning(self):
        h = Histogram([Axis(IntegerBinning(10, 20))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(11))))
        assert h.axis[0].binning.toCategoryBinning().categories == ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        assert h.axis[0].binning.toRegularBinning().toCategoryBinning().categories == ["[9.5, 10.5)", "[10.5, 11.5)", "[11.5, 12.5)", "[12.5, 13.5)", "[13.5, 14.5)", "[14.5, 15.5)", "[15.5, 16.5)", "[16.5, 17.5)", "[17.5, 18.5)", "[18.5, 19.5)", "[19.5, 20.5)"]
        assert h.axis[0].binning.toEdgesBinning().toCategoryBinning().categories == ["[9.5, 10.5)", "[10.5, 11.5)", "[11.5, 12.5)", "[12.5, 13.5)", "[13.5, 14.5)", "[14.5, 15.5)", "[15.5, 16.5)", "[16.5, 17.5)", "[17.5, 18.5)", "[18.5, 19.5)", "[19.5, 20.5)"]
        assert h.axis[0].binning.toIrregularBinning().toCategoryBinning().categories == ["[9.5, 10.5)", "[10.5, 11.5)", "[11.5, 12.5)", "[12.5, 13.5)", "[13.5, 14.5)", "[14.5, 15.5)", "[15.5, 16.5)", "[16.5, 17.5)", "[17.5, 18.5)", "[18.5, 19.5)", "[19.5, 20.5)"]
        assert h.axis[0].binning.toSparseRegularBinning().toCategoryBinning().categories == ["[9.5, 10.5)", "[10.5, 11.5)", "[11.5, 12.5)", "[12.5, 13.5)", "[13.5, 14.5)", "[14.5, 15.5)", "[15.5, 16.5)", "[16.5, 17.5)", "[17.5, 18.5)", "[18.5, 19.5)", "[19.5, 20.5)"]

    def test_binning_RegularBinning(self):
        h = Histogram([Axis(RegularBinning(10, RealInterval(0.1, 10.1)))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(10))))
        assert h.axis[0].binning.toCategoryBinning().categories == ["[0.1, 1.1)", "[1.1, 2.1)", "[2.1, 3.1)", "[3.1, 4.1)", "[4.1, 5.1)", "[5.1, 6.1)", "[6.1, 7.1)", "[7.1, 8.1)", "[8.1, 9.1)", "[9.1, 10.1)"]
        assert h.axis[0].binning.toEdgesBinning().toCategoryBinning().categories == ["[0.1, 1.1)", "[1.1, 2.1)", "[2.1, 3.1)", "[3.1, 4.1)", "[4.1, 5.1)", "[5.1, 6.1)", "[6.1, 7.1)", "[7.1, 8.1)", "[8.1, 9.1)", "[9.1, 10.1)"]
        assert h.axis[0].binning.toIrregularBinning().toCategoryBinning().categories == ["[0.1, 1.1)", "[1.1, 2.1)", "[2.1, 3.1)", "[3.1, 4.1)", "[4.1, 5.1)", "[5.1, 6.1)", "[6.1, 7.1)", "[7.1, 8.1)", "[8.1, 9.1)", "[9.1, 10.1)"]
        assert h.axis[0].binning.toSparseRegularBinning().toCategoryBinning().categories == ["[0.1, 1.1)", "[1.1, 2.1)", "[2.1, 3.1)", "[3.1, 4.1)", "[4.1, 5.1)", "[5.1, 6.1)", "[6.1, 7.1)", "[7.1, 8.1)", "[8.1, 9.1)", "[9.1, 10.1)"]

        h = Histogram([Axis(RegularBinning(10, RealInterval(-0.9, 9.1)))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(10))))
        assert h.axis[0].binning.toCategoryBinning().categories == ["[-0.9, 0.1)", "[0.1, 1.1)", "[1.1, 2.1)", "[2.1, 3.1)", "[3.1, 4.1)", "[4.1, 5.1)", "[5.1, 6.1)", "[6.1, 7.1)", "[7.1, 8.1)", "[8.1, 9.1)"]
        assert h.axis[0].binning.toSparseRegularBinning().toCategoryBinning().categories == ["[-0.9, 0.1)", "[0.1, 1.1)", "[1.1, 2.1)", "[2.1, 3.1)", "[3.1, 4.1)", "[4.1, 5.1)", "[5.1, 6.1)", "[6.1, 7.1)", "[7.1, 8.1)", "[8.1, 9.1)"]

        h = Histogram([Axis(RegularBinning(10, RealInterval(-100, 100)))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(10))))
        assert h.axis[0].binning.toCategoryBinning().categories == ["[-100, -80)", "[-80, -60)", "[-60, -40)", "[-40, -20)", "[-20, 0)", "[0, 20)", "[20, 40)", "[40, 60)", "[60, 80)", "[80, 100)"]
        assert h.axis[0].binning.toEdgesBinning().toCategoryBinning().categories == ["[-100, -80)", "[-80, -60)", "[-60, -40)", "[-40, -20)", "[-20, 0)", "[0, 20)", "[20, 40)", "[40, 60)", "[60, 80)", "[80, 100)"]
        assert h.axis[0].binning.toIrregularBinning().toCategoryBinning().categories == ["[-100, -80)", "[-80, -60)", "[-60, -40)", "[-40, -20)", "[-20, 0)", "[0, 20)", "[20, 40)", "[40, 60)", "[60, 80)", "[80, 100)"]
        assert h.axis[0].binning.toSparseRegularBinning().toCategoryBinning().categories == ["[-100, -80)", "[-80, -60)", "[-60, -40)", "[-40, -20)", "[-20, 0)", "[0, 20)", "[20, 40)", "[40, 60)", "[60, 80)", "[80, 100)"]

    def test_binning_EdgesBinning(self):
        h = Histogram([Axis(EdgesBinning([3, 4.5, 10, 20]))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(5))))
        assert h.axis[0].binning.toCategoryBinning().categories == ["[3, 4.5)", "[4.5, 10)", "[10, 20)"]
        assert h.axis[0].binning.toIrregularBinning().toCategoryBinning().categories == ["[3, 4.5)", "[4.5, 10)", "[10, 20)"]

    def test_binning_IrregularBinning(self):
        h = Histogram([Axis(IrregularBinning([RealInterval(3, 4.5), RealInterval(4.5, 10), RealInterval(10, 20)]))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(5))))
        assert h.axis[0].binning.toCategoryBinning().categories == ["[3, 4.5)", "[4.5, 10)", "[10, 20)"]

    def test_binning_SparseRegularBinning(self):
        h = Histogram([Axis(SparseRegularBinning([-3, 6, 10, 11, 12], 10, 0.0))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(5))))
        assert h.axis[0].binning.toCategoryBinning().categories == ["[-30, -20)", "[60, 70)", "[100, 110)", "[110, 120)", "[120, 130)"]

        h = Histogram([Axis(SparseRegularBinning([-3, 6, 10, 11, 12], 10, 0.1))], UnweightedCounts(InterpretedInlineBuffer.fromarray(numpy.arange(5))))
        assert h.axis[0].binning.toCategoryBinning().categories == ["[-29.9, -19.9)", "[60.1, 70.1)", "[100.1, 110.1)", "[110.1, 120.1)", "[120.1, 130.1)"]
