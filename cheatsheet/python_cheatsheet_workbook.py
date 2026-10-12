"""
코테용 Python 치트시트 문제집
================================

사용법
  1. 각 문제 함수의 `raise NotImplementedError` 줄을 지우고 직접 구현한다.
  2. `python python_cheatsheet_workbook.py` 로 실행하면 문제별로 통과/실패/미풀이가 표시된다.
     특정 섹션만 보려면: `python python_cheatsheet_workbook.py 3`  (3 = dict/set)
     한 문제만 보려면:   `python python_cheatsheet_workbook.py 3-2`  (여러 개: `3-2 4 5-1`)
  3. 막히면 아래 순서로 힌트를 본다.
       힌트1: 방향을 잡는 질문
       힌트2: 써야 할 개념/함수 이름
     그래도 막히면 Claude에게 "다음 힌트"라고 하면 된다 (문법 예시 → 의사코드 → 코드 순).
  4. 풀고 나서 새로 알게 된 문법은 치트시트(맨 아래 메모란)에 한 줄씩 적어둔다.

정답 코드는 들어있지 않다. 테스트(assert)가 통과하면 정답이다.
"""


# ════════════════════════════════════════════════════════════════════
# 0. 기본 틀
# ════════════════════════════════════════════════════════════════════

def ex0_1_solution_format(numbers):
    """
    [0-1] 프로그래머스 solution 형식
    정수 리스트 numbers를 받아 합계를 return 한다. (print가 아니라 return!)
    예) [1, 2, 3] -> 6

    힌트1: Kotlin의 `fun solution(numbers: IntArray): Int { return ... }` 를 Python으로 옮기면?
    힌트2: 내장 함수 sum
    """
    return sum(numbers)


def ex0_2_enumerate(words):
    """
    [0-2] 인덱스와 값을 같이 순회
    words의 각 원소를 "인덱스:값" 문자열로 만든 리스트를 return.
    예) ["a", "b"] -> ["0:a", "1:b"]

    힌트1: Kotlin의 forEachIndexed / withIndex() 에 해당하는 것은?
    힌트2: enumerate, f-string
    """
    raise NotImplementedError


def ex0_3_zip(names, scores):
    """
    [0-3] 두 리스트를 짝지어 순회
    이름 리스트와 점수 리스트를 받아 점수가 60 이상인 사람 이름만 리스트로 return.
    예) ["a","b","c"], [70, 50, 90] -> ["a", "c"]

    힌트1: 같은 위치의 원소끼리 묶어서 한 번에 돌 수 있을까? (Kotlin의 zip)
    힌트2: zip, 리스트 컴프리헨션 (조건 붙은 형태)
    """
    raise NotImplementedError


def ex0_4_ternary(n):
    """
    [0-4] 삼항 연산자
    n이 짝수면 "Even", 홀수면 "Odd" 를 한 줄로 return.

    힌트1: Kotlin의 `if (cond) a else b` 식(expression)은 Python에서 어순이 다르다. 어떻게?
    힌트2: 조건 표현식 (conditional expression)
    """
    raise NotImplementedError


