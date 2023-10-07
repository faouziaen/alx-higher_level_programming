#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    int list_size, list_allocated, i;
    PyObject *item;

    list_size = Py_SIZE(p);
    list_allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", list_allocated);

    for (i = 0; i < list_size; i++)
    {
        printf("Element %d: ", i);

        item = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(item)->tp_name);
    }
}