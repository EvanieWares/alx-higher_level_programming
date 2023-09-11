#include "lists.h"
#include <stdio.h>

/**
 * get_element - gets an element from a singly linked list
 * @head: pointer to the head node
 * @idx: index of the item to get
 *
 * Return: element at index idx
 */
int get_element(listint_t **head, int idx)
{
	int i = 0;
	listint_t *current = *head;

	while (i < idx)
	{
		current = current->next;
		i++;
	}
	return (current->n);
}

/**
 * get_count - count the elements in a singly linked list
 * @head: pointer to the head node
 *
 * Return: number of elements in the list
 */
int get_count(listint_t **head)
{
	int count = 0;
	listint_t *current = *head;

	while (current)
	{
		current = current->next;
		count++;
	}
	return (count);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head node
 *
 * Return: 1 if the list is palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int i, count;

	if (*head == NULL)
		return (1);

	count = get_count(head);
	for (i = 0; i < count / 2; i++)
	{
		int a = get_element(head, i);
		int b = get_element(head, count - i - 1);

		if (a != b)
		{
			return (0);
		}
	}
	return (1);
}