def ex0_5_divmod(n):
    """
    [0-5] 몫과 나머지
    분 단위 정수 n을 (시, 분) 튜플로 return.
    예) 135 -> (2, 15)

    힌트1: Python의 `/` 는 Kotlin Int 나눗셈과 결과 타입이 다르다. 정수 몫은 어떤 연산자?
    힌트2: //, %, 또는 divmod
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════
# 1. 문자열
# ════════════════════════════════════════════════════════════════════

def ex1_1_reverse(s):
    """
    [1-1] 문자열 뒤집기
    예) "abc" -> "cba"

    힌트1: 슬라이싱의 세 번째 값(step)이 음수면?
    힌트2: 슬라이싱 [start:stop:step]
    """
    raise NotImplementedError


def ex1_2_is_palindrome(s):
    """
    [1-2] 회문 판별 (대소문자 무시)
    예) "Level" -> True, "abc" -> False

    힌트1: 비교하기 전에 무엇을 통일해야 할까?
    힌트2: lower(), 슬라이싱
    """
    raise NotImplementedError


def ex1_3_split_join(sentence):
    """
    [1-3] 단어 순서 뒤집기
    공백으로 구분된 문장의 단어 순서를 뒤집어 다시 공백으로 이어 return.
    예) "I love python" -> "python love I"

    힌트1: 문자열 → 리스트 → 문자열 순서로 바꾸면?
    힌트2: split, join (join은 구분자 쪽에서 호출한다: Kotlin joinToString과 방향이 반대)
    """
    raise NotImplementedError


def ex1_4_count_char(s, ch):
    """
    [1-4] 특정 문자 개수 세기
    예) "banana", "a" -> 3

    힌트1: 반복문 없이 한 번에 셀 수 있는 문자열 메서드가 있을까?
    힌트2: str.count
    """
    raise NotImplementedError


def ex1_5_only_digits(s):
    """
    [1-5] 숫자만 골라 정수로
    문자열에서 숫자 문자만 골라 이어붙인 뒤 int로 return. (숫자가 최소 1개 있다고 가정)
    예) "a1b2c3" -> 123

    힌트1: 문자 하나가 숫자인지 판별하는 메서드는?
    힌트2: isdigit, join, int()
    """
    raise NotImplementedError


def ex1_6_caesar(s, n):
    """
    [1-6] 시저 암호 (소문자만, 공백은 그대로)
    각 소문자를 알파벳 순서로 n칸 민다. z 다음은 a.
    예) "ab z", 1 -> "bc a"

    힌트1: 문자를 숫자로 바꿨다가 다시 문자로 바꿀 수 있다면? 끝을 넘어가면 어떻게 되돌릴까?
    힌트2: ord, chr, % 26
    """
    raise NotImplementedError


def ex1_7_strip_replace(s):
    """
    [1-7] 양끝 공백 제거 + 치환
    양 끝 공백을 없애고, 가운데 '-'를 모두 ' '로 바꿔 return.
    예) "  a-b-c  " -> "a b c"

    힌트1: 메서드를 연달아 호출할 수 있다 (문자열은 불변이라 매번 새 문자열이 나온다).
    힌트2: strip, replace
    """
    raise NotImplementedError


def ex1_8_format(name, score):
    """
    [1-8] f-string 포매팅
    점수를 소수점 둘째 자리까지, 이름과 함께 "name: 점수" 형태로 return.
    예) "kim", 3.14159 -> "kim: 3.14"

    힌트1: f-string 중괄호 안에서 숫자 형식을 지정할 수 있다. 어떤 기호 뒤에?
    힌트2: 포맷 지정자 :.2f
    """
    raise NotImplementedError


def ex1_9_immutable(s, i, ch):
    """
    [1-9] 문자열의 i번째 문자만 바꾸기
    예) "hello", 0, "j" -> "jello"

    힌트1: s[i] = ch 를 하면 무슨 일이 생길까? 그렇다면 우회 방법은?
    힌트2: 문자열 불변성, 슬라이싱 이어붙이기 (또는 list로 바꿨다가 join)
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════
# 2. 리스트
# ════════════════════════════════════════════════════════════════════

def ex2_1_grid(rows, cols):
    """
    [2-1] 2차원 리스트 초기화
    rows x cols 크기의 0으로 채운 2차원 리스트를 return.
    단, 한 칸을 바꿨을 때 다른 행이 같이 바뀌면 안 된다.

    힌트1: [[0] * cols] * rows 로 만들면 각 행이 서로 다른 객체일까?
    힌트2: 리스트 컴프리헨션으로 행마다 새로 만들기
    """
    raise NotImplementedError


def ex2_2_squares_of_even(nums):
    """
    [2-2] 리스트 컴프리헨션
    짝수만 골라 제곱한 리스트를 return.
    예) [1, 2, 3, 4] -> [4, 16]

    힌트1: Kotlin의 filter { }.map { } 를 한 줄 식으로 쓴다면?
    힌트2: [식 for x in 리스트 if 조건]
    """
    raise NotImplementedError


def ex2_3_stack(ops):
    """
    [2-3] 리스트를 스택으로
    ops는 ("push", x) 또는 ("pop", None) 튜플의 리스트.
    pop 때 꺼낸 값을 순서대로 모은 리스트를 return. (빈 스택에서 pop은 없다고 가정)
    예) [("push",1),("push",2),("pop",None)] -> [2]

    힌트1: 리스트의 맨 뒤에 넣고 맨 뒤에서 빼는 메서드는?
    힌트2: append, pop(), 튜플 언패킹 (for op, x in ops)
    """
    raise NotImplementedError


def ex2_4_copy(a):
    """
    [2-4] 깊은 복사
    2차원 리스트 a의 복사본을 return. 복사본을 바꿔도 원본이 바뀌면 안 된다.

    힌트1: a[:] 나 list(a) 는 안쪽 리스트까지 복사할까?
    힌트2: 얕은 복사 vs 깊은 복사, copy.deepcopy (또는 행마다 슬라이싱)
    """
    raise NotImplementedError


def ex2_5_any_all(nums):
    """
    [2-5] any / all
    (모두 양수인가?, 0이 하나라도 있는가?) 튜플을 return.
    예) [1, 2, 0] -> (False, True)

    힌트1: Kotlin의 all { } / any { } 와 같은 내장 함수가 있다. 인자로 무엇을 넘길까?
    힌트2: all, any, 제너레이터 식
    """
    raise NotImplementedError


