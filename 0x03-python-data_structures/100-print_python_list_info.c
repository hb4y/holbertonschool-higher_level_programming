#include <stdio.h>
#include <Python.h>
/**
  * print_python_list_info - print a python list
  * @p: Python List Obj
  * Return: void
  */
void print_python_list_info(PyObject *p)
{
	int i, size;
	PyListObject *aux;
	PyObject *item;

	aux = (PyListObject *) p;
	size = (int) PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", (int) size);
	printf("[*] Allocated = %d\n", (int) aux->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, (char *)(item->ob_type)->tp_name);
}
}
