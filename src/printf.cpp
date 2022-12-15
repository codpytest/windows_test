#include <pybind11/pybind11.h>
#include <utility>
#include <cstdio>
#include <stdio.h>

namespace py = pybind11;

/**
 * main - prints the phrase with proper grammar,
 * but the outcome is a piece of art,
 * Return: 0 if exited properly, non-zero otherwise
 */
int main(void)
{
	printf("with proper grammar, but the outcome is a piece of art,\n");
	return (0);
}