def ex2_6_unpack(nums):
    """
    [2-6] 언패킹
    리스트의 (첫 원소, 마지막 원소, 가운데 원소들 리스트)를 return. 원소는 2개 이상.
    예) [1, 2, 3, 4] -> (1, 4, [2, 3])

    힌트1: 인덱스를 쓰지 않고 "나머지 전부"를 한 변수에 받을 수 있을까?
    힌트2: 별표 언패킹 first, *mid, last = ...
    """
    raise NotImplementedError


def ex2_7_remove_all(nums, target):
    """
    [2-7] 특정 값 모두 제거 (원본은 건드리지 말고 새 리스트로)
    예) [1, 2, 1, 3], 1 -> [2, 3]

    힌트1: remove()는 몇 개를 지울까? 순회 중에 원본을 지우면 무슨 문제가 생길까?
    힌트2: 조건 붙은 리스트 컴프리헨션
    """
    raise NotImplementedError


def ex2_8_index_of_max(nums):
    """
    [2-8] 최댓값의 인덱스 (여러 개면 가장 앞)
    예) [3, 9, 2, 9] -> 1

    힌트1: 최댓값을 먼저 구한 다음, 그 값의 위치를 찾는 메서드는?
    힌트2: max, list.index
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════
# 3. dict / set
# ════════════════════════════════════════════════════════════════════

def ex3_1_word_count(words):
    """
    [3-1] dict로 개수 세기 (Counter 쓰지 말고)
    예) ["a", "b", "a"] -> {"a": 2, "b": 1}

    힌트1: 없는 키를 읽으면 KeyError가 난다. 없을 때 기본값을 주며 읽는 방법은?
    힌트2: dict.get(key, 기본값)
    """
    raise NotImplementedError


def ex3_2_items_loop(scores):
    """
    [3-2] dict 순회
    {이름: 점수} 에서 점수가 가장 높은 사람의 이름을 return. (동점 없음)

    힌트1: 키와 값을 동시에 꺼내며 돌 수 있을까? 혹은 max에 "비교 기준"을 줄 수 있을까?
    힌트2: items(), 또는 max(dict, key=...)
    """
    raise NotImplementedError


def ex3_3_group(words):
    """
    [3-3] 그룹핑 (첫 글자 기준)
    예) ["apple", "avocado", "banana"] -> {"a": ["apple", "avocado"], "b": ["banana"]}

    힌트1: 키가 처음 나올 때 빈 리스트를 만들어 두는 방법은?
    힌트2: setdefault (5장에서 defaultdict로도 다시 풀어본다)
    """
    raise NotImplementedError


def ex3_4_dedup_keep_order(nums):
    """
    [3-4] 순서 유지하며 중복 제거
    예) [3, 1, 3, 2, 1] -> [3, 1, 2]

    힌트1: set(nums)는 순서를 지켜줄까? 지금까지 본 값을 기억하면서 돌면?
    힌트2: set으로 방문 체크, 또는 dict.fromkeys (dict는 삽입 순서 유지)
    """
    raise NotImplementedError


def ex3_5_set_ops(a, b):
    """
    [3-5] 집합 연산
    (둘 다 있는 것, a에만 있는 것, 둘 중 하나에만 있는 것)을 각각 정렬된 리스트로 묶어 튜플 return.
    예) [1,2,3], [2,3,4] -> ([2,3], [1], [1,4])

    힌트1: 수학 시간의 교집합/차집합/대칭차집합을 연산자 하나로 쓸 수 있다면?
    힌트2: &, -, ^ (set끼리), sorted
    """
    raise NotImplementedError


def ex3_6_tuple_key(points):
    """
    [3-6] 튜플을 키로
    (x, y) 좌표 리스트에서 서로 다른 좌표의 개수를 return.
    예) [(0,0), (1,2), (0,0)] -> 2

    힌트1: 리스트는 set/dict 키가 될 수 없는데 튜플은 된다. 왜일까?
    힌트2: hashable, set
    """
    raise NotImplementedError


def ex3_7_two_sum(nums, target):
    """
    [3-7] 두 수의 합 (O(n))
    합이 target이 되는 두 원소의 인덱스 (i, j), i < j 를 return. 답은 정확히 하나.
    예) [2, 7, 11, 15], 9 -> (0, 1)

    힌트1: 이중 for문은 O(n²)이다. 지금 보는 수의 "짝"이 앞에 있었는지 O(1)에 알 수 있다면?
    힌트2: dict에 {값: 인덱스} 저장
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════
# 4. 정렬
# ════════════════════════════════════════════════════════════════════

