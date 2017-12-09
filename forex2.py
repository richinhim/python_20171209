lst = [1,2,3,4,5,6,7,8]

for i in lst:
    print(i)
    if i % 2 == 1: continue
    if i == 6: break
    print(i,"번 출력되었습니다.")

message = "Hello!"

for item in message:
   #print("문자열 Hello!를 순차적으로 출력한다.")
    print(item)
#print()