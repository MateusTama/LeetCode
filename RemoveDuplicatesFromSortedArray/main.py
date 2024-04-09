class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 2 Ponteiros que serão utilizados.
        # l = ponteiro que marcará a posição/índice para um valor não duplicado
        # r = ponteiro que verificará se determinado valor é duplicado ou não
        # OBS: ponteiros começam em 1 pois o número na posição 0 não pode ser duplicado
        l = 1

        # Incrementa automaticamente
        for r in range(1, len(nums)):
            # Se o valor atual for diferente do valor anterior adicionamos na posição guardada pelo ponteiro l, se não, não executamos nada, pois r é incrementado automaticamente pelo laço for
            if nums[r] != nums[r - 1]:
                # na posição l de nums adicione o valor de r (único)
                nums[l] = nums[r]
                # incrementamos l para a próxima posição
                l += 1
        # retornamos l, que contém o número de elementos únicos
        return l

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))