def ex4_1_sort_vs_sorted(nums):
    """
    [4-1] sort vs sorted
    원본 nums는 바꾸지 말고, 내림차순 정렬된 새 리스트를 return.

    힌트1: 둘 중 어느 쪽이 원본을 바꾸고 None을 반환할까?
    힌트2: sorted(..., reverse=True)
    """
    raise NotImplementedError


def ex4_2_sort_by_len(words):
    """
    [4-2] key로 정렬
    길이 짧은 순, 길이가 같으면 사전순으로 정렬해 return.
    예) ["bb", "a", "ab", "c"] -> ["a", "c", "ab", "bb"]

    힌트1: Kotlin의 sortedWith(compareBy({ it.length }, { it })) 를 key 하나로 표현하려면 무엇을 반환해야 할까?
    힌트2: key=lambda + 튜플 (튜플은 앞 원소부터 비교)
    """
    raise NotImplementedError


def ex4_3_mixed_order(people):
    """
    [4-3] 섞인 방향 정렬
    people은 (이름, 나이) 리스트. 나이 내림차순, 나이가 같으면 이름 오름차순으로 정렬해 return.
    예) [("b",20),("a",20),("c",30)] -> [("c",30),("a",20),("b",20)]

    힌트1: reverse=True 를 쓰면 이름까지 뒤집힌다. 숫자 하나만 거꾸로 하려면?
    힌트2: 숫자에 음수 부호 붙이기
    """
    raise NotImplementedError


def ex4_4_stable(records):
    """
    [4-4] 안정 정렬 활용
    records는 (이름, 반) 리스트. 반 기준으로만 오름차순 정렬하되, 같은 반 안에서는 원래 순서 유지.
    예) [("z",2),("a",1),("y",2),("b",1)] -> [("a",1),("b",1),("z",2),("y",2)]

    힌트1: Python 정렬은 키가 같으면 원래 순서를 지킬까?
    힌트2: 안정 정렬(stable sort), key=lambda r: r[1]
    """
    raise NotImplementedError


def ex4_5_largest_number(nums):
    """
    [4-5] 이어붙여 가장 큰 수 (프로그래머스 "가장 큰 수" 축소판)
    0 이상 999 이하 정수 리스트를 이어붙여 만들 수 있는 가장 큰 수를 문자열로 return.
    예) [6, 10, 2] -> "6210",  [3, 30, 34] -> "34330"

    힌트1: 문자열 "3" 과 "30" 중 앞에 와야 할 것은? 길이가 다를 때 공정하게 비교하려면 어떻게 늘려볼까?
    힌트2: str 변환, 비교 기준을 바꾼 정렬 (key 트릭 또는 functools.cmp_to_key)
    (놓치기 쉬운 입력이 하나 있다. 채점기 테스트를 열어보기 전에 스스로 찾아볼 것)
    """
    raise NotImplementedError


