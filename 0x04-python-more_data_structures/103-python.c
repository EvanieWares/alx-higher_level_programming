#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints python list
 * @p: python object
*/
void print_python_list(PyObject *p)
{
	PyObject *iterator;

	iterator = PyObject_GetIter(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", PyList_Size(p));
	printf("[*] Allocated = %zd\n", ((PyVarObject *)p)->ob_size);

	while (PyObject *item = PyIter_Next(iterator))
	{
		if (PyBytes_Check(item))
		{
			printf("Element %zd: bytes\n", PyList_GET_SIZE(p) - 1);
			print_python_bytes(item);
		}
		else
		{
			printf("Element %zd: %s\n", PyList_GET_SIZE(p) - 1, item->ob_type->tp_name);
		}
	}

	Py_DECREF(iterator);
}

/**
 * print_python_bytes - prints python bytes
 * @p: python object
*/
void print_python_bytes(PyObject *p)
{
	char *string = PyBytes_AsString(p);

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", PyBytes_GET_SIZE(p));

	if (string)
		printf("  trying string: %s\n", string);

	printf("  first %d bytes: ", sizeof(char) * 10);

	for (int i = 0; i < 10; i++)
		printf("%02x ", ((char *)p)->ob_sval[i]);

	printf("\n");
}
