#
# @file    TestSBMLConvertStrict.py
# @brief   SBMLConvert unit tests for strict conversion
#
# @author  Akiya Jouraku (Python conversion)
# @author  Sarah Keating
 
# 
# ====== WARNING ===== WARNING ===== WARNING ===== WARNING ===== WARNING ======
#
# DO NOT EDIT THIS FILE.
#
# This file was generated automatically by converting the file located at
# src/sbml/test/TestSBMLConvertStrict.c
# using the conversion program dev/utilities/translateTests/translateTests.pl.
# Any changes made here will be lost the next time the file is regenerated.
#
# -----------------------------------------------------------------------------
# This file is part of libSBML.  Please visit http://sbml.org for more
# information about SBML, and the latest version of libSBML.
#
# Copyright 2005-2010 California Institute of Technology.
# Copyright 2002-2005 California Institute of Technology and
#                     Japan Science and Technology Corporation.
# 
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation.  A copy of the license agreement is provided
# in the file named "LICENSE.txt" included with this software distribution
# and also available online as http://sbml.org/software/libsbml/license.html
# -----------------------------------------------------------------------------

import sys
import unittest
import libsbml


class TestSBMLConvertStrict(unittest.TestCase):


  def test_SBMLConvertStrict_convertL1ParamRule(self):
    d = libsbml.SBMLDocument(1,2)
    m = d.createModel()
    c = m.createCompartment()
    c.setId( "c")
    p = m.createParameter()
    p.setId( "p")
    p1 = m.createParameter()
    p1.setId( "p1")
    math = libsbml.parseFormula("p")
    ar = m.createAssignmentRule()
    ar.setVariable( "p1")
    ar.setMath(math)
    ar.setUnits( "mole")
    self.assert_( d.setLevelAndVersion(2,1,True) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 1 )
    r1 = d.getModel().getRule(0)
    self.assert_( r1.getUnits() == "" )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvertStrict_convertNonStrictSBO(self):
    d = libsbml.SBMLDocument(2,4)
    m = d.createModel()
    c = m.createCompartment()
    c.setId( "c")
    c.setConstant(False)
    (c).setSBOTerm(64)
    self.assert_( d.setLevelAndVersion(2,3,True) == False )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 4 )
    self.assert_( d.setLevelAndVersion(2,2,True) == False )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 4 )
    self.assert_( d.setLevelAndVersion(2,1,True) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 1 )
    c1 = d.getModel().getCompartment(0)
    self.assert_( (c1).getSBOTerm() == -1 )
    self.assert_( d.setLevelAndVersion(1,2,True) == True )
    self.assert_( d.getLevel() == 1 )
    self.assert_( d.getVersion() == 2 )
    c2 = d.getModel().getCompartment(0)
    self.assert_( (c2).getSBOTerm() == -1 )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvertStrict_convertNonStrictUnits(self):
    d = libsbml.SBMLDocument(2,4)
    m = d.createModel()
    c = m.createCompartment()
    c.setId( "c")
    c.setConstant(False)
    p = m.createParameter()
    p.setId( "p")
    p.setUnits( "mole")
    math = libsbml.parseFormula("p")
    ar = m.createAssignmentRule()
    ar.setVariable( "c")
    ar.setMath(math)
    self.assert_( d.setLevelAndVersion(2,1,True) == False )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 4 )
    self.assert_( d.setLevelAndVersion(2,2,True) == False )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 4 )
    self.assert_( d.setLevelAndVersion(2,3,True) == False )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 4 )
    self.assert_( d.setLevelAndVersion(1,2,True) == False )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 4 )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvertStrict_convertSBO(self):
    d = libsbml.SBMLDocument(2,4)
    m = d.createModel()
    c = m.createCompartment()
    c.setId( "c")
    (c).setSBOTerm(240)
    self.assert_( d.setLevelAndVersion(2,3,True) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 3 )
    self.assert_( d.setLevelAndVersion(2,2,True) == True )
    self.assert_( d.getLevel() == 2 )
    self.assert_( d.getVersion() == 2 )
    c1 = d.getModel().getCompartment(0)
    self.assert_( (c1).getSBOTerm() == -1 )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

  def test_SBMLConvertStrict_convertToL1(self):
    d = libsbml.SBMLDocument(2,4)
    m = d.createModel()
    (m).setMetaId( "_m")
    c = m.createCompartment()
    c.setId( "c")
    (c).setSBOTerm(240)
    s = m.createSpecies()
    s.setId( "s")
    s.setCompartment( "c")
    self.assert_( d.setLevelAndVersion(1,2,True) == True )
    self.assert_( d.getLevel() == 1 )
    self.assert_( d.getVersion() == 2 )
    m1 = d.getModel()
    self.assert_( (m1).getMetaId() == "" )
    c1 = m1.getCompartment(0)
    self.assert_( (c1).getSBOTerm() == -1 )
    s1 = m1.getSpecies(0)
    self.assert_( s1.getHasOnlySubstanceUnits() == False )
    _dummyList = [ d ]; _dummyList[:] = []; del _dummyList
    pass  

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestSBMLConvertStrict))

  return suite

if __name__ == "__main__":
  if unittest.TextTestRunner(verbosity=1).run(suite()).wasSuccessful() :
    sys.exit(0)
  else:
    sys.exit(1)

