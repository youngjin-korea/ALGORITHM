# BFS는 그래프를 모두 순회하는 완전탐색 기법
# 구현: STACK(FILO), 재귀함수(스택성질을 갖는)로 구현
# 재귀함수는 StackOverFlow(자신을 무한대로 호출하는 것)를 방지 해야함.
# 시간 복잡도 => O(노드+엣지)

# 한번 방문한 노드를 방문하면 안됨 -> 노드 방문 여부 체크할 배열 생성
# 그래프는 인접 리스트로 표현

# DFS의 시작 노드 정하고, 사용할 자료구조 초기화 해주기
# 원본 그래프 시작노드 픽, 인접리스트, 방문배열, 스택에 시작점 더하기

# 그래프를 인접객체로 변환
graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# 인접 그래프, 시작노드 받음
def dfs(graph, start_node):
 
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()
 
    ## 시작 노드를 시하기 
    need_visited.append(start_node)
    
    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
 
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
 
            ## 방문한 목록에 추가하기 
            visited.append(node)
 
            ## 그 노드에 연결된 노드를 
            need_visited.extend(graph[node])
            
    return visited

print(dfs(graph,'A'))
# 결과: ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']


