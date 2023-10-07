#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to a pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *second_half = NULL;
	int result = 1;
	
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	
	second_half = slow;
	prev->next = NULL;
	reverse_list(&second_half);
	result = compare_lists(*head, second_half);
	reverse_list(&second_half);
	prev->next = second_half;
	return (result);
}

/**
 * reverse_list - Reverses a linked list.
 * @head: A pointer to a pointer to the head of the list.
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;
	
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * compare_lists - Compares two linked lists.
 * @list1: The first linked list.
 * @list2: The second linked list.
 * Return: 1 if the lists are identical, 0 otherwise.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	if (list1 == NULL && list2 == NULL)
		return (1);
	return (0);
}
