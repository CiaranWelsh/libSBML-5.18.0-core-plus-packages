using System;
using System.Runtime.InteropServices;
 
//------------------------------------------------------------------------------
// <auto-generated />
//
// This file was automatically generated by SWIG (http://www.swig.org).
// Version 3.0.12
//
// Do not make changes to this file unless you know what you are doing--modify
// the SWIG interface file instead.
//------------------------------------------------------------------------------

namespace libsbmlcs {

public class XMLOwningOutputFileStream : global::System.IDisposable {
	private HandleRef swigCPtr;
	protected bool swigCMemOwn;
	
	internal XMLOwningOutputFileStream(IntPtr cPtr, bool cMemoryOwn)
	{
		swigCMemOwn = cMemoryOwn;
		swigCPtr    = new HandleRef(this, cPtr);
	}
	
	internal static HandleRef getCPtr(XMLOwningOutputFileStream obj)
	{
		return (obj == null) ? new HandleRef(null, IntPtr.Zero) : obj.swigCPtr;
	}
	
	internal static HandleRef getCPtrAndDisown (XMLOwningOutputFileStream obj)
	{
		HandleRef ptr = new HandleRef(null, IntPtr.Zero);
		
		if (obj != null)
		{
			ptr             = obj.swigCPtr;
			obj.swigCMemOwn = false;
		}
		
		return ptr;
	}

  ~XMLOwningOutputFileStream() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != global::System.IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          libsbmlPINVOKE.delete_XMLOwningOutputFileStream(swigCPtr);
        }
        swigCPtr = new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero);
      }
      global::System.GC.SuppressFinalize(this);
    }
  }

  
/** */ /* libsbml-internal */ public
 XMLOwningOutputFileStream(string filename, string encoding, bool writeXMLDecl, string programName, string programVersion) : this(libsbmlPINVOKE.new_XMLOwningOutputFileStream__SWIG_0(filename, encoding, writeXMLDecl, programName, programVersion), true) {
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  
/** */ /* libsbml-internal */ public
 XMLOwningOutputFileStream(string filename, string encoding, bool writeXMLDecl, string programName) : this(libsbmlPINVOKE.new_XMLOwningOutputFileStream__SWIG_1(filename, encoding, writeXMLDecl, programName), true) {
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  
/** */ /* libsbml-internal */ public
 XMLOwningOutputFileStream(string filename, string encoding, bool writeXMLDecl) : this(libsbmlPINVOKE.new_XMLOwningOutputFileStream__SWIG_2(filename, encoding, writeXMLDecl), true) {
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  
/** */ /* libsbml-internal */ public
 XMLOwningOutputFileStream(string filename, string encoding) : this(libsbmlPINVOKE.new_XMLOwningOutputFileStream__SWIG_3(filename, encoding), true) {
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  
/** */ /* libsbml-internal */ public
 XMLOwningOutputFileStream(string filename) : this(libsbmlPINVOKE.new_XMLOwningOutputFileStream__SWIG_4(filename), true) {
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

}

}
