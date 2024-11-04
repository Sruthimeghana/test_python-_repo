# import time
# time.sleep(3)
# print("TIME IS UP......!")
#   output:TIME IS UP......!

# import time
# s = int(input("Enter the Seconds :"))
# for x in range(0,s):
#      time.sleep(5)
# print("TIME is UP.......!")
# output:
# Enter the Seconds :4
# TIME is UP.......!

# import time
# s = int(input("Enter the Seconds :"))
# for x in range(0,s):
#      print(x)
#      time.sleep(5)
# print("TIME is UP.......!")
# output:
# Enter the Seconds :4
# 0
# 1
# 2
# 3
# TIME is UP.......!
# reverse count:
# import time
# s = int(input("Enter the Seconds :"))
# for x in  range(s,0,-1): # reverse range
#      print(x)
#      time.sleep(5)
# print("TIME is UP.......!")
# output:
# Enter the Seconds :5
# 5
# 4
# 3
# 2
# 1
# TIME is UP.......!
# _________________________________________________

# second results:
# import time
# s = int(input("Enter the Seconds :"))
# for x in  range(s,0,-1): # reverse range
#      seconds = x %60  # modules gives   division remainder value
#      print(f"00:00:{seconds}")
#      time.sleep(5)
# print("TIME is UP.......!")
# output:
# Enter the Seconds :3
# 00:00:3
# 00:00:2
# 00:00:1
# TIME is UP.......!


# import time
# s = int(input("Enter the Seconds :"))
# for x in range(s, 0, -1):
#     seconds = x % 60
#     minutes = (x /60) % 60
#     hours = x / 3600
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("TIME is UP.......!")
# # Output:
# 00:01:05
# 00:01:04
# 00:01:03
# 00:01:02
# 00:01:01count down seconds pgrm.py
# 00:01:00

# import time
# s = int(input("Enter the Seconds :"))
# for x in range(s, 0, -1):
#     seconds = x % 60
#     minutes = int(x /60) % 60
#     hours =  int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("TIME is UP.......!")
# output:
# 01:00:05
# 01:00:04
# 01:00:03
# 01:00:02
# 01:00:01
# 01:00:00







