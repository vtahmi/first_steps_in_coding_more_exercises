import math
alley = 1
study_width = 0.70
study_length = 1.20
length = float(input())
width = float(input())
total_width = width - 1
total_area = math.floor(length * total_width)
print(total_area)
total_study_area = math.ceil(study_width * study_length)
print(total_study_area)



# import math
# alley = 1
# study_width = 0.70
# study_length = 1.20
# length = float(input())
# width = float(input())
# total_width = width - alley
# avail_width = math.floor(total_width / study_width)
# avail_length = math.floor(length / study_length)
# avail_area = avail_width * avail_length - 3
# print(avail_area)
