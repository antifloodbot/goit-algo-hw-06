# Завдання 2 — DFS vs BFS

У цьому завданні реалізовано алгоритми DFS та BFS для пошуку маршруту в графі транспортної мережі.

## Результати:

- **DFS шлях**: Central → North → University → Market → East → West → South → Park → Harbor
- **BFS шлях**: Central → South → Park → Harbor

## Аналіз:

- BFS пройшов найкоротший маршрут до цілі (менше станцій).
- DFS зайшов у глибину — через University → Market → West тощо.

## Висновок:

- BFS підходить для швидкого пошуку найкоротшого шляху.
- DFS зручний для задач з повним обходом або перевіркою зв'язності.