#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints python list
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	PyObject *size, *allocated;

	size = PyLong_FromSize_t(PyList_GET_SIZE(p));
	allocated = PyLong_FromSize_t(PyList_GET_ALLOC(p));

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyLong_AsLong(size));
	printf("[*] Allocated = %ld\n", PyLong_AsLong(allocated));

	for (Py_ssize_t i = 0; i < PyList_GET_SIZE(p); i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - prints python bytes
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_GET_SIZE(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	if (size >= 5)
	{
		printf("  trying string: %s\n", PyBytes_AS_STRING(p));
	}

	printf("  first %ld bytes: ", size >= 10 ? 10 : size);
	for (int i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
}