def ex4_6_max_with_key(words):
    """
    [4-6] max에 key
    가장 긴 단어를 return. (같은 길이면 먼저 나온 것)

    힌트1: sorted 말고 max에도 key를 줄 수 있을까?
    힌트2: max(..., key=len)
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════
# 5. collections
# ════════════════════════════════════════════════════════════════════

from collections import Counter, deque, defaultdict  # noqa: E402


def ex5_1_counter_top(s):
    """
    [5-1] Counter.most_common
    문자열에서 가장 많이 나온 문자 하나를 return. (최다 빈도 동점 없음)

    힌트1: 세는 일 자체를 대신해주는 클래스가 있다. 빈도순으로 꺼내는 메서드는?
    힌트2: Counter(s).most_common(1)
    """
    raise NotImplementedError


def ex5_2_counter_sub(participant, completion):
    """
    [5-2] Counter 뺄셈 (프로그래머스 "완주하지 못한 선수")
    participant 에는 있고 completion 에는 없는 단 한 명을 return. 동명이인이 있을 수 있다.
    예) ["a","b","a"], ["a","b"] -> "a"

    힌트1: set 차집합을 쓰면 동명이인 때 왜 틀릴까?
    힌트2: Counter끼리 - 연산
    """
    raise NotImplementedError


def ex5_3_is_anagram(a, b):
    """
    [5-3] Counter 비교
    두 문자열이 애너그램(글자 구성이 같음)인지 return.
    예) "listen", "silent" -> True

    힌트1: 정렬해서 비교하는 방법 말고, 글자별 개수를 비교하면?
    힌트2: Counter ==
    """
    raise NotImplementedError


def ex5_4_queue(tasks, k):
    """
    [5-4] deque를 큐로
    tasks 리스트를 앞에서 하나씩 꺼내 결과 리스트에 넣는다. 단, 꺼낸 값이 k의 배수면
    결과에 넣지 않고 큐 맨 뒤로 보낸 뒤 그 값을 k로 나눈 몫으로 바꾼다(0이 되면 버림).
    최종 결과 리스트를 return.
    예) [1, 4, 3], 2 -> [1, 3, 1]   (4 → 뒤로 가서 2 → 다시 뒤로 가서 1 → 결과)

    힌트1: list.pop(0) 은 왜 느릴까? 앞에서 꺼내는 게 O(1)인 자료구조는?
    힌트2: deque, popleft, append
    """
    raise NotImplementedError


def ex5_5_rotate(nums, k):
    """
    [5-5] deque.rotate
    리스트를 오른쪽으로 k칸 회전한 결과를 리스트로 return.
    예) [1,2,3,4,5], 2 -> [4,5,1,2,3]

    힌트1: 슬라이싱으로도 되지만, deque에는 회전 전용 메서드가 있다. 양수/음수 방향은?
    힌트2: deque.rotate, list()
    """
    raise NotImplementedError


def ex5_6_bfs(graph, start):
    """
    [5-6] deque로 BFS
    graph는 {노드: [이웃들]} dict. start에서 BFS로 방문한 순서를 리스트로 return.
    이웃은 리스트에 적힌 순서대로 방문.
    예) {1:[2,3], 2:[4], 3:[4], 4:[]}, 1 -> [1, 2, 3, 4]

    힌트1: 다음에 볼 노드를 줄 세울 자료구조와, 이미 본 노드를 기억할 자료구조가 각각 필요하다.
    힌트2: deque + set(visited), 큐에 넣을 때 방문 표시
    """
    raise NotImplementedError


def ex5_7_defaultdict_group(pairs):
    """
    [5-7] defaultdict
    (장르, 곡) 쌍 리스트를 {장르: [곡들]} 로 묶어 일반 dict로 return.
    예) [("pop","a"),("rock","b"),("pop","c")] -> {"pop":["a","c"], "rock":["b"]}

    힌트1: 3-3에서 setdefault로 한 것을 "키가 없으면 자동으로 빈 리스트"로 바꾸려면?
    힌트2: defaultdict(list), dict()로 변환
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════
# 6. 입출력 · 디버깅
# ════════════════════════════════════════════════════════════════════

def ex6_1_print_options(nums):
    """
    [6-1] print 대신 문자열로: sep / join
    숫자 리스트를 공백 없이 쉼표로 이은 문자열을 return. (print(*nums, sep=",") 출력과 같은 모양)
    예) [1, 2, 3] -> "1,2,3"

    힌트1: join은 문자열만 이어붙일 수 있다. 숫자를 먼저 어떻게 바꿀까?
    힌트2: map(str, ...), ",".join
    (덤: print의 sep, end 옵션도 직접 찍어보자)
    """
    raise NotImplementedError


def ex6_2_parse_input(line):
    """
    [6-2] 한 줄 입력 파싱
    "3 5 7" 같은 문자열을 정수 리스트로 return. (백준식 input().split() 연습)

    힌트1: 쪼갠 다음 각 원소에 int를 적용하려면?
    힌트2: split, map(int, ...), list()
    """
    raise NotImplementedError


def ex6_3_safe_get(arr, i):
    """
    [6-3] IndexError 다루기
    arr[i] 를 return 하되 범위를 벗어나면 -1 을 return. 음수 i는 범위 밖으로 친다.

    힌트1: Python에서 arr[-1] 은 에러가 날까? 그렇다면 왜 음수를 따로 막아야 할까?
    힌트2: 범위 체크 (0 <= i < len(arr)) 또는 try/except IndexError
    """
    raise NotImplementedError


