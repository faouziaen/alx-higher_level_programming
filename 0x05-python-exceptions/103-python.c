#include <Python.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <listobject.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * print_python_bytes - Print Python bytes object info
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = 0;
	Py_ssize_t i = 0;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (size > 10)
		size = 10;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", bytes->ob_sval[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - Print Python list object info
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = 0;
	Py_ssize_t i = 0;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *element = PyList_GET_ITEM(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}

/**
 * print_python_float - Print Python float object info
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *flt = (PyFloatObject *)p;
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = flt->ob_fval;
	printf("  value: %f\n", value);
}
