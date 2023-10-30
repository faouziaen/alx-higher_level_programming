#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * print_python_string_info - prints information about Python strings
 * @py_obj: address of PyObject struct
 */
void print_python_string_info(PyObject *py_obj)
{
	wprintf(L"[.] string object info\n");
	if (strcmp(py_obj->ob_type->tp_name, "str"))
	{
		wprintf(L"  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(py_obj))
		wprintf(L"  type: compact ascii\n");
	else
		wprintf(L"  type: compact unicode object\n");
	wprintf(L"  length: %lu\n", PyUnicode_GET_LENGTH(py_obj));
	wprintf(L"  value: %ls\n", PyUnicode_AS_UNICODE(py_obj));
}