def ex6_4_deep_recursion(n):
    """
    [6-4] 재귀 한도
    1부터 n까지의 합을 "재귀"로 구해 return. n = 5000 에서도 동작해야 한다.

    힌트1: 기본 재귀 깊이 제한은 대략 몇일까? n=5000 이면 무슨 에러가 날까?
    힌트2: sys.setrecursionlimit
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════
# 7. 시간복잡도 (O 표기를 문자열로 답하기)
# ════════════════════════════════════════════════════════════════════

def ex7_1_complexity_quiz():
    """
    [7-1] 연산별 평균 시간복잡도 퀴즈
    아래 dict의 값을 "O(1)", "O(n)", "O(log n)", "O(n log n)" 중 하나로 채워 return.

    힌트1: 리스트는 "배열", dict/set은 "해시 테이블"이다. 각각 어떤 연산이 전체를 훑어야 할까?
    힌트2: 해시 조회, 배열 시프트, 비교 정렬 하한
    """
    answers = {
        "list.append": "",
        "list.pop()": "",
        "list.pop(0)": "",
        "list.insert(0, x)": "",
        "x in list": "",
        "x in set": "",
        "dict[key]": "",
        "deque.popleft()": "",
        "sorted(list)": "",
        "heapq.heappush": "",
    }
    raise NotImplementedError  # 위 값을 채운 뒤 이 줄을 return answers 로 바꾼다


def ex7_2_fast_membership(haystack, needles):
    """
    [7-2] in 검사 비용
    needles 각각이 haystack에 있는지 bool 리스트로 return.
    haystack, needles 둘 다 20만 개여도 1초 안에 끝나야 한다.

    힌트1: list에 대한 `in` 을 20만 번 하면 총 몇 번 비교할까?
    힌트2: set으로 한 번 바꿔두기
    """
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════
# 채점기 (건드리지 않아도 됨)
# ════════════════════════════════════════════════════════════════════

_current_call = [None]  # 💥 에러가 났을 때 어떤 호출이었는지 보여주기 위해 기록


def _eq(actual, expected, call):
    """actual != expected 면 호출/내 결과/기대값을 담은 AssertionError를 던진다."""
    if actual == expected and type(actual) is type(expected):
        return
    if isinstance(actual, dict) and isinstance(expected, dict):
        keys = [k for k in expected if actual.get(k) != expected[k]]
        keys += [k for k in actual if k not in expected]
        mine = "{" + ", ".join(f"{k!r}: {actual.get(k, '(없음)')!r}" for k in keys) + "}"
        want = "{" + ", ".join(f"{k!r}: {expected.get(k, '(없어야 함)')!r}" for k in keys) + "}"
        lines = [f"호출    {call}", f"틀린 키만 → 내 결과 {mine}", f"           기대값  {want}"]
    else:
        lines = [f"호출    {call}", f"내 결과 {actual!r}", f"기대값  {expected!r}"]
        if actual is None:
            lines.append("→ return 을 빠뜨리지 않았나?")
        elif actual == expected:
            lines.append(f"→ 값은 같지만 타입이 다르다 ({type(actual).__name__} vs {type(expected).__name__})")
    raise AssertionError("\n" + "\n".join("       " + s for s in lines))


def _call(fn, *args):
    """fn(*args) 를 호출하면서, 에러 메시지용으로 호출 모양을 문자열로 남긴다."""
    call = f"{fn.__name__}({', '.join(map(repr, args))})"
    _current_call[0] = call
    return fn(*args), call


def _expect(*cases):
    """각 case = (함수, 인자..., 기대값). 위에서부터 차례로 검사한다."""
    def run():
        for fn, *args, expected in cases:
            actual, call = _call(fn, *args)
            _eq(actual, expected, call)
    return run


def _tests():
    def t2_1():
        g, call = _call(ex2_1_grid, 3, 2)
        _eq(g, [[0, 0], [0, 0], [0, 0]], call)
        g[0][0] = 1
        assert g[1][0] == 0, f"g[0][0] = 1 했더니 g 가 {g} 가 됐다. 행들이 같은 리스트를 공유하고 있다"

    def t2_4():
        a = [[1, 2], [3, 4]]
        b, call = _call(ex2_4_copy, a)
        b[0][0] = 99
        assert a == [[1, 2], [3, 4]], f"복사본에서 b[0][0] = 99 했더니 원본이 {a} 가 됐다"
        _eq(b, [[99, 2], [3, 4]], call + " 후 b[0][0] = 99")

    def t2_7():
        a = [1, 2, 1, 3]
        r, call = _call(ex2_7_remove_all, a, 1)
        assert a == [1, 2, 1, 3], f"원본이 {a} 로 바뀌었다"
        _eq(r, [2, 3], call)

    def t4_1():
        a = [3, 1, 2]
        r, call = _call(ex4_1_sort_vs_sorted, a)
        assert a == [3, 1, 2], f"원본이 {a} 로 바뀌었다"
        _eq(r, [3, 2, 1], call)

    def t5_7():
        r, call = _call(ex5_7_defaultdict_group, [("pop", "a"), ("rock", "b"), ("pop", "c")])
        assert type(r) is dict, f"{type(r).__name__} 말고 일반 dict로 돌려줘야 한다"
        _eq(r, {"pop": ["a", "c"], "rock": ["b"]}, call)

    def t7_2():
        import time
        hay = list(range(200_000))
        needles = list(range(100_000, 300_000))
        call = "ex7_2_fast_membership(0~199999, 100000~299999)"
        _current_call[0] = call
        st = time.time()
        r = ex7_2_fast_membership(hay, needles)
        elapsed = time.time() - st
        assert r is not None, "return 을 빠뜨리지 않았나?"
        assert r == [True] * 100_000 + [False] * 100_000, "앞 10만 개는 True, 뒤 10만 개는 False 여야 한다"
        assert elapsed < 1.0, f"{elapsed:.2f}초 걸렸다. 1초 안에 끝나야 한다"

    return [
        ("0", "0-1 solution 형식", _expect((ex0_1_solution_format, [1, 2, 3], 6))),
        ("0", "0-2 enumerate", _expect((ex0_2_enumerate, ["a", "b"], ["0:a", "1:b"]))),
        ("0", "0-3 zip", _expect((ex0_3_zip, ["a", "b", "c"], [70, 50, 90], ["a", "c"]))),
        ("0", "0-4 삼항", _expect((ex0_4_ternary, 4, "Even"), (ex0_4_ternary, 7, "Odd"))),
        ("0", "0-5 divmod", _expect((ex0_5_divmod, 135, (2, 15)))),
        ("1", "1-1 뒤집기", _expect((ex1_1_reverse, "abc", "cba"))),
        ("1", "1-2 회문", _expect((ex1_2_is_palindrome, "Level", True), (ex1_2_is_palindrome, "abc", False))),
        ("1", "1-3 split/join", _expect((ex1_3_split_join, "I love python", "python love I"))),
        ("1", "1-4 count", _expect((ex1_4_count_char, "banana", "a", 3))),
        ("1", "1-5 isdigit", _expect((ex1_5_only_digits, "a1b2c3", 123))),
        ("1", "1-6 ord/chr", _expect((ex1_6_caesar, "ab z", 1, "bc a"), (ex1_6_caesar, "xyz", 3, "abc"))),
        ("1", "1-7 strip/replace", _expect((ex1_7_strip_replace, "  a-b-c  ", "a b c"))),
        ("1", "1-8 f-string", _expect((ex1_8_format, "kim", 3.14159, "kim: 3.14"))),
        ("1", "1-9 불변성", _expect((ex1_9_immutable, "hello", 0, "j", "jello"), (ex1_9_immutable, "abc", 2, "z", "abz"))),
        ("2", "2-1 2차원 초기화", t2_1),
        ("2", "2-2 컴프리헨션", _expect((ex2_2_squares_of_even, [1, 2, 3, 4], [4, 16]))),
        ("2", "2-3 스택", _expect((ex2_3_stack, [("push", 1), ("push", 2), ("pop", None), ("push", 3), ("pop", None), ("pop", None)], [2, 3, 1]))),
        ("2", "2-4 깊은 복사", t2_4),
        ("2", "2-5 any/all", _expect((ex2_5_any_all, [1, 2, 0], (False, True)), (ex2_5_any_all, [1, 2], (True, False)))),
        ("2", "2-6 별표 언패킹", _expect((ex2_6_unpack, [1, 2, 3, 4], (1, 4, [2, 3])), (ex2_6_unpack, [1, 2], (1, 2, [])))),
        ("2", "2-7 값 모두 제거", t2_7),
        ("2", "2-8 최댓값 인덱스", _expect((ex2_8_index_of_max, [3, 9, 2, 9], 1))),
        ("3", "3-1 get 기본값", _expect((ex3_1_word_count, ["a", "b", "a"], {"a": 2, "b": 1}))),
        ("3", "3-2 items/max key", _expect((ex3_2_items_loop, {"a": 50, "b": 90, "c": 70}, "b"))),
        ("3", "3-3 setdefault", _expect((ex3_3_group, ["apple", "avocado", "banana"], {"a": ["apple", "avocado"], "b": ["banana"]}))),
        ("3", "3-4 순서 유지 중복 제거", _expect((ex3_4_dedup_keep_order, [3, 1, 3, 2, 1], [3, 1, 2]))),
        ("3", "3-5 집합 연산", _expect((ex3_5_set_ops, [1, 2, 3], [2, 3, 4], ([2, 3], [1], [1, 4])))),
        ("3", "3-6 튜플 키", _expect((ex3_6_tuple_key, [(0, 0), (1, 2), (0, 0)], 2))),
        ("3", "3-7 two sum", _expect((ex3_7_two_sum, [2, 7, 11, 15], 9, (0, 1)), (ex3_7_two_sum, [3, 2, 4], 6, (1, 2)))),
        ("4", "4-1 sort vs sorted", t4_1),
        ("4", "4-2 튜플 key", _expect((ex4_2_sort_by_len, ["bb", "a", "ab", "c"], ["a", "c", "ab", "bb"]))),
        ("4", "4-3 음수 key", _expect((ex4_3_mixed_order, [("b", 20), ("a", 20), ("c", 30)], [("c", 30), ("a", 20), ("b", 20)]))),
        ("4", "4-4 안정 정렬", _expect((ex4_4_stable, [("z", 2), ("a", 1), ("y", 2), ("b", 1)], [("a", 1), ("b", 1), ("z", 2), ("y", 2)]))),
        ("4", "4-5 가장 큰 수", _expect(
            (ex4_5_largest_number, [6, 10, 2], "6210"),
            (ex4_5_largest_number, [3, 30, 34, 5, 9], "9534330"),
            (ex4_5_largest_number, [0, 0, 0], "0"),
        )),
        ("4", "4-6 max key", _expect((ex4_6_max_with_key, ["ab", "abcd", "xyzw", "a"], "abcd"))),
        ("5", "5-1 most_common", _expect((ex5_1_counter_top, "abracadabra", "a"))),
        ("5", "5-2 Counter 뺄셈", _expect(
            (ex5_2_counter_sub, ["a", "b", "a"], ["a", "b"], "a"),
            (ex5_2_counter_sub, ["leo", "kiki", "eden"], ["eden", "kiki"], "leo"),
        )),
        ("5", "5-3 애너그램", _expect((ex5_3_is_anagram, "listen", "silent", True), (ex5_3_is_anagram, "aab", "abb", False))),
        ("5", "5-4 deque 큐", _expect((ex5_4_queue, [1, 4, 3], 2, [1, 3, 1]))),
        ("5", "5-5 rotate", _expect((ex5_5_rotate, [1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]))),
        ("5", "5-6 BFS", _expect(
            (ex5_6_bfs, {1: [2, 3], 2: [4], 3: [4], 4: []}, 1, [1, 2, 3, 4]),
            (ex5_6_bfs, {1: [3, 2], 2: [1], 3: [4], 4: [1]}, 1, [1, 3, 2, 4]),
        )),
        ("5", "5-7 defaultdict", t5_7),
        ("6", "6-1 map/join", _expect((ex6_1_print_options, [1, 2, 3], "1,2,3"))),
        ("6", "6-2 입력 파싱", _expect((ex6_2_parse_input, "3 5 7", [3, 5, 7]))),
        ("6", "6-3 IndexError", _expect(
            (ex6_3_safe_get, [1, 2], 1, 2),
            (ex6_3_safe_get, [1, 2], 2, -1),
            (ex6_3_safe_get, [1, 2], -1, -1),
        )),
        ("6", "6-4 재귀 한도", _expect((ex6_4_deep_recursion, 10, 55), (ex6_4_deep_recursion, 5000, 12502500))),
        ("7", "7-1 복잡도 퀴즈", _expect((ex7_1_complexity_quiz, {
            "list.append": "O(1)",
            "list.pop()": "O(1)",
            "list.pop(0)": "O(n)",
            "list.insert(0, x)": "O(n)",
            "x in list": "O(n)",
            "x in set": "O(1)",
            "dict[key]": "O(1)",
            "deque.popleft()": "O(1)",
            "sorted(list)": "O(n log n)",
            "heapq.heappush": "O(log n)",
        }))),
        ("7", "7-2 set 멤버십", t7_2),
    ]


def _run(targets=()):
    """targets: "3" 같은 섹션 번호나 "3-2" 같은 문제 번호. 비어 있으면 전체."""
    passed = failed = todo = 0
    for sec, name, fn in _tests():
        if targets and sec not in targets and name.split()[0] not in targets:
            continue
        _current_call[0] = None
        try:
            fn()
            print(f"  ✅ {name}")
            passed += 1
        except NotImplementedError:
            print(f"  ⬜ {name}  (아직 안 풂)")
            todo += 1
        except AssertionError as e:
            msg = str(e)
            print(f"  ❌ {name}{msg if msg.startswith(chr(10)) else '  ' + msg}")
            failed += 1
        except Exception as e:  # 풀이 코드에서 난 에러도 보여준다
            print(f"  💥 {name}  {type(e).__name__}: {e}")
            if _current_call[0]:
                print(f"       호출    {_current_call[0]}")
            failed += 1
    if passed + failed + todo == 0:
        print(f"  해당하는 문제가 없다: {' '.join(targets)}  (예: 3 또는 3-2)")
        return
    print(f"\n통과 {passed} · 실패 {failed} · 미풀이 {todo}")

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")  # Windows(cp949)에서 이모지 출력 에러 방지
    _run(sys.argv[1:])


# ════════════════════════════════════════════════════════════════════
# 내 치트시트 메모 (풀면서 새로 알게 된 문법을 한 줄씩)
# ════════════════════════════════════════════════════════════════════
# -
# -
# -
