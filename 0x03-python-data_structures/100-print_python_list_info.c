#include <stdlib.h>
#include <stdio.h>
#include <python.h>

/**
 * print_python_list_info -  printing the basics
 * @p: the list in python
 */
void print_python_list_info(PyObject *p)
{
	int e;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (e = 0; e < Py_SIZE(p); e++)
		printf("Element %d: %s\n", e, Py_TYPE(PyList_GetItem(p, e))->tp_name);
}
