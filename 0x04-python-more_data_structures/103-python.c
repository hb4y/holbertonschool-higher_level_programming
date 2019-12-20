#include <stdio.h>
#include <Python.h>
/**
  * print_python_list - print a python list
  * @p: Python List Obj
  * Return: void
  */
void print_python_list(PyObject *p)
{
	int i, size;
	PyListObject *aux;
	PyObject *item;

	aux = (PyListObject *) p;
	size = (int) PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int) size);
	printf("[*] Allocated = %d\n", (int) aux->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, (char *)(item->ob_type)->tp_name);
	}
}

/**
 * print_python_bytes - print a python list
 * @p: Python List Obj
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		return;
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}
