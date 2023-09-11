#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head node
 *
 * Return: 1 if the list is palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int i, count = 0;
	int list[2000];
	listint_t *current = *head;

	if(*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while(current)
	{
		list[count] = current->n;
		current = current->next;
		count++;
	}
	for (i = 0; i < count / 2; i++)
	{
		if (list[i] != list[count - i - 1])
		{
			return (0);
		}
	}
	return (1);
}

