import heapq

def min_total_cost(cables):
    # Перетворюємо список кабелів у мін-купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        # Виймаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(f"Мінімальні витрати на з'єднання: {min_total_cost(cables)}")
