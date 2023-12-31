#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - the singly linked list
 * @n: the integer
 * @next: next node
 *
 * Description: node structure for the single linked list
 */
typedef struct listint_s
{
        int a;
        struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int a);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
