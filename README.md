# Lab-4

## Лабораторная работа №4


| Предмет | Обозначение | Размер | Очки выживания |
| ------- | ----------- | ------ | -------------- |
| Винтовка (rifle) | r | 3 ячейки | 25 |
| Пистолет (pistol) | p | 2 ячейки | 15 |
| Боекомплект (ammo) | a | 2 ячейки | 15 |
| Аптечка (medkit) | m | 2 ячейки | 20 |
| Ингалятор (inhaler) | i | 1 ячейка | 5* |
| Нож (knife) | k | 1 ячейка | 15 |
| Топор (axe) | x | 3 ячейки | 20 |
| Оберег (talisman) | t | 1 ячейка | 25 |
| Фляжка (flask) | f | 1 ячейка | 15 |
| Антидот (antidot) | d | 1 ячейка | 10* |
| Еда (supplies) | s | 2 ячейки | 20 |
| Арбалет (crossbow) | c | 2 ячейки | 20 |

**Задание**

* Том имеет ограниченное количество места в своём рюкзаке и может взять далеко не всё. 
* Каждый предмет имеет определённую ценность, выраженную в очках выживания.
* Каждый предмет, взятый с собой, повышает общие очки выживания, но его отсутствие очки выживания вычитает. 
* Том может страдать от астмы или быть заражённым, ввиду чего **ингалятор** или **антидот** соответственно должны присутствовать обязательно. 
* Наш герой уже имеет некоторое количество очков выживания, и необходимо выполнить проверку на то, чтобы итоговый счёт был положительным.

Напишите программу, которая решит проблему Тома и избавит его от долгих раздумий. Результат желательно представить в виде двумерного "ивентаря" (один элемент = одна ячейка), заполненного обозначениями предметов, к примеру:

```
[r],[r],[r]  
[c],[c],[t]  
[m],[m],[k]  

Итоговые очки выживания: 5
```

**Варианты**

| Вариант | Ячейки | Болезнь | Очков выживания |
| 10      | 3x3    | нет     | 10              |       

**Допзадание** 

Найти решение или доказать его отсутствие для случая с инвентарём в 7 ячеек.

Найти все комбинации вещей для вашего варианта, удовлетворяющие последнему условию задачи (общий счёт положительный).

**Дополнительно**

Описание задачи о рюкзаке: https://proglib.io/p/python-i-dinamicheskoe-programmirovanie-na-primere-zadachi-o-ryukzake-2020-02-04
