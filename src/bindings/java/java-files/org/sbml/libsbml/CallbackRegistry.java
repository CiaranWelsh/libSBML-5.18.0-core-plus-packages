/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 3.0.12
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.sbml.libsbml;

public class CallbackRegistry {
   private long swigCPtr;
   protected boolean swigCMemOwn;

   protected CallbackRegistry(long cPtr, boolean cMemoryOwn)
   {
     swigCMemOwn = cMemoryOwn;
     swigCPtr    = cPtr;
   }

   protected static long getCPtr(CallbackRegistry obj)
   {
     return (obj == null) ? 0 : obj.swigCPtr;
   }

   protected static long getCPtrAndDisown (CallbackRegistry obj)
   {
     long ptr = 0;

     if (obj != null)
     {
       ptr             = obj.swigCPtr;
       obj.swigCMemOwn = false;
     }

     return ptr;
   }

  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        libsbmlJNI.delete_CallbackRegistry(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  
/**
	 * Invokes all registered callbacks on the given document. If the callbacks indicate
	 * that processing should be stopped they return a value other than operation success.
	 <p>
	 * @return LIBSBML_OPERATION_SUCCESS to indicate that processing should be continued, 
	 *         any other value to stop processing
	 */ public
 static int invokeCallbacks(SBMLDocument doc) {
    return libsbmlJNI.CallbackRegistry_invokeCallbacks(SBMLDocument.getCPtr(doc), doc);
  }

  
/**
   * Clears all registered processing callbacks
   */ public
 static void clearCallbacks() {
    libsbmlJNI.CallbackRegistry_clearCallbacks();
  }

  
/**
   * Registers a new processing callback that will be called with a newly instantiated
   * ModelDefinition object. This allows for all post processing on it that needs to
   * happen before integrating it with the target document.
   <p>
   * @param cb the callback.
   */ public
 static void addCallback(Callback cb) {
    libsbmlJNI.CallbackRegistry_addCallback(Callback.getCPtr(cb), cb);
  }

  
/**
	 * @return the number of registered callbacks.
	 */ public
 static int getNumCallbacks() {
    return libsbmlJNI.CallbackRegistry_getNumCallbacks();
  }

  
/**
   * Removes the callback with given index.
   <p>
   * @param index the index of the callback to be removed from the list.
   */ public
 static void removeCallback(int index) {
    libsbmlJNI.CallbackRegistry_removeCallback__SWIG_0(index);
  }

  
/**
	 * Removes the specified callback from the list of registered callbacks
	 <p>
	 * @param cb the callback to be removed.
	 */ public
 static void removeCallback(Callback cb) {
    libsbmlJNI.CallbackRegistry_removeCallback__SWIG_1(Callback.getCPtr(cb), cb);
  }

}
