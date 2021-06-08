class Heap :
    def __init__(self, data) : # 힙 클래스 객체 생성시 루트 노드를 넣고 생성
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx) : # 부모 자식 바꿔야 하면 True 리턴하는 함수
        if inserted_idx <= 1 : # 힙에 암것도 안들어 있거나 방금 삽입한게 첫 데이터인 경우
            return False
        
        parent_idx = inserted_idx // 2
        
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx] :
            return True # 부모 자식 비교 후 자식이 더 크면? 바꿔야댐
        else :
            return False
    
    def insert(self, data) : # 힙에 데이터 삽입
        if len(self.heap_array) == 0 : # 힙에 데이터가 없는 경우
            self.heap_array.append(None)
            self.heap_array.append(data) 
            return True

        self.heap_array.append(data) # 일단 왼쪽 하단에 데이터 삽입

        inserted_idx = len(self.heap_array) - 1
        # 삽입된 데이터의 위치

        while self.move_up(inserted_idx) : # 부모 자식 바꿔야 되면 계속 바꿈
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            # 부모 자식 데이터 스왑        
            inserted_idx = parent_idx
            # 스왑했으니 인덱스 위치 바꾸고 다시 체크

    def move_down(self, popped_idx) :
        l_child_idx = popped_idx * 2
        r_child_idx = (popped_idx * 2) + 1
        
        if len(self.heap_array) - 1 < l_child_idx : # 자식 없는 경우
            return False

        elif len(self.heap_array) - 1 == l_child_idx : # 왼쪽 자식만 있는 경우
            if self.heap_array[l_child_idx] > self.heap_array[popped_idx] :
                # 왼쪽 자식이 부모 보다 크면
                return True
            else :
                return False

        else : # 왼쪽 오른쪽 둘다 자식 있는 경우
            if self.heap_array[l_child_idx] > self.heap_array[r_child_idx] :
                # 왼쪽 자식이 오른쪽 자식보다 크면
                if self.heap_array[l_child_idx] > self.heap_array[popped_idx] :
                # 왼쪽 자식이 부모보다 크면
                    return True
                else :
                    return False
            else :
                if self.heap_array[r_child_idx] > self.heap_array[popped_idx] :
                # 오른쪽 자식이 부모보다 크면
                    return True
                else :
                    return False
            
    def pop(self) :
        if len(self.heap_array) <= 1 :
            return None # 암것도 안들어 있으면 None 리턴

        last_idx = len(self.heap_array) - 1
        self.heap_array[last_idx], self.heap_array[1] = self.heap_array[1], self.heap_array[last_idx]
        # 루트 노트랑 마지막 노드랑 데이터 스왑
        popped_data = self.heap_array.pop() # 마지막 데이터 꺼내기
        popped_idx = 1
        
        while self.move_down(popped_idx) : # 부모 자식 바꿔야 되면 계속 바꿈
            l_child_idx = popped_idx * 2
            r_child_idx = (popped_idx * 2) + 1
            
            if len(self.heap_array) - 1 == l_child_idx : # 왼쪽 자식만 있는 경우
                self.heap_array[l_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[l_child_idx]
                # 스왑
                popped_idx = l_child_idx
            else :
                if self.heap_array[l_child_idx] > self.heap_array[r_child_idx] :
                # 왼쪽 자식이 오른쪽 자식보다 크면
                    self.heap_array[l_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[l_child_idx]
                    # 스왑
                    popped_idx = l_child_idx
                else : # 오른쪽 자식이 더 크면 오른쪽 자식과 스왑
                    self.heap_array[r_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[r_child_idx]
                    popped_idx = r_child_idx

        return popped_data
            

        

