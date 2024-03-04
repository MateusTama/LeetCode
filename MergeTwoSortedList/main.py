# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # First Head
        pointer1 = list1
        # Second Head
        pointer2 = list2
        # Lista sem nada
        if (pointer1 == None):
            pointer1 = pointer2
            return list2
        else:
            # Enquanto o next do nó for != None
            while(pointer1.next):
                # Avançamos 1 posição
                pointer1 = pointer1.next
            # None = Head da segunda lista. Head já armazena uma lista, apenas adicionamos o head no next do ultimo elemento da primeira lista
            pointer1.next = pointer2
            # Ordenar
            newPointer = list1
            # Bubblesort
            # Enquanto tiver next
            while(newPointer):
                # Resetamos a variável para comparação com o valor próximo ao valor comparado
                nextPointer = newPointer.next
                # Enquanto tiver next
                while(nextPointer):
                    # Se o valor do pointer da variavel comparada for menor que o valor da comparação
                    if (newPointer.val > nextPointer.val):
                        # Variável aux guardando o valor do pointer comparado
                        aux = newPointer.val
                        # Valor do pointer comparado vai ser atribuído o valor de comparação
                        newPointer.val = nextPointer.val
                        # Valor de comparação vai ser atribuído o valor comparado
                        nextPointer.val = aux
                    # Avançamos o valor comparado
                    nextPointer = nextPointer.next
                # Avançando o novo ponteiro
                newPointer = newPointer.next
        # Retornando o head da lista encadeada
        return list1
    
# TESTES

node2 = ListNode(30)
node1 = ListNode(20, node2)
firstNodeHead = ListNode(10, node1)

node4 = ListNode(60)
node3 = ListNode(50, node4)
secondNodeHead = ListNode(40, node3)

# print(firstNodeHead.next.val)
print(Solution().mergeTwoLists(firstNodeHead, secondNodeHead))