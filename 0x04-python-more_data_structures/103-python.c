#include "Python.h"
#include <stdio.h>
#include <string.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints python list
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	unsigned long i, size, allocated;
	PyListObject *list;

	list = (PyListObject *)p;
	allocated = list->allocated;
	size = list->ob_base.ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", allocated);

	for (i = 0; i < size; i++)
	{
		const char *tp_name = list->ob_item[i]->ob_type->tp_name;

		printf("Element %lu: %s\n", i, tp_name);
		if (strcmp(tp_name, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[i]);
		}
	}
}

/**
 * print_python_bytes - prints python bytes
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	int i;
	Py_ssize_t size;
	PyBytesObject *bytes = (PyBytesObject *) p;

	if (!PyBytes_Check(bytes))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = bytes->ob_base.ob_size;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	if (size >= 5)
	{
		printf("  trying string: %s\n", bytes->ob_sval);
	}

	printf("  first %ld bytes: ", size >= 10 ? 10 : size);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	}
	printf("\n");
}
